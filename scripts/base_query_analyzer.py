from city_queries_v2 import CITY_QUERIES_V2
from road_queries_v2 import ROAD_QUERIES_V2

city_queries = 0
road_queries = 0
park_queries = 0
building_queries = 0

for query in CITY_QUERIES_V2:
    if ('Find cities' in query['natural-language'] or 
        'Find the city' in query['natural-language'] or 
        'Find all cities' in query['natural-language'] or 
        'Find the northernmost city' in query['natural-language'] or 
        'Find the southernmost city' in query['natural-language'] or 
        'Find the easternmost city' in query['natural-language'] or 
        'Find the westernmost city' in query['natural-language']):
        city_queries += 1
for query in ROAD_QUERIES_V2:
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

print('Number of city queries: ' + str(city_queries), flush=True)
print('Number of road queries: ' + str(road_queries), flush=True)
print('Total: ' + str(city_queries + road_queries), flush=True)