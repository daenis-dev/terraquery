# TODO: Verbiage gaps
# - owned by groups
# - owned by individuals
# - written out words - query error - fifty two thousand evaluated as fifteen thousand
# - find cities with a park
# - find cities with at least one park
# - find cities that contain at least two intersections
# - find the city with the most number of parks - query error - ST_Within(... HINT: No function matches the given name and argument type; may need explicit type casts


BASE_QUERIES = [
  # Cities (52)
  {
    "natural-language": "Find cities within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT c.name FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find cities within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT c.name FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326))"
  },
  {
    "natural-language": "Find cities within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT c.name FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
  {
    "natural-language": "Find cities within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT c.name FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326))"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred thousand",
    "sql": "SELECT * FROM cities WHERE population > 100000"
  },
  {
    "natural-language": "Find cities with more than one hundred thousand people",
    "sql": "SELECT * FROM cities WHERE population > 100000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred and fifty thousand",
    "sql": "SELECT * FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with more than one hundred and fifty thousand people",
    "sql": "SELECT * FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population greater than 200000",
    "sql": "SELECT * FROM cities WHERE population > 200000"
  },
  {
    "natural-language": "Find cities with more than 200000 people",
    "sql": "SELECT * FROM cities WHERE population > 200000"
  },
  {
    "natural-language": "Find cities with a population greater than 270,000",
    "sql": "SELECT * FROM cities WHERE population > 270000"
  },
  {
    "natural-language": "Find cities with more than 270,000 people",
    "sql": "SELECT * FROM cities WHERE population > 270000"
  },
  {
    "natural-language": "Find cities with a population of at least ten thousand",
    "sql": "SELECT * FROM cities WHERE population >= 10000"
  },
  {
    "natural-language": "Find cities with at least ten thousand people",
    "sql": "SELECT * FROM cities WHERE population >= 10000"
  },
  {
    "natural-language": "Find cities with a population of at least 76000",
    "sql": "SELECT * FROM cities WHERE population >= 76000"
  },
  {
    "natural-language": "Find cities with at least 76000 people",
    "sql": "SELECT * FROM cities WHERE population >= 76000"
  },
  {
    "natural-language": "Find cities with a population of at least forty five thousand and seven hundred",
    "sql": "SELECT * FROM cities WHERE population >= 45700"
  },
  {
    "natural-language": "Find cities with at least forty five thousand and seven hundred people",
    "sql": "SELECT * FROM cities WHERE population >= 45700"
  },
  {
    "natural-language": "Find cities with a population of at least 100,000",
    "sql": "SELECT * FROM cities WHERE population >= 100000"
  },
  {
    "natural-language": "Find cities with at least 100,000 people",
    "sql": "SELECT * FROM cities WHERE population >= 100000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred thousand",
    "sql": "SELECT * FROM cities WHERE population < 100000"
  },
  {
    "natural-language": "Find cities with less than one hundred thousand people",
    "sql": "SELECT * FROM cities WHERE population < 100000"
  },
  {
    "natural-language": "List all cities and order by population, descending",
    "sql": "SELECT * FROM cities ORDER BY population DESC"
  },
  {
    "natural-language": "List all cities and order by size, descending",
    "sql": "SELECT * FROM cities ORDER BY ST_Area(boundary) DESC"
  },
  {
    "natural-language": "Find cities that contain at least one intersection",
    "sql": "SELECT * FROM cities WHERE ST_NumGeometries(boundary) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least 5 intersections",
    "sql": "SELECT * FROM cities WHERE ST_NumGeometries(boundary) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least six intersections",
    "sql": "SELECT * FROM cities WHERE ST_NumGeometries(boundary) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least 10 intersections",
    "sql": "SELECT * FROM cities WHERE ST_NumGeometries(boundary) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least five buildings that are owned by individuals",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 5"
  },
  {
    "natural-language": "Find cities where the majority of buildings are owned by groups",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING COUNT(CASE WHEN o.is_group = TRUE THEN 1 END) > COUNT(CASE WHEN o.is_group = FALSE THEN 1 END)"
  },
  {
    "natural-language": "Find cities where the majority of buildings are owned by individuals",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING SUM(CASE WHEN o.is_group = FALSE THEN 1 ELSE 0 END) > SUM(CASE WHEN o.is_group = TRUE THEN 1 ELSE 0 END)"
  },
  {
    "natural-language": "Find the city with the most number of parks",
    "sql": "SELECT c.* FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id ORDER BY COUNT(p.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find cities with no parks",
    "sql": "SELECT * FROM cities WHERE NOT EXISTS (SELECT 1 FROM parks p WHERE ST_Within(p.boundary, cities.boundary))"
  },
  {
    "natural-language": "Find cities with at least one park",
    "sql": "SELECT c.* FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) > 0 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find the city with the most buildings",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) GROUP BY c.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest number of buildings",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) GROUP BY c.id ORDER BY COUNT(b.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the least buildings",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) GROUP BY c.id ORDER BY COUNT(b.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the least amount of roads",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most intersecting roads",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(DISTINCT r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 100000",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 100000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 100,000",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 100000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than ninety two thousand",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 92000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than forty five thousand",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 45000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than one hundred and eighty five thousand",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 185000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population of at least two hundred thousand",
    "sql": "SELECT c.* FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population >= 200000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find cities with an area greater than one square kilometer",
    "sql": "SELECT * FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 1000000"
  },
  {
    "natural-language": "Find cities with an area greater than fourty square kilometers",
    "sql": "SELECT * FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 40000000"
  },
  {
    "natural-language": "Find cities with an area greater than 40 sq km",
    "sql": "SELECT * FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 40000000"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than 70,000",
    "sql": "SELECT * FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than eighty thousand",
    "sql": "SELECT * FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than 90000",
    "sql": "SELECT * FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than 100,000",
    "sql": "SELECT * FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find all cities that contain at least 3 sq km of park",
    "sql": "SELECT c.*, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 3000"
  },
  {
    "natural-language": "Find all cities that contain at least two square kilometers of park",
    "sql": "SELECT c.*, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 2000"
  },
  {
    "natural-language": "Find all cities that contain at least one square kilometer of park",
    "sql": "SELECT c.*, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 1000"
  },
  {
    "natural-language": "Find the city where a majority of the buildings are owned by individuals",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING SUM(CASE WHEN o.is_group = FALSE THEN 1 ELSE 0 END) > SUM(CASE WHEN o.is_group = TRUE THEN 1 ELSE 0 END)"
  },
  {
    "natural-language": "Find the northernmost city",
    "sql": "SELECT name FROM cities ORDER BY ST_YMax(boundary) DESC LIMIT 1"
  },
   {
    "natural-language": "Find the southernmost city",
    "sql": "SELECT name FROM cities ORDER BY ST_YMin(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the easternmost city",
    "sql": "SELECT name FROM cities ORDER BY ST_XMax(boundary) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the westernmost city",
    "sql": "SELECT name FROM cities ORDER BY ST_XMin(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city where most buildings are owned by individuals",
    "sql": "SELECT c.* FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING SUM(CASE WHEN o.is_group = FALSE THEN 1 ELSE 0 END) > SUM(CASE WHEN o.is_group = TRUE THEN 1 ELSE 0 END)"
  },

  # Roads (58)
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads that intersect at (-119.2700, 34.2600)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_SetSRID(ST_Point(-119.2700, 34.2600), 4326))"
  },
  {
    "natural-language": "Find roads that intersect at (-119.2650, 34.2400)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_SetSRID(ST_Point(-119.2650, 34.2400), 4326))"
  },
  {
    "natural-language": "Find roads that intersect at (-119.2700, 34.2600) or (-119.2450, 34.2700)",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, ST_SetSRID(ST_Point(-119.2700, 34.2600), 4326)) OR ST_Intersects(route, ST_SetSRID(ST_Point(-119.2450, 34.2700), 4326))"
  },
  {
    "natural-language": "Find roads that span at least four kilometers through a city with a population of at least one hundred thousand",
    "sql": "SELECT r.name AS road_name, c.name AS city_name, ST_Length(ST_Transform(r.route, 3857)) / 1000 AS road_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population >= 100000 AND ST_Length(ST_Transform(r.route, 3857)) >= 4000"
  },
  {
    "natural-language": "Find roads with at least 2 km through a city with a population less than one hundred thousand",
    "sql": "SELECT r.name AS road_name, c.name AS city_name, ST_Length(ST_Transform(r.route, 3857)) / 1000 AS road_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 AND ST_Length(ST_Transform(r.route, 3857)) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least one kilometer through a city with a population of at least one hundred thousand",
    "sql": "SELECT r.name AS road_name, c.name AS city_name, ST_Length(ST_Transform(r.route, 3857)) / 1000 AS road_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population >= 100000 AND ST_Length(ST_Transform(r.route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least 1 km through a city with a population less than one hundred thousand",
    "sql": "SELECT r.name AS road_name, c.name AS city_name, ST_Length(ST_Transform(r.route, 3857)) / 1000 AS road_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 AND ST_Length(ST_Transform(r.route, 3857)) >= 5000"
  },
  {
    "natural-language": "Find roads within two kilometers of a park",
    "sql": "SELECT r.* FROM roads r JOIN parks p ON ST_DWithin(r.route, p.boundary, 2000)"
  },
  {
    "natural-language": "Find roads that go through a park",
    "sql": "SELECT r.* FROM roads r JOIN parks p ON ST_Intersects(r.route, p.boundary)"
  },
  {
    "natural-language": "Find roads that are longer than 4 km",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
  },
  {
    "natural-language": "Find roads that are at least 4 km",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
  },
  {
    "natural-language": "Find roads that are shorter than 4 km",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
  },
  {
    "natural-language": "Find roads that are longer than two kilometers",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
  },
  {
    "natural-language": "Find roads that are at least two kilometers",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
  },
  {
    "natural-language": "Find roads that are shorter than two kilometers",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
  },
  {
    "natural-language": "Find roads that are longer than five kilometers",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
  },
  {
    "natural-language": "Find roads that are at least five kilometers",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
  },
  {
    "natural-language": "Find roads that are shorter than five kilometers",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
  },
  {
    "natural-language": "Find roads that are longer than 6 km",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
  },
  {
    "natural-language": "Find roads that are at least 6 km",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
  },
  {
    "natural-language": "Find roads that are shorter than 6 km",
    "sql": "SELECT * FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
  },
  {
    "natural-language": "Find the longest road",
    "sql": "SELECT * FROM roads ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road",
    "sql": "SELECT * FROM roads ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Ventura",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ventura')) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road in Ojai",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ojai')) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Oxnard",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Oxnard')) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road in Camarillo",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Camarillo')) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within the busiest city",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MAX(population) FROM cities) ORDER BY ST_Length(r.route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road in the quietest city",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MIN(population) FROM cities) ORDER BY ST_Length(r.route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road in the busiest city",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MAX(population) FROM cities) ORDER BY ST_Length(r.route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within the quietest city",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MIN(population) FROM cities) ORDER BY ST_Length(r.route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find all roads within ten kilometers of Camarillo",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 10000) WHERE c.name = 'Camarillo'"
  },
  {
    "natural-language": "Find all roads within five kilometers of Ventura",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 5000) WHERE c.name = 'Ventura'"
  },
  {
    "natural-language": "Find roads within ten kilometers of Oxnard",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 10000) WHERE c.name = 'Oxnard'"
  },
  {
    "natural-language": "Find roads within eight kilometers of Ojai",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 8000) WHERE c.name = 'Ojai'"
  },
  {
    "natural-language": "Find roads within 10 km of Camarillo",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 10000) WHERE c.name = 'Camarillo'"
  },
  {
    "natural-language": "Find roads within 5 km of Ventura",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 5000) WHERE c.name = 'Ventura'"
  },
  {
    "natural-language": "Find all roads within 12 km of Oxnard",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 12000) WHERE c.name = 'Oxnard'"
  },
  {
    "natural-language": "Find all roads within 3 km of Ojai",
    "sql": "SELECT r.name, ST_Length(r.route) AS road_length FROM roads r JOIN cities c ON ST_DWithin(r.route, c.boundary, 3000) WHERE c.name = 'Ojai'"
  },
  {
    "natural-language": "List all roads in Ojai",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ojai'))"
  },
  {
    "natural-language": "List all roads in Camarillo",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Camarillo'))"
  },
  {
    "natural-language": "List roads in Oxnard",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Oxnard'))"
  },
  {
    "natural-language": "List roads in Ventura",
    "sql": "SELECT * FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ventura'))"
  },
  {
    "natural-language": "List all roads that have multiple buildings that are owned by the same group",
    "sql": "SELECT r.* FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY r.id HAVING COUNT(DISTINCT b.id) > 1"
  },
  {
    "natural-language": "List all roads that have buildings that are not owned by groups",
    "sql": "SELECT r.* FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE"
  },
  {
    "natural-language": "Find the road with the most buildings",
    "sql": "SELECT r.* FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) GROUP BY r.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the road with the least buildings",
    "sql": "SELECT r.* FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) GROUP BY r.id ORDER BY COUNT(b.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the road with the most individual owners",
    "sql": "SELECT r.* FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY r.id ORDER BY COUNT(DISTINCT b.owning_entity_id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the road with the least individual owners",
    "sql": "SELECT r.* FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY r.id ORDER BY COUNT(DISTINCT b.owning_entity_id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find roads with no buildings",
    "sql": "SELECT * FROM roads WHERE NOT EXISTS (SELECT 1 FROM buildings b WHERE ST_Intersects(b.location, roads.route))"
  },
  {
    "natural-language": "Find the easternmost road",
    "sql": "SELECT * FROM roads ORDER BY ST_X(ST_Transform(ST_StartPoint(route), 4326)) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the westernmost road",
    "sql": "SELECT * FROM roads ORDER BY ST_X(ST_Transform(ST_StartPoint(route), 4326)) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the southernmost road",
    "sql": "SELECT * FROM roads ORDER BY ST_Y(ST_Transform(ST_StartPoint(route), 4326)) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the norhternmost road",
    "sql": "SELECT * FROM roads ORDER BY ST_Y(ST_Transform(ST_StartPoint(route), 4326)) DESC LIMIT 1"
  },

  # Parks (58)
  {
    "natural-language": "Find parks within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT * FROM parks p WHERE ST_Within(p.boundary, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find parks within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT * FROM parks p WHERE ST_Within(p.boundary, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
  {
    "natural-language": "Find parks with an area less than ten square kilometers",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 10000000"
  },
  {
    "natural-language": "Find parks with an area of at least ten square kilometers",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 10000000"
  },
  {
    "natural-language": "Find parks with an area greater than ten square kilometers",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 10000000"
  },
  {
    "natural-language": "Find parks with an area less than nine square kilometers",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 9000000"
  },
  {
    "natural-language": "Find parks with an area of at least nine square kilometers",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 9000000"
  },
  {
    "natural-language": "Find parks with an area greater than nine square kilometers",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 9000000"
  },
  {
    "natural-language": "Find parks with an area less than 8 sq km",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 8000000"
  },
  {
    "natural-language": "Find parks with an area of at least 8 sq km",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 8000000"
  },
  {
    "natural-language": "Find parks with an area greater than 8 sq km",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 8000000"
  },
  {
    "natural-language": "Find parks with an area less than 7 sq km",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 7000000"
  },
  {
    "natural-language": "Find parks with an area of at least 7 sq km",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 7000000"
  },
  {
    "natural-language": "Find parks with an area greater than 7 sq km",
    "sql": "SELECT * FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 7000000"
  },
  {
    "natural-language": "Find parks containing a road that is at least 2 km",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) >= 2000"
  },
  {
    "natural-language": "Find parks containing a road that is at least 5 km",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) >= 5000"
  },
  {
    "natural-language": "Find parks containing a road that is less than 4 km",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) < 4000"
  },
  {
    "natural-language": "Find parks containing a road that is at least nineteen kilometers",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) >= 19000"
  },
  {
    "natural-language": "Find parks containing a road that is less than three hundred kilometers",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) < 300000"
  },
  {
    "natural-language": "Find parks containing a road that is shorter than five kilometers",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) < 5000"
  },
  {
    "natural-language": "Find parks containing a road that is greater than six kilometers",
    "sql": "SELECT p.* FROM parks p JOIN roads r ON ST_Intersects(p.boundary, r.route) WHERE ST_Length(ST_Transform(r.route, 3857)) > 6000"
  },
  {
    "natural-language": "Find all parks within 10 km of Oxnard",
    "sql": "SELECT * FROM parks p WHERE ST_DWithin(ST_Transform(p.boundary, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Oxnard' LIMIT 1), 10000)"
  },
  {
    "natural-language": "Find parks within fifteen kilometers of Ojai",
    "sql": "SELECT * FROM parks p WHERE ST_DWithin(ST_Transform(p.boundary, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Ojai' LIMIT 1), 15000)"
  },
  {
    "natural-language": "Find all parks within 8 km of Camarillo",
    "sql": "SELECT * FROM parks p WHERE ST_DWithin(ST_Transform(p.boundary, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Camarillo' LIMIT 1), 8000)"
  },
  {
    "natural-language": "Find parks within 6 km of Ventura",
    "sql": "SELECT * FROM parks p WHERE ST_DWithin(ST_Transform(p.boundary, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Ventura' LIMIT 1), 6000)"
  },
  {
    "natural-language": "Find parks in Ventura",
    "sql": "SELECT * FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Ventura' LIMIT 1))"
  },
  {
    "natural-language": "Find all parks in Ojai",
    "sql": "SELECT * FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Ojai' LIMIT 1))"
  },
  {
    "natural-language": "Find parks in Oxnard",
    "sql": "SELECT * FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Oxnard' LIMIT 1))"
  },
  {
    "natural-language": "Find all parks in Camarillo",
    "sql": "SELECT * FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Camarillo' LIMIT 1))"
  },
  {
    "natural-language": "Find parks within a city that has a population of less than two hundred thousand",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population < 200000"
  },
  {
    "natural-language": "Find parks within a city that has a population of less than 300,000",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population < 300000"
  },
  {
    "natural-language": "Find parks within a city that has a population of at least one hundred thousand",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population >= 100000"
  },
  {
    "natural-language": "Find parks within a city that has a population of at least 50,000",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population >= 50000"
  },
  {
    "natural-language": "Find parks within a city that has a population greater than ninety thousand",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population > 90000"
  },
  {
    "natural-language": "Find parks within a city that has a population greater than 115,000",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population > 115000"
  },
  {
    "natural-language": "Find parks in a city with a population that is greater than 200,000",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population > 200000"
  },
  {
    "natural-language": "Find parks within the city that has the highest population",
    "sql": "SELECT p.* FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population = (SELECT MAX(population) FROM cities)"
  },
  {
    "natural-language": "Find the largest park",
    "sql": "SELECT * FROM parks ORDER BY ST_Area(ST_Transform(boundary, 3857)) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the smallest park",
    "sql": "SELECT * FROM parks ORDER BY ST_Area(ST_Transform(boundary, 3857)) ASC LIMIT 1"
  },
  {
    "natural-language": "Find parks that are within one kilometer of a building that is owned by a group who owns multiple buildings",
    "sql": "SELECT DISTINCT ON (p.name) p.name, b.street_number, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857)) AS distance_in_meters FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 1000) JOIN owning_entities oe ON b.owning_entity_id = oe.id WHERE oe.is_group = TRUE ORDER BY p.name, distance_in_meters"
  },
  {
    "natural-language": "Find parks that are within two kilometers of a building that is owned by a group who owns multiple buildings",
    "sql": "SELECT DISTINCT ON (p.name) p.name, b.street_number, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857)) AS distance_in_meters FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 2000) JOIN owning_entities oe ON b.owning_entity_id = oe.id WHERE oe.is_group = TRUE ORDER BY p.name, distance_in_meters"
  },
  {
    "natural-language": "Find parks that are within 3 km of a building that is owned by a group who owns multiple buildings",
    "sql": "SELECT DISTINCT ON (p.name) p.name, b.street_number, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857)) AS distance_in_meters FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 3000) JOIN owning_entities oe ON b.owning_entity_id = oe.id WHERE oe.is_group = TRUE ORDER BY p.name, distance_in_meters"
  },
  {
    "natural-language": "Find parks with no roads running through them",
    "sql": "SELECT * FROM parks p WHERE NOT EXISTS (SELECT 1 FROM roads r WHERE ST_Intersects(p.boundary, r.route))"
  },
  {
    "natural-language": "Find all parks with at least one road running through them",
    "sql": "SELECT * FROM parks p WHERE EXISTS (SELECT 1 FROM roads r WHERE ST_Intersects(p.boundary, r.route))"
  },
  {
    "natural-language": "Find the westernmost park",
    "sql": "SELECT * FROM parks ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), i)) LIMIT 1))) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the easternmost park",
    "sql": "SELECT * FROM parks ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), i)) DESC LIMIT 1))) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the northernmost park",
    "sql": "SELECT * FROM parks ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), i)) DESC LIMIT 1))) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the southernmost park",
    "sql": "SELECT * FROM parks ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), i)) LIMIT 1))) ASC LIMIT 1"
  },
  {
    "natural-language": "Find parks north of Ventura",
    "sql": "SELECT * FROM parks p WHERE ST_Y(ST_Centroid(p.boundary)) > (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ventura' LIMIT 1)"
  },
  {
    "natural-language": "Find parks south of Ojai",
    "sql": "SELECT * FROM parks p WHERE ST_Y(ST_Centroid(p.boundary)) < (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ojai' LIMIT 1)"
  },
  {
    "natural-language": "Find parks south of Ventura",
    "sql": "SELECT * FROM parks p WHERE ST_Y(ST_Centroid(p.boundary)) < (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ventura' LIMIT 1)"
  },
  {
    "natural-language": "Find parks within one kilometer of a building",
    "sql": "SELECT DISTINCT p.* FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 1000)"
  },
  {
    "natural-language": "Find parks within 2 km of a building",
    "sql": "SELECT DISTINCT p.* FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 2000)"
  },
  {
    "natural-language": "Find parks within three kilometers of a building",
    "sql": "SELECT DISTINCT p.* FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 3000)"
  },
  {
    "natural-language": "Find parks within 4 km of a building",
    "sql": "SELECT DISTINCT p.* FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 4000)"
  },
  {
    "natural-language": "Find parks that are at least one kilometer from the nearest building",
    "sql": "SELECT p.* FROM parks p WHERE NOT EXISTS (SELECT 1 FROM buildings b WHERE ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 1000))"
  },
  {
    "natural-language": "Find the park with the most buildings within two kilometers",
    "sql": "SELECT p.*, COUNT(b.id) AS building_count FROM parks p JOIN buildings b ON ST_DWithin(p.boundary, b.location, 2000) GROUP BY p.id ORDER BY building_count DESC LIMIT 1"
  },
  {
    "natural-language": "Find parks that are not in Ojai",
    "sql": "SELECT * FROM parks p WHERE NOT ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Ojai' LIMIT 1))"
  },

  # Buildings (51)
  {
    "natural-language": "Find buildings within 10 km of Ventura",
    "sql": "SELECT * FROM buildings WHERE ST_DWithin(ST_Transform(location, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Ventura'), 10000)"
  },
  {
    "natural-language": "Find buildings within 10 km of Ojai",
    "sql": "SELECT * FROM buildings WHERE ST_DWithin(ST_Transform(location, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Ojai'), 10000)"
  },
  {
    "natural-language": "Find buildings within 10 km of Camarillo",
    "sql": "SELECT * FROM buildings WHERE ST_DWithin(ST_Transform(location, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Camarillo'), 10000)"
  },
  {
    "natural-language": "Find buildings within 10 km of Oxnard",
    "sql": "SELECT * FROM buildings WHERE ST_DWithin(ST_Transform(location, 3857), (SELECT ST_Transform(boundary, 3857) FROM cities WHERE name = 'Oxnard'), 10000)"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT * FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT * FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326))"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT * FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT * FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326))"
  },
  {
    "natural-language": "Find buildings in Ojai",
    "sql": "SELECT * FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ojai'))"
  },
  {
    "natural-language": "Find buildings in Ventura",
    "sql": "SELECT * FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ventura'))"
  },
  {
    "natural-language": "Find all buildings in Camarillo",
    "sql": "SELECT * FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Camarillo'))"
  },
  {
    "natural-language": "Find all buildings in Oxnard",
    "sql": "SELECT * FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Oxnard'))"
  },
  {
    "natural-language": "Find buildings within half of a kilometer of a park",
    "sql": "SELECT b.* FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 500)"
  },
  {
    "natural-language": "Find buildings within 1 km of a park",
    "sql": "SELECT b.* FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 1000)"
  },
  {
    "natural-language": "Find buildings within 2 km of a park",
    "sql": "SELECT b.* FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 2000)"
  },
  {
    "natural-language": "Find buildings within three kilometers of a park",
    "sql": "SELECT b.* FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 3000)"
  },
  {
    "natural-language": "Find buildings within the most populated town",
    "sql": "SELECT * FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities ORDER BY population DESC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings within the least populated town",
    "sql": "SELECT * FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities ORDER BY population ASC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings that are owned by a group",
    "sql": "SELECT * FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = TRUE)"
  },
  {
    "natural-language": "Find buildings that are owned by an individual",
    "sql": "SELECT * FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = FALSE)"
  },
  {
    "natural-language": "Find buildings that are owned by a group within one kilometer of Oxnard",
    "sql": "SELECT b.id, b.street_number, b.location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 1000) AND oe.is_group = TRUE"
  },
  {
    "natural-language": "Find buildings that are owned by individuals within one kilometer of Oxnard",
    "sql": "SELECT b.id, b.street_number, b.location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 1000) AND oe.is_group = FALSE"
  },
  {
    "natural-language": "Find buildings that are owned by a group within two kilometers of Ventura",
    "sql": "SELECT b.id, b.street_number, b.location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 2000) AND oe.is_group = TRUE"
  },
  {
    "natural-language": "Find buildings that are owned by individuals within 2 km of Ventura",
    "sql": "SELECT b.id, b.street_number, b.location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 2000) AND oe.is_group = FALSE"
  },
  {
    "natural-language": "Find buildings that are owned by a group within three kilometers of Ojai",
    "sql": "SELECT b.id, b.street_number, b.location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 3000) AND oe.is_group = TRUE"
  },
  {
    "natural-language": "Find buildings that are owned by individuals within 3 km of Ojai",
    "sql": "SELECT b.id, b.street_number, b.location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 3000) AND oe.is_group = FALSE"
  },
  {
    "natural-language": "Find buildings with a street number in the one hundreds",
    "sql": "SELECT * FROM buildings WHERE street_number LIKE '1%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings with a street number in the two hundreds",
    "sql": "SELECT * FROM buildings WHERE street_number LIKE '2%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings with a street number in the 300s",
    "sql": "SELECT * FROM buildings WHERE street_number LIKE '3%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings with a street number in the 400s",
    "sql": "SELECT * FROM buildings WHERE street_number LIKE '4%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings on the longest road",
    "sql": "SELECT * FROM buildings WHERE road_id = (SELECT id FROM roads ORDER BY ST_Length(route) DESC LIMIT 1)"
  },
  {
    "natural-language": "Find buildings within two kilometers of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(r1.route, r2.route)), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, b.location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 2000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings within three kilometers of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(r1.route, r2.route)), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, b.location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 3000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings within 4 km of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(r1.route, r2.route)), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, b.location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 4000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings on Seaward Ave",
    "sql": "SELECT * FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Seaward Ave')"
  },
  {
    "natural-language": "Find buildings off of Ojai Ave",
    "sql": "SELECT * FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Ojai Ave')"
  },
  {
    "natural-language": "Find buildings on Maricopa Hwy",
    "sql": "SELECT * FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Maricopa Hwy')"
  },
  {
    "natural-language": "Find buildings off of Grand Ave",
    "sql": "SELECT * FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Grand Ave')"
  },
  {
    "natural-language": "Find buildings in the most populated city that are owned by groups",
    "sql": "SELECT * FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = TRUE) AND ST_Within(location, (SELECT boundary FROM cities ORDER BY population DESC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings in the most populated city that are owned by individuals",
    "sql": "SELECT * FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = FALSE) AND ST_Within(location, (SELECT boundary FROM cities ORDER BY population DESC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings on any road that spans multiple cities",
    "sql": "SELECT * FROM buildings WHERE road_id IN (SELECT r.id FROM roads r JOIN cities c1 ON ST_Intersects(r.route, c1.boundary) JOIN cities c2 ON ST_Intersects(r.route, c2.boundary) WHERE c1.id != c2.id)"
  },
  {
    "natural-language": "Find buildings on any road that spans a single city",
    "sql": "SELECT * FROM buildings WHERE road_id IN (SELECT r.id FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) GROUP BY r.id HAVING COUNT(DISTINCT c.id) = 1)"
  },
  {
    "natural-language": "Find buildings within one kilometer of three or more roads",
    "sql": "SELECT b.* FROM buildings b JOIN roads r ON ST_DWithin(b.location, r.route, 1000) GROUP BY b.id HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find the westernmost building in Ventura",
    "sql": "SELECT * FROM buildings WHERE ST_X(location) = (SELECT MIN(ST_X(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ventura')))"
  },
  {
    "natural-language": "Find the easternmost building in Camarillo",
    "sql": "SELECT * FROM buildings WHERE ST_X(location) = (SELECT MAX(ST_X(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Camarillo')))"
  },
  {
    "natural-language": "Find the northernmost building in Ojai",
    "sql": "SELECT * FROM buildings WHERE ST_Y(location) = (SELECT MAX(ST_Y(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ojai')))"
  },
  {
    "natural-language": "Find the southernmost building in Oxnard",
    "sql": "SELECT * FROM buildings WHERE ST_Y(location) = (SELECT MIN(ST_Y(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Oxnard')))"
  },
  {
    "natural-language": "Find buildings in the southern half of Ojai",
    "sql": "SELECT * FROM buildings WHERE ST_Y(location) < (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ojai') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ojai'))"
  },
  {
    "natural-language": "Find buildings in the northern half of Camarillo",
    "sql": "SELECT * FROM buildings WHERE ST_Y(location) > (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Camarillo') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Camarillo'))"
  },
  {
    "natural-language": "Find buildings in the eastern half of Ventura",
    "sql": "SELECT * FROM buildings WHERE ST_X(location) > (SELECT ST_X(ST_Centroid(boundary)) FROM cities WHERE name = 'Ventura') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ventura'))"
  },
  {
    "natural-language": "Find buildings in the western half of Oxnard",
    "sql": "SELECT * FROM buildings WHERE ST_X(location) < (SELECT ST_X(ST_Centroid(boundary)) FROM cities WHERE name = 'Oxnard') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Oxnard'))"
  },

  # Owners (50)
  {
    "natural-language": "Find owners with buildings within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find owners with buildings within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326))"
  },
  {
    "natural-language": "Find owners with buildings within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
  {
    "natural-language": "Find owners with buildings within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326))"
  },
  {
    "natural-language": "Find owners with buildings in Oxnard",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Oxnard'"
  },
  {
    "natural-language": "Find groups that own buildings in Ventura",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Ventura' AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find individual owners with buildings in Ojai",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Ojai' AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find groups that own buildings in Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Camarillo' AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find owners that have buildings in more than one city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) GROUP BY o.id HAVING COUNT(DISTINCT c.id) > 1"
  },
  {
    "natural-language": "Find owners that have buildings in a single city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) GROUP BY o.id HAVING COUNT(DISTINCT c.id) = 1"
  },
  {
    "natural-language": "Find groups that own more than one building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) > 1 AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find owners that own more than three buildings",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) > 3"
  },
  {
    "natural-language": "Find owners that own exactly one building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) = 1"
  },
  {
    "natural-language": "Find owners that own at least one building off of Main St",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Main St'"
  },
  {
    "natural-language": "Find owners that own at least one building on Rose Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Rose Ave'"
  },
  {
    "natural-language": "Find owners that own at least two buildings on Rose Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Rose Ave' GROUP BY o.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find owners that own at least 3 buildings on Rose Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Rose Ave' GROUP BY o.id HAVING COUNT(b.id) >= 3"
  },
  {
    "natural-language": "Find owners that own at least 4 buildings on Rose Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Rose Ave' GROUP BY o.id HAVING COUNT(b.id) >= 4"
  },
  {
    "natural-language": "Find owners that own at least two buildings on Victoria Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Victoria Ave' GROUP BY o.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find owners that own at least 2 buildings on Telephone Rd",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Telephone Rd' GROUP BY o.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find owners that own at least two buildings on Thompson Blvd",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Thompson Blvd' GROUP BY o.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find owners that own at least 2 buildings on Ventura Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Ventura Ave' GROUP BY o.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find the owner with the most buildings within ten kilometers of Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Camarillo' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 10000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within eighty five kilometers of Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Camarillo' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 85000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within 2 km of Oxnard",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Oxnard' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 2000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within sixty five kilometers of Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Camarillo' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 65000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within 2km of Ventura",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Ventura' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 2000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the group with the most buildings off of Vineyard Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Vineyard Ave' AND o.is_group = TRUE GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find individual owners with one or more buildings in Ventura",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.name = 'Ventura' AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find the owner with the most buildings in the most populated city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.id = (SELECT id FROM cities ORDER BY population DESC LIMIT 1) GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings in the least populated city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) WHERE c.id = (SELECT id FROM cities ORDER BY population ASC LIMIT 1) GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find individual owners that own a single building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) = 1 AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find the group that owns the most buildings",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) = (SELECT MAX(building_count) FROM (SELECT COUNT(b.id) AS building_count FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id) AS subquery) AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find all groups that own more than one building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) > 1 AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find the individual that owns the most buildings",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) = (SELECT MAX(building_count) FROM (SELECT COUNT(b.id) AS building_count FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id) AS subquery) AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find all owners that have a single building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) = 1"
  },
  {
    "natural-language": "Find all individuals that own more than one building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) > 1 AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find owners that have more than one building on the same road",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id, b.road_id HAVING COUNT(b.id) > 1"
  },
  {
    "natural-language": "Find owners that have more than two buildings on the same road",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id, b.road_id HAVING COUNT(b.id) > 2"
  },
  {
    "natural-language": "Find owners that have buildings on two or more roads",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(DISTINCT b.road_id) >= 2"
  },
  {
    "natural-language": "Find owners that have buildings on Seaward Ave",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN roads r ON b.road_id = r.id WHERE r.name = 'Seaward Ave' GROUP BY o.id"
  },
  {
    "natural-language": "Find owners that have more than three buildings on the same road",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id, b.road_id HAVING COUNT(b.id) > 3"
  },
  {
    "natural-language": "Find owners with two or more buildings across two or more cities",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(b.location, c.boundary) GROUP BY o.id HAVING COUNT(DISTINCT c.id) > 1 AND COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find groups that own more than 3 buildings",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id GROUP BY o.id HAVING COUNT(b.id) > 3 AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find the owner of the northernmost building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id ORDER BY ST_Y(b.location) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner of the easternmost building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id ORDER BY ST_X(b.location) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner of the southernmost building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id ORDER BY ST_Y(b.location) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the owner of the westernmost building",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id ORDER BY ST_X(b.location) ASC LIMIT 1"
  },
  {
    "natural-language": "Find owners of buildings within one kilometer of a park",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN parks p ON ST_DWithin(b.location, p.boundary, 1000)"
  },
  {
    "natural-language": "Find owners of buildings within two kilometers of a park",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN parks p ON ST_DWithin(b.location, p.boundary, 2000)"
  },
  {
    "natural-language": "Find all cities",
    "sql": "SELECT * FROM cities"
  },
  {
    "natural-language": "Find all roads",
    "sql": "SELECT * FROM roads"
  },
  {
    "natural-language": "Find parks",
    "sql": "SELECT * FROM parks"
  },
  {
    "natural-language": "Find all owners",
    "sql": "SELECT * FROM owning_entities"
  },
  {
    "natural-language": "Find buildings",
    "sql": "SELECT * FROM buildings"
  }
]