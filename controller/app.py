from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

model_path = "../terraquery_model" # was ./terraquery_model
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def get_schema():
    return "Assume the schema: CREATE EXTENSION postgis; CREATE TABLE cities (id SERIAL PRIMARY KEY, name VARCHAR(255), population INTEGER, boundary GEOMETRY(Polygon, 4326)); CREATE TABLE roads (id SERIAL PRIMARY KEY, name VARCHAR(255), route GEOMETRY(LineString, 4326)); CREATE TABLE parks (id SERIAL PRIMARY KEY, name VARCHAR(255), boundary GEOMETRY(Polygon, 4326)); CREATE TABLE owning_entities (id SERIAL PRIMARY KEY, name VARCHAR(255), is_group BOOLEAN); CREATE TABLE buildings (id SERIAL PRIMARY KEY, street_number VARCHAR(10), location GEOMETRY(Point, 4326), road_id INTEGER REFERENCES roads(id), owning_entity_id INTEGER REFERENCES owning_entities(id)) - "

def generate_sql_for_natural_language_query(natural_language_query):
    input_query = natural_language_query + ". " + get_schema()
    prompt = f"Query: {input_query}\nSQL:"
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=500,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    sql_start = generated_text.find("SQL:") + len("SQL:")
    sql_query = generated_text[sql_start:].strip()
    
    return sql_query

@app.route('/v1/generated-sql-queries', methods=['GET'])
def get_generated_sql():
    natural_language_query = request.args.get('natural-language-query')
    if not natural_language_query:
        return jsonify({"error": "Missing 'natural-language-query' parameter"}), 400
    
    sql_query = generate_sql_for_natural_language_query(natural_language_query)
    return jsonify({"natural-language-query": natural_language_query, "generated-sql-query": sql_query})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
