-- TODO: Take this on - Coffee that compares prices in a distance

-- NLP based GIS used to analyze risk to property from flood, fire and (landslide?), air quality
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
