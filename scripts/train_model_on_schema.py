from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

model_path = "C:/Users/dkala/projects/terraquery/t5_small"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

dataset = load_dataset("json", data_files="scripts/terraquery_dataset.json")

def preprocess_function(examples):
    input_texts = [f"Translate to SQL: {query}" for query in examples["natural-language"]]
    target_texts = examples["sql"]
    
    inputs = tokenizer(input_texts, truncation=True, padding="max_length", max_length=256)
    targets = tokenizer(target_texts, truncation=True, padding="max_length", max_length=256)

    inputs["labels"] = targets["input_ids"]
    return inputs

dataset = dataset["train"].train_test_split(test_size=0.2)
tokenized_datasets = dataset.map(preprocess_function, batched=True)

training_args = TrainingArguments(
    output_dir="./terraquery_model_v3",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_steps=10,
    remove_unused_columns=False,
    num_train_epochs=3
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

trainer.train()

model.save_pretrained("./terraquery_model_v3")
tokenizer.save_pretrained("./terraquery_model_v3")
