import psycopg2
import json
import random
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from base_queries import BASE_QUERIES
import random
import re

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()

query_variations = {
        "Find": ["Find", "Search", "Retrieve", "Get", "List"],

        "cities": ["cities", "towns", "municipalities", "urban areas"],
        "city": ["city", "town", "municipality", "urban area"],
        "a population greater than": ["a population greater than", "a population that is greater than", "more than", "a population larger than", "a population that is larger than", "over"], # TODO: If 'population', the word 'people' at the end is optional
        "a poulation less than": ["a poulation less than", "a poulation that is less than", "less than", "a population smaller than", "a population that is smaller than", "under"], # TODO: If 'population', the word 'people' at the end is optional
        "a population of at least": ["a population of at least", "at least", "a population of no less than", "no less than"], # TODO: If 'population', the word 'people' at the end is optional
        "a population of at most": ["a population of at most", "at most", "a population of no more than", "no more than"], # TODO: If 'population', the word 'people' at the end is optional
        "square kilometer": ["square kilometer", "sq km"],
        "square kilometers": ["square kilometers", "sq km"],
        "kilometer": ["kilometer", "km"],
        "kilometers": ["kilometers", "km"],
        "an area greater than": ["an area greater than", "an area larger than", "greater than", "larger than"],
        "an area less than": ["an area less than", "an area smaller than", "less than", "smaller than"],
        "an area of at least": ["an area of at least", "an area no less than", "at least", "no less than"],
        "an area of at most": ["an area of at most", "an area no more than", "at most", "no more than"],
        "the largest area": ["the largest area", "the greatest area"],
        
        "building that is owned by an individual": ["building that is owned by an individual", "building that belongs to an individual", "building that is not owned by a group", "building that does not belong to a group"],
        "buildings that are owned by individuals": ["buildings that are owned by individuals", "buildings that belong to individuals", "buildings that are not owned by groups", "buildings that do not belong to groups"],
        "building that is owned by a group": ["building that is owned by a group", "building that belongs to a group", "building that is not owned by an individual", "building that does not belong to an individual"],
        "buildings that are owned by groups": ["buildings that are owned by groups", "buildings that belong to groups", "buildings that are not owned by individuals", "buildings that do not belong to individuals"],
        "buildings": ["buildings", "structures", "facilities", "establishments"],
        "building": ["building", "structure", "facility", "establishment"],

        "intersections": ["intersections", "roads that intersect", "intersecting roads", "roads that cross each other"],
        "fewest roads": ["fewest roads", "least number of roads"],
        "that intersect the point": ["that intersect the point", "that intersect", "that intersect the point at", "that cross"],
        "roads that are longer than": ["roads that are longer than"],
        "roads that are at least": ["roads that are at least"],
        "roads that are shorter than": ["roads that are shorter than"],
        "roads that are at most": ["roads that are at most"],
        "roads that span at least": ["roads that span at least"],
        "roads that span at most": ["roads that span at most"],

        "greatest number of parks": ["greatest number of parks", "most parks", "highest number of parks"],
        "fewest number of parks" : ["fewest number of parks", "fewest parks", "lowest number of parks"],
        "parks": ["parks", "green spaces", "recreational areas", "natural reserves"],
        "park": ["park", "green space", "recreational area", "natural reserve"],

        "within the area bound by": ["in the area of", "within the region", "inside the boundary", "inside the boundary of", "nearby", "in", "in the area bound by"],
        
        
        "roads": ["roads", "streets", "highways", "routes", "ways"],
        "road": ["road", "street", "highway", "route", "way"],
        "people": ["people", "residents", "inhabitants"],
        
        "owners": ["owners", "proprietors", "landlords", "holders"],
        "owner": ["owner", "proprietor", "landlord", "holder"]
    }

generated_queries_set = set(query["natural-language"] for query in BASE_QUERIES)

new_queries = []

def generate_query_variation(query):
    for key, variations in query_variations.items():
        if key in query:
            query = query.replace(key, random.choice(variations))

    return query

def get_schema():
    return "Assume the schema: CREATE EXTENSION postgis; CREATE TABLE cities (id SERIAL PRIMARY KEY, name VARCHAR(255), population INTEGER, boundary GEOMETRY(Polygon, 4326)); CREATE TABLE roads (id SERIAL PRIMARY KEY, name VARCHAR(255), route GEOMETRY(LineString, 4326)); CREATE TABLE parks (id SERIAL PRIMARY KEY, name VARCHAR(255), boundary GEOMETRY(Polygon, 4326)); CREATE TABLE owning_entities (id SERIAL PRIMARY KEY, name VARCHAR(255), is_group BOOLEAN); CREATE TABLE buildings (id SERIAL PRIMARY KEY, street_number VARCHAR(10), location GEOMETRY(Point, 4326), road_id INTEGER REFERENCES roads(id), owning_entity_id INTEGER REFERENCES owning_entities(id))"

def generate_dynamic_queries(num_new_queries=100):
    for _ in range(num_new_queries):
        new_query = get_random_query_from_base_queries()
        new_query["natural-language"] = generate_query_variation(new_query["natural-language"]) + ". " + get_schema()

        while new_query["natural-language"] in generated_queries_set:
            new_query = get_random_query_from_base_queries()
            new_query["natural-language"] = generate_query_variation(new_query["natural-language"]) + ". " + get_schema()

        new_queries.append(new_query)
        generated_queries_set.add(new_query["natural-language"])
    
    return new_queries

def get_random_query_from_base_queries():
    return random.choice(BASE_QUERIES).copy()


def test_query(query):
    try:
        cur.execute(query["sql"])
        result = cur.fetchall()
        if len(result) > 0:
            # print(f"Query '{query['natural-language']}' returned {len(result)} results.")
            return True
        else:
            # print(f"Query '{query['natural-language']}' returned no results.")
            return False
    except Exception as e:
        print('Failed query: ' + str(query["sql"]), flush=True)
        # print(f"Error executing query '{query['natural-language']}': {str(e)}")
        return False

def retry_failed_query(query):
    # print(f"Retrying query '{query['natural-language']}' after failure.")
    new_query = get_random_query_from_base_queries()
    new_query["natural-language"] = generate_query_variation(new_query["natural-language"]) + ". " + get_schema()
    
    while new_query["natural-language"] in generated_queries_set:
        new_query = get_random_query_from_base_queries()
        new_query["natural-language"] = generate_query_variation(new_query["natural-language"]) + ". " + get_schema()
        
    return new_query

def reset_transaction():
    # print("Rolling back the transaction due to an error...")
    conn.rollback()

new_queries = generate_dynamic_queries(3600)

with open('scripts/terraquery_dataset.json', 'w') as f:
    json.dump(new_queries, f, indent=4)

for query in new_queries:
    passed = test_query(query)
    retries = 0
    while not passed and retries < 3:
        reset_transaction()
        query = retry_failed_query(query)
        passed = test_query(query)
        retries += 1

cur.close()
conn.close()
