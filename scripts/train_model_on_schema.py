from datasets import load_dataset

from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

# TODO: Train a version without the owner queries

model_path = "C:/Users/dkala/projects/terraquery/distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("json", data_files="scripts/terraquery_dataset.json")

def preprocess_function(examples):
    input_texts = [f"Query: {natural_language}\nSQL: {sql}" for natural_language, sql in zip(examples["natural-language"], examples["sql"])]
    encoding = tokenizer(input_texts, truncation=True, padding="max_length", max_length=256, return_tensors="pt")
    encoding["labels"] = encoding["input_ids"]
    return encoding

dataset = dataset["train"].train_test_split(test_size=0.2)
tokenized_datasets = dataset.map(preprocess_function, batched=True)

training_args = TrainingArguments(
    output_dir="./terraquery_model",
    per_device_train_batch_size=2,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    remove_unused_columns=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

trainer.train()

model.save_pretrained("./terraquery_model")
tokenizer.save_pretrained("./terraquery_model")
