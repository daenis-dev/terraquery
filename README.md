# Terraquery

GIS powered by natural language based SQL generation, implemented with Ventura County geospatial data. Current version allows clients to query for city and road data.



### Run the API Locally

- Create a virtual environment and install the required libraries (Windows)

  ```
  >> virtualenv env
  
  >> source env/Scripts/activate
  
  >> pip install -r local_requirements.txt
  ```

- Download the model from Hugging Face and copy the model to the project directory:

  ```
  >> huggingface-cli download google-t5/t5-small --repo-type model
  
  >> mv C:/Users/USERNAME/.cache/huggingface/hub/models--google-t5--t5-small/snapshots/df1b.. C:/Users/USERNAME/projects/terraquery/t5_small
  ```
  
- Add a *scripts/config.py* file:

  ```
  DB_NAME = "terraquery"
  DB_USER = "postgres"
  DB_PASSWORD = "changeit"
  DB_HOST = "host.docker.internal"
  DB_HOST_LOCAL = "localhost"
  DB_PORT = "5432"
  ```

- Create a Postgres database according to the *config.py* file, and run the *database/schema.sql* script

- Generate the training data

  ```
  >> py scripts/generate_data.py
  ```

- Train the model

  ```
  >> py scripts/train_model_on_data.py
  ```

- Build the application

  ```
  >> docker build --no-cache -t terraquery .
  
  >> docker run -p 9090:9090 --name terraquery-container -d terraquery
  ```



### API

**URL:** http://docker.host.internal/v1/generated-sql-queries

**Method:** GET

**URL Encoded Parameters:**

- natural-language-query: a plain text request for the GIS



### Schema

Includes extensions and tables; indexes and data are included in *database/schema.sql*

```sql
CREATE EXTENSION postgis;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    population INTEGER,
    boundary GEOMETRY(MultiPolygon, 4326)
);
CREATE TABLE roads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    route GEOMETRY(MultiLineString, 4326)
);
CREATE TABLE parks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    boundary GEOMETRY(MultiPolygon, 4326)
);
CREATE TABLE owning_entities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    is_group BOOLEAN
);
CREATE TABLE buildings (
    id SERIAL PRIMARY KEY,
    street_number VARCHAR(10),
    location GEOMETRY(Point, 4326),
    road_id INTEGER REFERENCES roads(id),
    owning_entity_id INTEGER REFERENCES owning_entities(id)
);
```



### Project File Structure

```
terraquery
	- controller
		- app.py
	- database
		- schema.sql
	- scripts
		- base_query_analyzer.py (count training data)
		- city_queries.py (base queries for cities)
		- road_queries.py (base queries for roads)
		- config.py
		- generate_data.py (generate training data from base queries)
		- test_base_queries.py (execute and validate base queries)
		- train_model_on_schema.py (create model from training data)
		- view_webmap.py (visualize data)
	- Dockerfile
	- requirements.txt
```
