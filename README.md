# Terraquery

GIS powered by natural language based SQL generation, implemented with Ventura County geospatial data. Current version allows clients to query for city and road data.



### Run the API Locally

- Create a virtual environment and install the required libraries (Windows)

  ```
  >> virtualenv env
  
  >> source env/Scripts/activate
  
  >> pip install -r local_requirements.txt
  ```

- **TODO: Pip Dependencies!!!**

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



### Recommended Verbiage

For best results, the following verbiage is recommended when sending requests to the API.

- Find
  - Search for
  - Retrieve
  - Get
  - List
- City
  - Town
  - Municipality
  - Urban area
- Road
  - road
  - street
  - highway
  - route
  - way
- People
  - residents
  - inhabitants
- Intersections
  - Intersections
  - Roads that intersect
  - Intersecting roads
  - Roads that cross each other
- Kilometers
  - km
- Square Kilometers
  - sq km

- Fewest roads
  - Least number of roads
- Most roads
  - Greatest number of roads
- That intersect the point
  - That intersect
  - That intersect the point at
  - That cross
- Roads that are longer than
- Roads that are shorter than
- Roads that are at most
- Roads that span at least
- Roads that span at most
- Roads within
  - All roads within
- An area greater than
  - An area larger than
  - Greater than
  - Larger than
- An area less than
  - An area smaller than
  - Less than
  - Smaller than
- An area of at least
  - An area no less than
  - At least
  - No less than
- An area of at most
  - An area no more than
  - At most
  - No more than
- The largest area
  - The greatest area
- A population greater than
  - A population that is greater than
  - More than
  - A population larger than
  - A population that is larger than
  - A population that is over
  - Over
- A population less than
  - A population that is less than
  - less than
  - A population smaller than
  - A population that is smaller than
  - A population that is under
  - Under
- A population of at least
  - At least
  - A population no less than
  - No less than
- A population of at most
  - At most
  - A population of at most
  - No more than
- City with the highest population
  - City with the most people
  - Busiest city
- City with the lowest population
  - City with the least people
  - Slowest city