BASE_QUERIES = [
  # Parks
  {
    "natural-language": "Find parks with an area less than ten square kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 10000000"
  },
  {
    "natural-language": "Find parks with an area of at least ten square kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 10000000"
  },
  {
    "natural-language": "Find parks with an area greater than ten square kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 10000000"
  },
  {
    "natural-language": "Find parks with an area less than nine square kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 9000000"
  },
  {
    "natural-language": "Find parks with an area of at least nine square kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 9000000"
  },
  {
    "natural-language": "Find parks with an area greater than nine square kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 9000000"
  },
  {
    "natural-language": "Find parks with an area less than 8 sq km",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 8000000"
  },
  {
    "natural-language": "Find parks with an area of at least 8 sq km",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 8000000"
  },
  {
    "natural-language": "Find parks with an area greater than 8 sq km",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 8000000"
  },
  {
    "natural-language": "Find parks with an area less than 7 sq km",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) < 7000000"
  },
  {
    "natural-language": "Find parks with an area of at least 7 sq km",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) >= 7000000"
  },
  {
    "natural-language": "Find parks with an area greater than 7 sq km",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks WHERE ST_Area(ST_Transform(boundary, 3857)) > 7000000"
  },
  {
    "natural-language": "Find parks containing a road that is at least 2 km",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) >= 2000"
  },
  {
    "natural-language": "Find parks containing a road that is at least 5 km",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) >= 5000"
  },
  {
    "natural-language": "Find parks containing a road that is less than 4 km",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) < 4000"
  },
  {
    "natural-language": "Find parks containing a road that is at least nineteen kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) >= 19000"
  },
  {
    "natural-language": "Find parks containing a road that is less than three hundred kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) < 300000"
  },
  {
    "natural-language": "Find parks containing a road that is shorter than five kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) < 5000"
  },
  {
    "natural-language": "Find parks containing a road that is greater than six kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)) WHERE ST_Length(r.route::geography) >= 6000"
  },
  {
    "natural-language": "Find all parks within 10 km of Oxnard",
    "sql": "SELECT p.id, p.name FROM parks p JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(p.boundary::geography, c.boundary::geography, 10000)"
  },
  {
    "natural-language": "Find parks within fifteen kilometers of Ojai",
    "sql": "SELECT p.id, p.name FROM parks p JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(p.boundary::geography, c.boundary::geography, 15000)"
  },
  {
    "natural-language": "Find all parks within 8 km of Camarillo",
    "sql": "SELECT p.id, p.name FROM parks p JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(p.boundary::geography, c.boundary::geography, 8000)"
  },
  {
    "natural-language": "Find parks within 6 km of Ventura",
    "sql": "SELECT p.id, p.name FROM parks p JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(p.boundary::geography, c.boundary::geography, 000)"
  },
  {
    "natural-language": "Find parks in Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(ST_Transform(p.boundary, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura' LIMIT 1), 4326))"
  },
  {
    "natural-language": "Find all parks in Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(ST_Transform(p.boundary, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ojai' LIMIT 1), 4326))"
  },
  {
    "natural-language": "Find parks in Oxnard",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(ST_Transform(p.boundary, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Oxnard' LIMIT 1), 4326))"
  },
  {
    "natural-language": "Find all parks in Camarillo",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(ST_Transform(p.boundary, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Camarillo' LIMIT 1), 4326))"
  },
  {
    "natural-language": "Find parks within a city that has a population of less than two hundred thousand",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 200000"
  },
  {
    "natural-language": "Find parks within a city that has a population of less than 300,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 300000"
  },
  {
    "natural-language": "Find parks within a city that has a population of at least one hundred thousand",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000"
  },
  {
    "natural-language": "Find parks within a city that has a population of at least 50,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 50000"
  },
  {
    "natural-language": "Find parks within a city that has a population greater than ninety thousand",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 90000"
  },
  {
    "natural-language": "Find parks within a city that has a population greater than 115,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 115000"
  },
  {
    "natural-language": "Find parks in a city with a population that is greater than 200,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 200000"
  },
  {
    "natural-language": "Find parks within the city that has the highest population",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(ST_Transform(p.boundary, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population = (SELECT MAX(population) FROM cities)"
  },
  {
    "natural-language": "Find the largest park",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks ORDER BY ST_Area(ST_Transform(boundary, 3857)) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the smallest park",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks ORDER BY ST_Area(ST_Transform(boundary, 3857)) ASC LIMIT 1"
  },
  {
    "natural-language": "Find parks that are within one kilometer of a building that is owned by a group who owns multiple buildings",
    "sql": "SELECT DISTINCT ON (p.name) p.name, ST_AsGeoJSON(p.boundary) AS boundary, b.street_number, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857)) AS distance_in_meters FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 1000) JOIN owning_entities oe ON b.owning_entity_id = oe.id WHERE oe.is_group = TRUE ORDER BY p.name, distance_in_meters"
  },
  {
    "natural-language": "Find parks that are within two kilometers of a building that is owned by a group who owns multiple buildings",
    "sql": "SELECT DISTINCT ON (p.name) p.name, ST_AsGeoJSON(p.boundary) AS boundary, b.street_number, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857)) AS distance_in_meters FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 2000) JOIN owning_entities oe ON b.owning_entity_id = oe.id WHERE oe.is_group = TRUE ORDER BY p.name, distance_in_meters"
  },
  {
    "natural-language": "Find parks that are within 3 km of a building that is owned by a group who owns multiple buildings",
    "sql": "SELECT DISTINCT ON (p.name) p.name, ST_AsGeoJSON(p.boundary) AS boundary, b.street_number, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857)) AS distance_in_meters FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 3000) JOIN owning_entities oe ON b.owning_entity_id = oe.id WHERE oe.is_group = TRUE ORDER BY p.name, distance_in_meters"
  },
  {
    "natural-language": "Find parks with no roads running through them",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE NOT EXISTS (SELECT 1 FROM roads r WHERE ST_Intersects(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)))"
  },
  {
    "natural-language": "Find all parks with at least one road running through them",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE EXISTS (SELECT 1 FROM roads r WHERE ST_Intersects(ST_Transform(p.boundary, 4326), ST_Transform(r.route, 4326)))"
  },
  {
    "natural-language": "Find the westernmost park",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), i)) LIMIT 1))) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the easternmost park",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_X(ST_PointN(ST_ExteriorRing(boundary), i)) DESC LIMIT 1))) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the northernmost park",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), i)) DESC LIMIT 1))) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the southernmost park",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), (SELECT i FROM generate_series(1, ST_NumPoints(ST_ExteriorRing(boundary))) AS i ORDER BY ST_Y(ST_PointN(ST_ExteriorRing(boundary), i)) LIMIT 1))) ASC LIMIT 1"
  },
  {
    "natural-language": "Find parks north of Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Y(ST_Centroid(p.boundary)) > (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ventura' LIMIT 1)"
  },
  {
    "natural-language": "Find parks south of Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Y(ST_Centroid(p.boundary)) < (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ojai' LIMIT 1)"
  },
  {
    "natural-language": "Find parks south of Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Y(ST_Centroid(p.boundary)) < (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ventura' LIMIT 1)"
  },
  {
    "natural-language": "Find parks within one kilometer of a building",
    "sql": "SELECT DISTINCT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 1000)"
  },
  {
    "natural-language": "Find parks within 2 km of a building",
    "sql": "SELECT DISTINCT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 2000)"
  },
  {
    "natural-language": "Find parks within three kilometers of a building",
    "sql": "SELECT DISTINCT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 3000)"
  },
  {
    "natural-language": "Find parks within 4 km of a building",
    "sql": "SELECT DISTINCT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN buildings b ON ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 4000)"
  },
  {
    "natural-language": "Find parks that are at least one kilometer from the nearest building",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p WHERE NOT EXISTS (SELECT 1 FROM buildings b WHERE ST_DWithin(ST_Transform(p.boundary, 3857), ST_Transform(b.location, 3857), 1000))"
  },
  {
    "natural-language": "Find the park with the most buildings within two kilometers",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary, COUNT(b.id) AS building_count FROM parks p JOIN buildings b ON ST_DWithin(p.boundary, b.location, 2000) GROUP BY p.id ORDER BY building_count DESC LIMIT 1"
  },
  {
    "natural-language": "Find parks that are not in Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE NOT ST_Within(ST_Transform(p.boundary, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ojai' LIMIT 1), 4326))"
  },

  {
    "natural-language": "Find buildings within 10 km of Ventura",
    "sql": "SELECT b.id, b.street_number, b.location FROM buildings b JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(b.location::geography, c.boundary::geography, 10000)"
  },
  {
    "natural-language": "Find buildings within 10 km of Ojai",
    "sql": "SELECT b.id, b.street_number, b.location FROM buildings b JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(b.location::geography, c.boundary::geography, 10000)"
  },
  {
    "natural-language": "Find buildings within 10 km of Camarillo",
    "sql": "SELECT b.id, b.street_number, b.location FROM buildings b JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(b.location::geography, c.boundary::geography, 10000)"
  },
  {
    "natural-language": "Find buildings within 10 km of Oxnard",
    "sql": "SELECT b.id, b.street_number, b.location FROM buildings b JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(b.location::geography, c.boundary::geography, 10000)"
  },
  {
    "natural-language": "Find buildings in Ojai",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ojai'))"
  },
  {
    "natural-language": "Find buildings in Ventura",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ventura'))"
  },
  {
    "natural-language": "Find all buildings in Camarillo",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Camarillo'))"
  },
  {
    "natural-language": "Find all buildings in Oxnard",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Oxnard'))"
  },
  {
    "natural-language": "Find buildings within half of a kilometer of a park",
    "sql": "SELECT b.street_number, ST_AsGeoJSON(b.location) AS location FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 500)"
  },
  {
    "natural-language": "Find buildings within 1 km of a park",
    "sql": "SELECT b.street_number, ST_AsGeoJSON(b.location) AS location FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 1000)"
  },
  {
    "natural-language": "Find buildings within 2 km of a park",
    "sql": "SELECT b.street_number, ST_AsGeoJSON(b.location) AS location FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 2000)"
  },
  {
    "natural-language": "Find buildings within three kilometers of a park",
    "sql": "SELECT b.street_number, ST_AsGeoJSON(b.location) AS location FROM buildings b JOIN parks p ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(p.boundary, 3857), 3000)"
  },
  {
    "natural-language": "Find buildings within the most populated town",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities ORDER BY population DESC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings within the least populated town",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities ORDER BY population ASC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings that are owned by a group",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = TRUE)"
  },
  {
    "natural-language": "Find buildings that are owned by an individual",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = FALSE)"
  },
  {
    "natural-language": "Find buildings that are owned by a group within one kilometer of Oxnard",
    "sql": "SELECT b.id, b.street_number, ST_AsGeoJSON(b.location) AS location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 1000) AND oe.is_group = TRUE"
  },
  {
    "natural-language": "Find buildings that are owned by individuals within one kilometer of Oxnard",
    "sql": "SELECT b.id,b.street_number, ST_AsGeoJSON(b.location) AS location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 1000) AND oe.is_group = FALSE"
  },
  {
    "natural-language": "Find buildings that are owned by a group within two kilometers of Ventura",
    "sql": "SELECT b.id, b.street_number, ST_AsGeoJSON(b.location) AS location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 2000) AND oe.is_group = TRUE"
  },
  {
    "natural-language": "Find buildings that are owned by individuals within 2 km of Ventura",
    "sql": "SELECT b.id, b.street_number, ST_AsGeoJSON(b.location) AS location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 2000) AND oe.is_group = FALSE"
  },
  {
    "natural-language": "Find buildings that are owned by a group within three kilometers of Ojai",
    "sql": "SELECT b.id, b.street_number, ST_AsGeoJSON(b.location) AS location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 3000) AND oe.is_group = TRUE"
  },
  {
    "natural-language": "Find buildings that are owned by individuals within 3 km of Ojai",
    "sql": "SELECT b.id, b.street_number, ST_AsGeoJSON(b.location) AS location, oe.name AS owner_name FROM buildings b JOIN owning_entities oe ON b.owning_entity_id = oe.id JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(c.boundary::geography, b.location::geography, 3000) AND oe.is_group = FALSE"
  },
  {
    "natural-language": "Find buildings with a street number in the one hundreds",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE street_number LIKE '1%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings with a street number in the two hundreds",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE street_number LIKE '2%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings with a street number in the 300s",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE street_number LIKE '3%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings with a street number in the 400s",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE street_number LIKE '4%' AND LENGTH(street_number) = 3"
  },
  {
    "natural-language": "Find buildings on the longest road",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id = (SELECT id FROM roads ORDER BY ST_Length(route) DESC LIMIT 1)"
  },
  {
    "natural-language": "Find buildings within two kilometers of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(ST_Transform(r1.route, 4326), ST_Transform(r2.route, 4326))), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, ST_AsGeoJSON(b.location) AS location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 2000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings within three kilometers of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(ST_Transform(r1.route, 4326), ST_Transform(r2.route, 4326))), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, ST_AsGeoJSON(b.location) AS location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 3000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings within 4 km of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(ST_Transform(r1.route, 4326), ST_Transform(r2.route, 4326))), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, ST_AsGeoJSON(b.location) AS location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 4000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings on Seaward Ave",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Seaward Ave')"
  },
  {
    "natural-language": "Find buildings off of Ojai Ave",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Ojai Ave')"
  },
  {
    "natural-language": "Find buildings on Maricopa Hwy",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Maricopa Hwy')"
  },
  {
    "natural-language": "Find buildings off of Grand Ave",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id = (SELECT id FROM roads WHERE name = 'Grand Ave')"
  },
  {
    "natural-language": "Find buildings in the most populated city that are owned by groups",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = TRUE) AND ST_Within(location, (SELECT boundary FROM cities ORDER BY population DESC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings in the most populated city that are owned by individuals",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE owning_entity_id IN (SELECT id FROM owning_entities WHERE is_group = FALSE) AND ST_Within(location, (SELECT boundary FROM cities ORDER BY population DESC LIMIT 1))"
  },
  {
    "natural-language": "Find buildings on any road that spans multiple cities",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id IN (SELECT r.id FROM roads r JOIN cities c1 ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c1.boundary, 4326)) JOIN cities c2 ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c2.boundary, 4326)) WHERE c1.id != c2.id)"
  },
  {
    "natural-language": "Find buildings on any road that spans a single city",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id IN (SELECT r.id FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) GROUP BY r.id HAVING COUNT(DISTINCT c.id) = 1)"
  },
  {
    "natural-language": "Find buildings within one kilometer of three or more roads",
    "sql": "SELECT b.street_number, ST_AsGeoJSON(b.location) AS location FROM buildings b JOIN roads r ON ST_DWithin(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326), 1000) GROUP BY b.id HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find the westernmost building in Ventura",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_X(location) = (SELECT MIN(ST_X(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ventura')))"
  },
  {
    "natural-language": "Find the easternmost building in Camarillo",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_X(location) = (SELECT MAX(ST_X(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Camarillo')))"
  },
  {
    "natural-language": "Find the northernmost building in Ojai",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Y(location) = (SELECT MAX(ST_Y(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ojai')))"
  },
  {
    "natural-language": "Find the southernmost building in Oxnard",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Y(location) = (SELECT MIN(ST_Y(location)) FROM buildings WHERE ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Oxnard')))"
  },
  {
    "natural-language": "Find buildings in the southern half of Ojai",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Y(location) < (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Ojai') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ojai'))"
  },
  {
    "natural-language": "Find buildings in the northern half of Camarillo",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_Y(location) > (SELECT ST_Y(ST_Centroid(boundary)) FROM cities WHERE name = 'Camarillo') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Camarillo'))"
  },
  {
    "natural-language": "Find buildings in the eastern half of Ventura",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_X(location) > (SELECT ST_X(ST_Centroid(boundary)) FROM cities WHERE name = 'Ventura') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Ventura'))"
  },
  {
    "natural-language": "Find buildings in the western half of Oxnard",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE ST_X(location) < (SELECT ST_X(ST_Centroid(boundary)) FROM cities WHERE name = 'Oxnard') AND ST_Within(location, (SELECT boundary FROM cities WHERE name = 'Oxnard'))"
  },
  {
    "natural-language": "Find owners with buildings in Oxnard",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Oxnard'"
  },
  {
    "natural-language": "Find groups that own buildings in Ventura",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Ventura' AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find individual owners with buildings in Ojai",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Ojai' AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find groups that own buildings in Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Camarillo' AND o.is_group = TRUE"
  },
  {
    "natural-language": "Find owners that have buildings in more than one city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) GROUP BY o.id HAVING COUNT(DISTINCT c.id) > 1"
  },
  {
    "natural-language": "Find owners that have buildings in a single city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) GROUP BY o.id HAVING COUNT(DISTINCT c.id) = 1"
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
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Camarillo' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 10000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within eighty five kilometers of Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Camarillo' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 85000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within 2 km of Oxnard",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Oxnard' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 2000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within sixty five kilometers of Camarillo",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Camarillo' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 65000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings within 2km of Ventura",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Ventura' AND ST_Distance(b.location, ST_SetSRID(ST_Point(-119.9895, 34.2197), 4326)) <= 2000 GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
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
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.name = 'Ventura' AND o.is_group = FALSE"
  },
  {
    "natural-language": "Find the owner with the most buildings in the most populated city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.id = (SELECT id FROM cities ORDER BY population DESC LIMIT 1) GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the owner with the most buildings in the least populated city",
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) WHERE c.id = (SELECT id FROM cities ORDER BY population ASC LIMIT 1) GROUP BY o.id ORDER BY COUNT(b.id) DESC LIMIT 1"
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
    "sql": "SELECT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN cities c ON ST_Within(ST_Transform(b.location, 4326), ST_Transform(c.boundary, 4326)) GROUP BY o.id HAVING COUNT(DISTINCT c.id) > 1 AND COUNT(b.id) >= 2"
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
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN parks p ON ST_DWithin(ST_Transform(b.location, 4326), ST_Transform(p.boundary, 4326), 1000)"
  },
  {
    "natural-language": "Find owners of buildings within two kilometers of a park",
    "sql": "SELECT DISTINCT o.name FROM owning_entities o JOIN buildings b ON o.id = b.owning_entity_id JOIN parks p ON ST_DWithin(ST_Transform(b.location, 4326), ST_Transform(p.boundary, 4326), 2000)"
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