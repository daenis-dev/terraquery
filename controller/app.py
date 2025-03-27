import psycopg2
import folium
from flask import Flask, request, render_template_string
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import json
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

app = Flask(__name__)

model_path = "./terraquery_model"
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

def execute_and_get_result_set_for_results(description):
    columns = [desc[0] for desc in description]
    allowed_pairs = [
        ("name", "boundary"),
        ("name", "route"),
        ("street_number", "location"),
    ]

    selected_pair = next(
        ((name_field, geom_field) for name_field, geom_field in allowed_pairs if name_field in columns and geom_field in columns),
        None
    )

    if not selected_pair:
        return "Error: Query must return one of the following field pairs: (name, boundary), (name, route), or (street_number, location)."

    return selected_pair

def get_geom_for_row(row, description, name_field, geom_field):
    columns = [desc[0] for desc in description]
    row_dict = dict(zip(columns, row))
    name = row_dict.get(name_field, "Unnamed")
    geom_geojson = row_dict.get(geom_field)

    if geom_geojson:
        try:
            return json.loads(geom_geojson)
        except Exception as e:
            print(f"Error loading GeoJSON for {name}: {e}")

def get_webmap_for_spatial_query(sql_query):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute(sql_query)

        name_field, geom_field = execute_and_get_result_set_for_results(cursor.description)

        m = folium.Map(location=[34.2746, -119.2290], zoom_start=11)

        for row in cursor.fetchall():
            columns = [desc[0] for desc in cursor.description]
            row_dict = dict(zip(columns, row))
            name = row_dict.get(name_field, "Unnamed")

            geom = get_geom_for_row(row, cursor.description, name_field, geom_field)

            if geom["type"] == "Point":
                folium.Marker(
                    location=[geom["coordinates"][1], geom["coordinates"][0]],
                    popup=name,
                    icon=folium.Icon(color="red")
                ).add_to(m)
            elif geom["type"] in ["Polygon", "MultiPolygon"]:
                folium.GeoJson(
                    geom,
                    name=name,
                    style_function=lambda x: {"color": "blue", "fillColor": "#0000ff", "fillOpacity": 0.2}
                ).add_to(m)
            elif geom["type"] in ["LineString", "MultiLineString"]:
                folium.GeoJson(
                    geom,
                    name=name,
                    style_function=lambda x: {"color": "red", "weight": 3, "opacity": 1}
                ).add_to(m)

        cursor.close()
        conn.close()

        return m._repr_html_()

    except Exception as e:
        return f"Error: {e}"

@app.route('/v1/generated-sql-queries', methods=['GET'])
def get_generated_sql():
    natural_language_query = request.args.get('natural-language-query')
    if not natural_language_query:
        return jsonify({"error": "Missing 'natural-language-query' parameter"}), 400
    
    sql_query = generate_sql_for_natural_language_query(natural_language_query)

    webmap_html = get_webmap_for_spatial_query(sql_query)
    
    return render_template_string("""
        <html>
            <head>
                <title>Generated Web Map</title>
            </head>
            <body>
                <h2>Natural Language Query: {{ query }}</h2>
                <h3>Generated SQL Query:</h3>
                <pre>{{ sql }}</pre>
                <h3>Generated Web Map:</h3>
                {{ webmap|safe }}
            </body>
        </html>
    """, query=natural_language_query, sql=sql_query, webmap=webmap_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
