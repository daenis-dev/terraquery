from base_queries import BASE_QUERIES
from city_queries import CITY_QUERIES
from road_queries import ROAD_QUERIES

city_queries = 0
road_queries = 0
park_queries = 0
building_queries = 0

for query in CITY_QUERIES:
    if ('Find cities' in query['natural-language'] or 
        'Find the city' in query['natural-language'] or 
        'Find all cities' in query['natural-language'] or 
        'Find the northernmost city' in query['natural-language'] or 
        'Find the southernmost city' in query['natural-language'] or 
        'Find the easternmost city' in query['natural-language'] or 
        'Find the westernmost city' in query['natural-language']):
        city_queries += 1
for query in ROAD_QUERIES:
    if ('Find roads' in query['natural-language'] or 
        'Find the road' in query['natural-language'] or 
        'Find all roads' in query['natural-language'] or 
        'Find the longest road' in query['natural-language'] or 
        'Find the shortest road' in query['natural-language'] or 
        'Find the northernmost road' in query['natural-language'] or 
        'Find the southernmost road' in query['natural-language'] or 
        'Find the easternmost road' in query['natural-language'] or 
        'Find the westernmost road' in query['natural-language']):
        road_queries += 1
for query in BASE_QUERIES:
    if ('Find parks' in query['natural-language'] or 
        'Find the park' in query['natural-language'] or 
        'Find all parks' in query['natural-language'] or
        'Find the largest park' in query['natural-language'] or 
        'Find the smallest park' in query['natural-language'] or 
        'Find the northernmost park' in query['natural-language'] or 
        'Find the southernmost park' in query['natural-language'] or 
        'Find the easternmost park' in query['natural-language'] or 
        'Find the westernmost park' in query['natural-language']):
        park_queries += 1

    if ('Find buildings' in query['natural-language'] or 
        'Find the building' in query['natural-language'] or 
        'Find all buildings' in query['natural-language'] or
        'Find the northernmost building' in query['natural-language'] or 
        'Find the southernmost building' in query['natural-language'] or 
        'Find the easternmost building' in query['natural-language'] or 
        'Find the westernmost building' in query['natural-language']):
        building_queries += 1

print('Number of city queries: ' + str(city_queries), flush=True)
print('Number of road queries: ' + str(road_queries), flush=True)
print('Number of park queries: ' + str(park_queries), flush=True)
print('Number of building queries: ' + str(building_queries), flush=True)