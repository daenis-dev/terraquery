from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import json
import re

MODEL_DIR = "./terraquery-flan-t5-small-v2"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

print("Loading model...")
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

device = "mps" if torch.backends.mps.is_available() else "cpu"
model = model.to(device)
model.eval()

app = FastAPI()


class SpecRequest(BaseModel):
    query: str


def repair_flat_spec(raw: str):
    text = raw.strip()

    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]

    try:
        return json.loads(text)
    except Exception:
        pass

    def number_after(key, default=None):
        match = re.search(rf'"{key}"\s*:\s*([0-9.]+)', text)
        return float(match.group(1)) if match else default

    def string_after(key, default=None):
        match = re.search(rf'"{key}"\s*:\s*"([^"]+)"', text)
        return match.group(1) if match else default

    def null_or_string_after(key, default=None):
        match = re.search(rf'"{key}"\s*:\s*(null|"[^"]+")', text)
        if not match:
            return default
        value = match.group(1)
        return None if value == "null" else value.strip('"')

    def null_or_number_after(key, default=None):
        match = re.search(rf'"{key}"\s*:\s*(null|[0-9.]+)', text)
        if not match:
            return default
        value = match.group(1)
        if value == "null":
            return None
        num = float(value)
        return int(num) if num.is_integer() else num

    show_match = re.search(r'"show"\s*:\s*\[([^\]]*)\]', text)
    show = ["structures", "vegetation", "encroachment"]

    if show_match:
        show = re.findall(r'"([^"]+)"', show_match.group(1))

    distance = number_after("distance_meters", 2)
    if distance is not None and float(distance).is_integer():
        distance = int(distance)

    return {
        "intent": string_after("intent", "encroachment_analysis"),
        "target": string_after("target", "structures"),
        "conditions": {
            "proximity": {
                "object": string_after("object", "vegetation"),
                "distance_meters": distance,
            }
        },
        "filters": {
            "min_height_meters": null_or_number_after("min_height_meters", None),
            "min_cluster_size": null_or_number_after("min_cluster_size", None),
        },
        "ranking": {
            "type": null_or_string_after("type", None),
            "top_n": null_or_number_after("top_n", None),
        },
        "render": {
            "mode": string_after("mode", "highlight"),
            "show": show,
        },
    }


@app.post("/generate-spec")
def generate_spec(request: SpecRequest):
    prompt = f"Generate TerraQuery LiDAR spec: {request.query}"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=128,
    )

    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            num_beams=4,
            do_sample=False,
        )

    decoded = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    )

    try:
        spec = repair_flat_spec(decoded)

        print("\n===================================================")
        print("Generated TerraQuery Spec")
        print("===================================================")
        print(f"Query: {request.query}")
        print("")
        print(json.dumps(spec, indent=2))
        print("===================================================\n")

    except Exception as exc:
        print("\n===================================================")
        print("SPEC GENERATION FAILED")
        print("===================================================")
        print(f"Query: {request.query}")
        print("")
        print(decoded)
        print("===================================================\n")

        return {
            "success": False,
            "raw_output": decoded,
            "error": str(exc),
        }

    return {
        "success": True,
        "spec": spec,
        "raw_output": decoded,
    }