from __future__ import annotations

import argparse
import json
import math
import random
import re
import shutil
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import numpy as np
import torch
from sklearn.model_selection import StratifiedKFold, train_test_split
from torch.utils.data import Dataset
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    EarlyStoppingCallback,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    TrainerCallback,
    TrainerControl,
    TrainerState,
    TrainingArguments,
    set_seed,
)


Entry = Dict[str, Any]

DEFAULT_MODEL_NAME = "google/flan-t5-small"
TASK_PREFIX = "Generate TerraQuery LiDAR spec: "


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fine-tune FLAN-T5 Small to convert TerraQuery natural language queries into JSON specs."
    )
    parser.add_argument("--data", default="dataset_augmented.jsonl")
    parser.add_argument("--output-dir", default="terraquery-flan-t5-small-v2")
    parser.add_argument("--model-name", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--test-size", type=float, default=0.10)
    parser.add_argument("--val-size", type=float, default=0.10)
    parser.add_argument("--max-input-length", type=int, default=128)
    parser.add_argument("--max-target-length", type=int, default=512)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--eval-batch-size", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--warmup-ratio", type=float, default=0.06)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=2)
    parser.add_argument("--early-stopping-patience", type=int, default=4)
    parser.add_argument("--k-folds", type=int, default=0)
    parser.add_argument("--overwrite-output-dir", action="store_true")
    parser.add_argument("--no-train", action="store_true")
    return parser.parse_args()


def progress_bar(label: str, current: int, total: int, width: int = 36) -> None:
    if total <= 0:
        return
    percent = min(100, int((current / total) * 100))
    filled = min(width, int(width * current / total))
    bar = "█" * filled + "░" * (width - filled)
    print(f"\r{label}: [{bar}] {percent:3d}% ({current:,}/{total:,})", end="", flush=True)
    if current >= total:
        print()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def pretty_target_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).lower()


def load_jsonl(path: Path) -> List[Entry]:
    if not path.exists():
        raise FileNotFoundError(f"Training data not found: {path}")

    entries: List[Entry] = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL on line {line_number}: {exc}") from exc

            if "input" not in entry or "output" not in entry:
                raise ValueError(f"Line {line_number} must contain 'input' and 'output'")
            if not isinstance(entry["input"], str):
                raise ValueError(f"Line {line_number}: input must be a string")
            if not isinstance(entry["output"], dict):
                raise ValueError(f"Line {line_number}: output must be a JSON object")

            entries.append(entry)

    return entries


def validate_schema(entries: List[Entry]) -> None:
    required_top = {"intent", "target", "conditions", "filters", "ranking", "render"}

    for index, entry in enumerate(entries, start=1):
        output = entry["output"]
        missing = required_top - set(output.keys())
        if missing:
            raise ValueError(f"Entry {index}: output missing keys: {sorted(missing)}")

        proximity = output.get("conditions", {}).get("proximity", {})
        if "object" not in proximity or "distance_meters" not in proximity:
            raise ValueError(f"Entry {index}: conditions.proximity requires object and distance_meters")

        render = output.get("render", {})
        if "mode" not in render or "show" not in render:
            raise ValueError(f"Entry {index}: render requires mode and show")
        if not isinstance(render.get("show"), list):
            raise ValueError(f"Entry {index}: render.show must be a list")


def remove_duplicate_inputs(entries: List[Entry]) -> List[Entry]:
    deduped: List[Entry] = []
    seen_inputs: Dict[str, str] = {}

    for entry in entries:
        input_key = normalize_text(entry["input"])
        output_key = canonical_json(entry["output"])

        if input_key in seen_inputs:
            if seen_inputs[input_key] != output_key:
                raise ValueError(
                    "Conflicting labels found for input: "
                    f"{entry['input']!r}\n"
                    "Fix the dataset so each input maps to exactly one JSON spec."
                )
            continue

        seen_inputs[input_key] = output_key
        deduped.append(entry)

    return deduped


def spec_category(spec: Dict[str, Any]) -> str:
    target = spec.get("target")
    render = spec.get("render", {})
    ranking = spec.get("ranking", {})
    filters = spec.get("filters", {})

    if target == "utility":
        return "utility"
    if render.get("mode") == "context":
        return "context"

    ranking_type = ranking.get("type")
    if ranking_type:
        return f"ranking:{ranking_type}"

    if filters.get("min_height_meters") is not None:
        return "filter:min_height"
    if filters.get("min_cluster_size") is not None:
        return "filter:min_cluster"

    show = render.get("show", [])
    if show == ["vegetation", "encroachment"]:
        return "render:vegetation_encroachment"
    if show == ["structures", "encroachment"]:
        return "render:structures_encroachment"
    if show == ["encroachment"]:
        return "render:encroachment_only"

    return "basic"


def print_distribution(name: str, entries: List[Entry]) -> None:
    counts: Dict[str, int] = {}
    for entry in entries:
        category = spec_category(entry["output"])
        counts[category] = counts.get(category, 0) + 1

    print(f"\n{name} distribution ({len(entries):,} examples):")
    for category, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        pct = (count / max(1, len(entries))) * 100
        print(f"  {category:32s} {count:6,d}  {pct:5.1f}%")


def stratified_split(
    entries: List[Entry],
    test_size: float,
    val_size: float,
    seed: int,
) -> Tuple[List[Entry], List[Entry], List[Entry]]:
    labels = [spec_category(entry["output"]) for entry in entries]

    label_counts: Dict[str, int] = {}
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1

    small_labels = {label: count for label, count in label_counts.items() if count < 3}
    if small_labels:
        raise ValueError(
            "Some categories are too small for train/val/test stratification: "
            f"{small_labels}."
        )

    train_val, test = train_test_split(
        entries,
        test_size=test_size,
        random_state=seed,
        stratify=labels,
    )

    train_val_labels = [spec_category(entry["output"]) for entry in train_val]
    adjusted_val_size = val_size / max(1e-9, 1.0 - test_size)

    train, val = train_test_split(
        train_val,
        test_size=adjusted_val_size,
        random_state=seed,
        stratify=train_val_labels,
    )

    return list(train), list(val), list(test)


class TerraQueryDataset(Dataset):
    def __init__(
        self,
        entries: List[Entry],
        tokenizer: Any,
        max_input_length: int,
        max_target_length: int,
    ) -> None:
        self.entries = entries
        self.tokenizer = tokenizer
        self.max_input_length = max_input_length
        self.max_target_length = max_target_length

    def __len__(self) -> int:
        return len(self.entries)

    def __getitem__(self, index: int) -> Dict[str, Any]:
        entry = self.entries[index]
        source = TASK_PREFIX + entry["input"]
        target = pretty_target_json(entry["output"])

        model_inputs = self.tokenizer(
            source,
            max_length=self.max_input_length,
            truncation=True,
        )

        labels = self.tokenizer(
            text_target=target,
            max_length=self.max_target_length,
            truncation=True,
        )

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs


class SimpleProgressCallback(TrainerCallback):
    def __init__(self) -> None:
        self.last_percent = -1

    def on_train_begin(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        self.last_percent = -1
        print()

    def on_step_end(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        if not state.max_steps:
            return
        percent = int((state.global_step / state.max_steps) * 100)
        if percent != self.last_percent:
            self.last_percent = percent
            progress_bar("Training", state.global_step, state.max_steps)

    def on_train_end(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        if state.max_steps:
            progress_bar("Training", state.max_steps, state.max_steps)


def normalize_json_prediction(text: str) -> Optional[str]:
    text = text.strip()
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1 or end <= start:
        return None

    candidate = text[start : end + 1]

    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None

    return canonical_json(parsed)


def evaluate_json_exact_match(
    trainer: Seq2SeqTrainer,
    tokenizer: Any,
    entries: List[Entry],
    dataset: TerraQueryDataset,
    split_name: str,
    max_target_length: int,
) -> Dict[str, float]:
    print(f"\nRunning generation evaluation on {split_name} split...")

    predictions = trainer.predict(dataset, max_length=max_target_length)
    pred_ids = predictions.predictions

    if isinstance(pred_ids, tuple):
        pred_ids = pred_ids[0]

    decoded_preds = tokenizer.batch_decode(pred_ids, skip_special_tokens=True)

    total = len(entries)
    valid_json_count = 0
    exact_count = 0
    examples_to_print: List[Tuple[str, str, str]] = []

    for entry, pred_text in zip(entries, decoded_preds):
        pred_norm = normalize_json_prediction(pred_text)
        gold_norm = canonical_json(entry["output"])

        if pred_norm is not None:
            valid_json_count += 1

        if pred_norm == gold_norm:
            exact_count += 1
        elif len(examples_to_print) < 5:
            examples_to_print.append((entry["input"], pred_text, pretty_target_json(entry["output"])))

    valid_json_rate = valid_json_count / max(1, total)
    exact_match_rate = exact_count / max(1, total)

    print(f"{split_name} valid JSON rate: {valid_json_rate:.4f}")
    print(f"{split_name} exact JSON match: {exact_match_rate:.4f}")

    if examples_to_print:
        print(f"\nSample {split_name} mismatches:")
        for input_text, pred, gold in examples_to_print:
            print("-" * 80)
            print(f"Input: {input_text}")
            print(f"Pred : {pred}")
            print(f"Gold : {gold}")

    return {
        f"{split_name}_valid_json_rate": valid_json_rate,
        f"{split_name}_exact_match_rate": exact_match_rate,
    }


def run_k_fold_check(entries: List[Entry], k_folds: int, seed: int) -> None:
    if k_folds <= 1:
        return

    labels = [spec_category(entry["output"]) for entry in entries]
    label_counts: Dict[str, int] = {}

    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1

    min_count = min(label_counts.values())

    if min_count < k_folds:
        raise ValueError(
            f"Cannot run {k_folds}-fold stratified split. "
            f"Smallest category has only {min_count} examples."
        )

    print(f"\nRunning stratified {k_folds}-fold split sanity check...")
    splitter = StratifiedKFold(n_splits=k_folds, shuffle=True, random_state=seed)

    for fold, (train_idx, val_idx) in enumerate(splitter.split(entries, labels), start=1):
        print(f"  Fold {fold}: train={len(train_idx):,}, val={len(val_idx):,}")

    print("K-fold stratification sanity check complete.")


def build_training_args(args: argparse.Namespace, output_dir: Path, train_dataset_len: int) -> Seq2SeqTrainingArguments:
    steps_per_epoch = max(
        1,
        math.ceil(train_dataset_len / (args.batch_size * args.gradient_accumulation_steps)),
    )
    eval_steps = max(25, steps_per_epoch // 2)

    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    use_fp16 = torch.cuda.is_available() and not use_bf16

    common_kwargs = dict(
        output_dir=str(output_dir),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.eval_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        weight_decay=args.weight_decay,
        warmup_ratio=args.warmup_ratio,
        save_strategy="steps",
        eval_steps=eval_steps,
        save_steps=eval_steps,
        logging_steps=max(10, eval_steps // 5),
        save_total_limit=2,
        predict_with_generate=True,
        generation_max_length=args.max_target_length,
        generation_num_beams=4,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        report_to="none",
        fp16=use_fp16,
        bf16=use_bf16,
    )

    try:
        return Seq2SeqTrainingArguments(
            **common_kwargs,
            eval_strategy="steps",
        )
    except TypeError:
        return Seq2SeqTrainingArguments(
            **common_kwargs,
            evaluation_strategy="steps",
        )


def train() -> None:
    args = parse_args()

    set_seed(args.seed)
    random.seed(args.seed)
    np.random.seed(args.seed)

    data_path = Path(args.data)
    output_dir = Path(args.output_dir)

    if output_dir.exists() and args.overwrite_output_dir:
        shutil.rmtree(output_dir)

    if output_dir.exists() and any(output_dir.iterdir()) and not args.overwrite_output_dir:
        raise FileExistsError(
            f"Output directory already exists and is not empty: {output_dir}\n"
            "Use --overwrite-output-dir or choose a new --output-dir."
        )

    print(f"Loading data from {data_path}...")
    entries = load_jsonl(data_path)
    validate_schema(entries)
    entries = remove_duplicate_inputs(entries)

    print(f"Loaded {len(entries):,} unique examples.")
    print_distribution("Full dataset", entries)

    run_k_fold_check(entries, args.k_folds, args.seed)

    train_entries, val_entries, test_entries = stratified_split(
        entries=entries,
        test_size=args.test_size,
        val_size=args.val_size,
        seed=args.seed,
    )

    print_distribution("Train", train_entries)
    print_distribution("Validation", val_entries)
    print_distribution("Test", test_entries)

    if args.no_train:
        print("\n--no-train enabled; exiting after validation/splitting.")
        return

    print(f"\nLoading base model: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(args.model_name)

    train_dataset = TerraQueryDataset(train_entries, tokenizer, args.max_input_length, args.max_target_length)
    val_dataset = TerraQueryDataset(val_entries, tokenizer, args.max_input_length, args.max_target_length)
    test_dataset = TerraQueryDataset(test_entries, tokenizer, args.max_input_length, args.max_target_length)

    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        model=model,
        label_pad_token_id=-100,
    )

    training_args = build_training_args(args, output_dir, len(train_dataset))

    try:
        trainer = Seq2SeqTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            processing_class=tokenizer,
            data_collator=data_collator,
            callbacks=[
                SimpleProgressCallback(),
                EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience),
            ],
        )
    except TypeError:
        trainer = Seq2SeqTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            data_collator=data_collator,
            callbacks=[
                SimpleProgressCallback(),
                EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience),
            ],
        )

    print("\nStarting training...")
    trainer.train()

    print("\nEvaluating best model...")
    trainer.evaluate(eval_dataset=val_dataset)

    eval_metrics = evaluate_json_exact_match(
        trainer=trainer,
        tokenizer=tokenizer,
        entries=val_entries,
        dataset=val_dataset,
        split_name="validation",
        max_target_length=args.max_target_length,
    )

    test_metrics = evaluate_json_exact_match(
        trainer=trainer,
        tokenizer=tokenizer,
        entries=test_entries,
        dataset=test_dataset,
        split_name="test",
        max_target_length=args.max_target_length,
    )

    print("\nSaving final model/tokenizer...")
    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))

    metadata = {
        "base_model": args.model_name,
        "task_prefix": TASK_PREFIX,
        "train_examples": len(train_entries),
        "validation_examples": len(val_entries),
        "test_examples": len(test_entries),
        "validation_metrics": eval_metrics,
        "test_metrics": test_metrics,
        "max_input_length": args.max_input_length,
        "max_target_length": args.max_target_length,
    }

    with (output_dir / "terraquery_training_metadata.json").open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"\nDone. Model saved to: {output_dir}")
    print("\nUse this directory in your app with:")
    print(f"  AutoTokenizer.from_pretrained('{output_dir}')")
    print(f"  AutoModelForSeq2SeqLM.from_pretrained('{output_dir}')")


if __name__ == "__main__":
    train()
