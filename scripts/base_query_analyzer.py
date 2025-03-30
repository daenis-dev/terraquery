from city_queries import CITY_QUERIES
from road_queries import ROAD_QUERIES

print('Number of city queries: ' + str(len(CITY_QUERIES)), flush=True)
print('Number of road queries: ' + str(len(ROAD_QUERIES)), flush=True)
print('Total: ' + str(len(CITY_QUERIES) + len(ROAD_QUERIES)), flush=True)