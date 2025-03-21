from datasets import load_dataset

from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

# Load the pre-trained model and tokenizer from the Spider training
model = GPT2LMHeadModel.from_pretrained("../terraquery_model_spider")
tokenizer = GPT2Tokenizer.from_pretrained("../terraquery_model_spider")

# Load your custom dataset
dataset = load_dataset("json", data_files="terraquery_dataset.json")

# Preprocessing function for your custom dataset
def preprocess_function(examples):
    input_texts = [f"Query: {natural_language}\nSQL: {sql}" for natural_language, sql in zip(examples["natural-language"], examples["sql"])]
    encoding = tokenizer(input_texts, truncation=True, padding="max_length", max_length=256, return_tensors="pt")
    encoding["labels"] = encoding["input_ids"]
    return encoding

# Split dataset into training and test sets (adjust as needed)
dataset = dataset["train"].train_test_split(test_size=0.2)
tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Set up fine-tuning training arguments
training_args = TrainingArguments(
    output_dir="../terraquery_model",  # Model output directory for fine-tuned model
    per_device_train_batch_size=2,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="../logs",
    logging_steps=10,
    remove_unused_columns=False,
)

# Initialize Trainer for fine-tuning
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

# Fine-tune the model on your custom schema data
trainer.train()

# Save the fine-tuned model and tokenizer
model.save_pretrained("../terraquery_model")
tokenizer.save_pretrained("../terraquery_model")
