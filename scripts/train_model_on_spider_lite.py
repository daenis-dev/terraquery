from datasets import load_dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
import numpy as np

def get_dataset():
    return load_dataset("json", data_files={
        "train": "../spider/data/processed_train_spider.json",
        "dev": "../spider/data/processed_dev_spider.json"
        }
    )

def queries_that_occur_at_least_twice_in(dataset):
    train_df = pd.DataFrame(dataset["train"])
    threshold = 2
    sql_counts = train_df["sql"].value_counts()
    frequent_sqls = sql_counts[sql_counts >= threshold].index

    return train_df[train_df["sql"].isin(frequent_sqls)]

dataset = get_dataset()

train_df = queries_that_occur_at_least_twice_in(dataset)

random_classes = np.random.choice(train_df["sql"].unique(), size=1000, replace=False)

train_df_sampled = train_df[train_df["sql"].isin(random_classes)]

train_df_sampled, _ = train_test_split(train_df_sampled, train_size=1000, stratify=train_df_sampled["sql"], random_state=42)

train_dataset = dataset["train"].select(train_df_sampled.index.tolist())

model_path = "C:/Users/dkala/projects/terraquery/distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def preprocess_function(examples):
    input_texts = [f"Query: {natural_language}\nSQL: {sql}" for natural_language, sql in zip(examples["natural-language"], examples["sql"])]
    encoding = tokenizer(input_texts, truncation=True, padding="max_length", max_length=256, return_tensors="pt")
    encoding["labels"] = encoding["input_ids"]
    return encoding

tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)

tokenized_datasets = tokenized_train_dataset.train_test_split(test_size=0.2)

training_args = TrainingArguments(
    output_dir="../terraquery_model_spider",
    per_device_train_batch_size=2,
    evaluation_strategy="epoch",
    save_strategy="epoch",
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

model.save_pretrained("../terraquery_model_spider")
tokenizer.save_pretrained("../terraquery_model_spider")
