import psycopg2
import json
import random
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_PORT, DB_HOST_LOCAL
from city_queries import CITY_QUERIES
from road_queries import ROAD_QUERIES
import random
import re

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST_LOCAL,
    port=DB_PORT
)

cur = conn.cursor()

BASE_QUERIES = CITY_QUERIES + ROAD_QUERIES

query_variations = {
        "Find": ["Find", "Search for", "Retrieve", "Get", "List"],

        "city with the highest population": ["city with the highest population", "city with the most people", "busiest city"],
        "city with the lowest population": ["city with the lowest population", "city with the least people", "slowest city"],
        "cities": ["cities", "towns", "municipalities", "urban areas"],
        "city": ["city", "town", "municipality", "urban area"],
        "a population greater than": ["a population greater than", "a population that is greater than", "more than", "a population larger than", "a population that is larger than", "a population that is over", "over"],
        "a poulation less than": ["a poulation less than", "a population that is less than", "less than", "a population smaller than", "a population that is smaller than", "a population that is under", "under"],
        "a population of at least": ["a population of at least", "at least", "a population of no less than", "no less than"],
        "a population of at most": ["a population of at most", "at most", "a population of no more than", "no more than"],
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
        "most roads": ["most roads", "greatest number of roads"],
        "that intersect the point": ["that intersect the point", "that intersect", "that intersect the point at", "that cross"],
        "roads that are longer than": ["roads that are longer than"],
        "roads that are at least": ["roads that are at least"],
        "roads that are shorter than": ["roads that are shorter than"],
        "roads that are at most": ["roads that are at most"],
        "roads that span at least": ["roads that span at least"],
        "roads that span at most": ["roads that span at most"],
        "roads within": ["roads within", "all roads within"],

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

def generate_dynamic_queries():
    index = 0
    for _ in range(len(BASE_QUERIES)):
        new_query = get_next_query_from_base_queries(index)
        new_query["natural-language"] = generate_query_variation(new_query["natural-language"]) + ". " + get_schema()
        new_queries.append(new_query)
        generated_queries_set.add(new_query["natural-language"])
        index += 1
        print('Query number: ' + str(index), flush=True)
    
    return new_queries

def get_next_query_from_base_queries(index):
    query = BASE_QUERIES[index]
    index += 1
    print('query number: ' + str(index), flush=True)
    return query


def test_query(query):
    try:
        cur.execute(query["sql"])
        result = cur.fetchall() # TODO: Gets hung up on last entry
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

new_queries = generate_dynamic_queries()

with open('scripts/terraquery_dataset.json', 'w') as f:
    json.dump(new_queries, f, indent=4)

for query in new_queries:
    test_query(query)

cur.close()
conn.close()
