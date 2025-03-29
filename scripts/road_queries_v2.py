ROAD_QUERIES_V2 = [
    # Find roads that are longer than, at least, shorter than, and at most using Web Mercator for length (1 - 200 km)
    {
        "natural-language": "Find roads that are longer than one kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1000"
    },
    {
        "natural-language": "Find roads that are longer than two kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
    },
    {
        "natural-language": "Find roads that are longer than three kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3000"
    },
    {
        "natural-language": "Find roads that are longer than four kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
    },
    {
        "natural-language": "Find roads that are longer than five kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
    },
    {
        "natural-language": "Find roads that are longer than six kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
    },
    {
        "natural-language": "Find roads that are longer than seven kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7000"
    },
    {
        "natural-language": "Find roads that are longer than eight kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8000"
    },
    {
        "natural-language": "Find roads that are longer than nine kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9000"
    },
    {
        "natural-language": "Find roads that are longer than ten kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10000"
    },
    {
        "natural-language": "Find roads that are longer than twenty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20000"
    },
    {
        "natural-language": "Find roads that are longer than thirty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 30000"
    },
    {
        "natural-language": "Find roads that are longer than forty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 40000"
    },
    {
        "natural-language": "Find roads that are longer than fifty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 50000"
    },
    {
        "natural-language": "Find roads that are longer than sixty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 60000"
    },
    {
        "natural-language": "Find roads that are longer than seventy kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 70000"
    },
    {
        "natural-language": "Find roads that are longer than eighty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 80000"
    },
    {
        "natural-language": "Find roads that are longer than ninety kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 90000"
    },
    {
        "natural-language": "Find roads that are longer than one hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 100000"
    },
    {
        "natural-language": "Find roads that are longer than two hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 200000"
    },
    {
        "natural-language": "Find roads that are longer than 1 kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1000"
    },
    {
        "natural-language": "Find roads that are longer than 2 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
    },
    {
        "natural-language": "Find roads that are longer than 3 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3000"
    },
    {
        "natural-language": "Find roads that are longer than 4 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
    },
    {
        "natural-language": "Find roads that are longer than 5 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
    },
    {
        "natural-language": "Find roads that are longer than 6 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
    },
    {
        "natural-language": "Find roads that are longer than 7 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7000"
    },
    {
        "natural-language": "Find roads that are longer than 8 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8000"
    },
    {
        "natural-language": "Find roads that are longer than 9 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9000"
    },
    {
        "natural-language": "Find roads that are longer than 10 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10000"
    },
    {
        "natural-language": "Find roads that are longer than 20 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20000"
    },
    {
        "natural-language": "Find roads that are longer than 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 30000"
    },
    {
        "natural-language": "Find roads that are longer than 40 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 40000"
    },
    {
        "natural-language": "Find roads that are longer than 50 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 50000"
    },
    {
        "natural-language": "Find roads that are longer than 60 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 60000"
    },
    {
        "natural-language": "Find roads that are longer than 70 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 70000"
    },
    {
        "natural-language": "Find roads that are longer than 80 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 80000"
    },
    {
        "natural-language": "Find roads that are longer than 90 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 90000"
    },
    {
        "natural-language": "Find roads that are longer than 100 hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 100000"
    },
    {
        "natural-language": "Find roads that are longer than 200 hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 200000"
    },
    {
        "natural-language": "Find roads that are longer than 1 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1000"
    },
    {
        "natural-language": "Find roads that are longer than 2 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
    },
    {
        "natural-language": "Find roads that are longer than 3 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3000"
    },
    {
        "natural-language": "Find roads that are longer than 4 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
    },
    {
        "natural-language": "Find roads that are longer than 5 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
    },
    {
        "natural-language": "Find roads that are longer than 6 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
    },
    {
        "natural-language": "Find roads that are longer than 7 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7000"
    },
    {
        "natural-language": "Find roads that are longer than 8 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8000"
    },
    {
        "natural-language": "Find roads that are longer than 9 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9000"
    },
    {
        "natural-language": "Find roads that are longer than 10 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10000"
    },
    {
        "natural-language": "Find roads that are longer than 20 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20000"
    },
    {
        "natural-language": "Find roads that are longer than 30 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 30000"
    },
    {
        "natural-language": "Find roads that are longer than 40 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 40000"
    },
    {
        "natural-language": "Find roads that are longer than 50 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 50000"
    },
    {
        "natural-language": "Find roads that are longer than 60 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 60000"
    },
    {
        "natural-language": "Find roads that are longer than 70 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 70000"
    },
    {
        "natural-language": "Find roads that are longer than 80 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 80000"
    },
    {
        "natural-language": "Find roads that are longer than 90 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 90000"
    },
    {
        "natural-language": "Find roads that are longer than 100 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 100000"
    },
    {
        "natural-language": "Find roads that are longer than 200 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 200000"
    },
    {
        "natural-language": "Find roads that are at least one kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1000"
    },
    {
        "natural-language": "Find roads that are at least two kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
    },
    {
        "natural-language": "Find roads that are at least three kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3000"
    },
    {
        "natural-language": "Find roads that are at least four kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
    },
    {
        "natural-language": "Find roads that are at least five kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
    },
    {
        "natural-language": "Find roads that are at least six kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
    },
    {
        "natural-language": "Find roads that are at least seven kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7000"
    },
    {
        "natural-language": "Find roads that are at least eight kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8000"
    },
    {
        "natural-language": "Find roads that are at least nine kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9000"
    },
    {
        "natural-language": "Find roads that are at least ten kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10000"
    },
    {
        "natural-language": "Find roads that are at least twenty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20000"
    },
    {
        "natural-language": "Find roads that are at least thirty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 30000"
    },
    {
        "natural-language": "Find roads that are at least forty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 40000"
    },
    {
        "natural-language": "Find roads that are at least fifty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 50000"
    },
    {
        "natural-language": "Find roads that are at least sixty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 60000"
    },
    {
        "natural-language": "Find roads that are at least seventy kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 70000"
    },
    {
        "natural-language": "Find roads that are at least eighty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 80000"
    },
    {
        "natural-language": "Find roads that are at least ninety kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 90000"
    },
    {
        "natural-language": "Find roads that are at least one hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 100000"
    },
    {
        "natural-language": "Find roads that are at least two hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 200000"
    },
    {
        "natural-language": "Find roads that are at least 1 kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1000"
    },
    {
        "natural-language": "Find roads that are at least 2 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
    },
    {
        "natural-language": "Find roads that are at least 3 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3000"
    },
    {
        "natural-language": "Find roads that are at least 4 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
    },
    {
        "natural-language": "Find roads that are at least 5 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
    },
    {
        "natural-language": "Find roads that are at least 6 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
    },
    {
        "natural-language": "Find roads that are at least 7 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7000"
    },
    {
        "natural-language": "Find roads that are at least 8 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8000"
    },
    {
        "natural-language": "Find roads that are at least 9 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9000"
    },
    {
        "natural-language": "Find roads that are at least 10 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10000"
    },
    {
        "natural-language": "Find roads that are at least 20 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20000"
    },
    {
        "natural-language": "Find roads that are at least 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 30000"
    },
    {
        "natural-language": "Find roads that are at least 40 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 40000"
    },
    {
        "natural-language": "Find roads that are at least 50 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 50000"
    },
    {
        "natural-language": "Find roads that are at least 60 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 60000"
    },
    {
        "natural-language": "Find roads that are at least 70 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 70000"
    },
    {
        "natural-language": "Find roads that are at least 80 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 80000"
    },
    {
        "natural-language": "Find roads that are at least 90 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 90000"
    },
    {
        "natural-language": "Find roads that are at least 100 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 100000"
    },
    {
        "natural-language": "Find roads that are at least 200 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 200000"
    },
    {
        "natural-language": "Find roads that are at least 1 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1000"
    },
    {
        "natural-language": "Find roads that are at least 2 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
    },
    {
        "natural-language": "Find roads that are at least 3 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3000"
    },
    {
        "natural-language": "Find roads that are at least 4 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
    },
    {
        "natural-language": "Find roads that are at least 5 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
    },
    {
        "natural-language": "Find roads that are at least 6 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
    },
    {
        "natural-language": "Find roads that are at least 7 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7000"
    },
    {
        "natural-language": "Find roads that are at least 8 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8000"
    },
    {
        "natural-language": "Find roads that are at least 9 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9000"
    },
    {
        "natural-language": "Find roads that are at least 10 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10000"
    },
    {
        "natural-language": "Find roads that are at least 20 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20000"
    },
    {
        "natural-language": "Find roads that are at least 30 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 30000"
    },
    {
        "natural-language": "Find roads that are at least 40 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 40000"
    },
    {
        "natural-language": "Find roads that are at least 50 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 50000"
    },
    {
        "natural-language": "Find roads that are at least 60 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 60000"
    },
    {
        "natural-language": "Find roads that are at least 70 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 70000"
    },
    {
        "natural-language": "Find roads that are at least 80 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 80000"
    },
    {
        "natural-language": "Find roads that are at least 90 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 90000"
    },
    {
        "natural-language": "Find roads that are at least 100 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 100000"
    },
    {
        "natural-language": "Find roads that are at least 200 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 200000"
    },
    {
        "natural-language": "Find roads that are shorter than one kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1000"
    },
    {
        "natural-language": "Find roads that are shorter than two kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
    },
    {
        "natural-language": "Find roads that are shorter than three kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3000"
    },
    {
        "natural-language": "Find roads that are shorter than four kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
    },
    {
        "natural-language": "Find roads that are shorter than five kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
    },
    {
        "natural-language": "Find roads that are shorter than six kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
    },
    {
        "natural-language": "Find roads that are shorter than seven kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7000"
    },
    {
        "natural-language": "Find roads that are shorter than eight kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8000"
    },
    {
        "natural-language": "Find roads that are shorter than nine kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9000"
    },
    {
        "natural-language": "Find roads that are shorter than ten kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10000"
    },
    {
        "natural-language": "Find roads that are shorter than twenty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20000"
    },
    {
        "natural-language": "Find roads that are shorter than thirty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 30000"
    },
    {
        "natural-language": "Find roads that are shorter than forty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 40000"
    },
    {
        "natural-language": "Find roads that are shorter than fifty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 50000"
    },
    {
        "natural-language": "Find roads that are shorter than sixty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 60000"
    },
    {
        "natural-language": "Find roads that are shorter than seventy kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 70000"
    },
    {
        "natural-language": "Find roads that are shorter than eighty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 80000"
    },
    {
        "natural-language": "Find roads that are shorter than ninety kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 90000"
    },
    {
        "natural-language": "Find roads that are shorter than one hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 100000"
    },
    {
        "natural-language": "Find roads that are shorter than two hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 200000"
    },
    {
        "natural-language": "Find roads that are shorter than 1 kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1000"
    },
    {
        "natural-language": "Find roads that are shorter than 2 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
    },
    {
        "natural-language": "Find roads that are shorter than 3 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3000"
    },
    {
        "natural-language": "Find roads that are shorter than 4 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
    },
    {
        "natural-language": "Find roads that are shorter than 5 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
    },
    {
        "natural-language": "Find roads that are shorter than 6 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
    },
    {
        "natural-language": "Find roads that are shorter than 7 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7000"
    },
    {
        "natural-language": "Find roads that are shorter than 8 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8000"
    },
    {
        "natural-language": "Find roads that are shorter than 9 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9000"
    },
    {
        "natural-language": "Find roads that are shorter than 10 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10000"
    },
    {
        "natural-language": "Find roads that are shorter than 20 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20000"
    },
    {
        "natural-language": "Find roads that are shorter than 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 30000"
    },
    {
        "natural-language": "Find roads that are shorter than 40 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 40000"
    },
    {
        "natural-language": "Find roads that are shorter than 50 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 50000"
    },
    {
        "natural-language": "Find roads that are shorter than 60 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 60000"
    },
    {
        "natural-language": "Find roads that are shorter than 70 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 70000"
    },
    {
        "natural-language": "Find roads that are shorter than 80 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 80000"
    },
    {
        "natural-language": "Find roads that are shorter than 90 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 90000"
    },
    {
        "natural-language": "Find roads that are shorter than 100 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 100000"
    },
    {
        "natural-language": "Find roads that are shorter than 200 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 200000"
    },
    {
        "natural-language": "Find roads that are shorter than 1 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1000"
    },
    {
        "natural-language": "Find roads that are shorter than 2 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
    },
    {
        "natural-language": "Find roads that are shorter than 3 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3000"
    },
    {
        "natural-language": "Find roads that are shorter than 4 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
    },
    {
        "natural-language": "Find roads that are shorter than 5 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
    },
    {
        "natural-language": "Find roads that are shorter than 6 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
    },
    {
        "natural-language": "Find roads that are shorter than 7 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7000"
    },
    {
        "natural-language": "Find roads that are shorter than 8 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8000"
    },
    {
        "natural-language": "Find roads that are shorter than 9 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9000"
    },
    {
        "natural-language": "Find roads that are shorter than 10 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10000"
    },
    {
        "natural-language": "Find roads that are shorter than 20 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20000"
    },
    {
        "natural-language": "Find roads that are shorter than 30 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 30000"
    },
    {
        "natural-language": "Find roads that are shorter than 40 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 40000"
    },
    {
        "natural-language": "Find roads that are shorter than 50 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 50000"
    },
    {
        "natural-language": "Find roads that are shorter than 60 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 60000"
    },
    {
        "natural-language": "Find roads that are shorter than 70 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 70000"
    },
    {
        "natural-language": "Find roads that are shorter than 80 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 80000"
    },
    {
        "natural-language": "Find roads that are shorter than 90 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 90000"
    },
    {
        "natural-language": "Find roads that are shorter than 100 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 100000"
    },
    {
        "natural-language": "Find roads that are shorter than 200 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 200000"
    },
    {
        "natural-language": "Find roads that are at most one kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1000"
    },
    {
        "natural-language": "Find roads that are at most two kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2000"
    },
    {
        "natural-language": "Find roads that are at most three kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3000"
    },
    {
        "natural-language": "Find roads that are at most four kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4000"
    },
    {
        "natural-language": "Find roads that are at most five kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5000"
    },
    {
        "natural-language": "Find roads that are at most six kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6000"
    },
    {
        "natural-language": "Find roads that are at most seven kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7000"
    },
    {
        "natural-language": "Find roads that are at most eight kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8000"
    },
    {
        "natural-language": "Find roads that are at most nine kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9000"
    },
    {
        "natural-language": "Find roads that are at most ten kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10000"
    },
    {
        "natural-language": "Find roads that are at most twenty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20000"
    },
    {
        "natural-language": "Find roads that are at most thirty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 30000"
    },
    {
        "natural-language": "Find roads that are at most forty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 40000"
    },
    {
        "natural-language": "Find roads that are at most fifty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 50000"
    },
    {
        "natural-language": "Find roads that are at most sixty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 60000"
    },
    {
        "natural-language": "Find roads that are at most seventy kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 70000"
    },
    {
        "natural-language": "Find roads that are at most eighty kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 80000"
    },
    {
        "natural-language": "Find roads that are at most ninety kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 90000"
    },
    {
        "natural-language": "Find roads that are at most one hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 100000"
    },
    {
        "natural-language": "Find roads that are at most two hundred kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 200000"
    },
    {
        "natural-language": "Find roads that are at most 1 kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1000"
    },
    {
        "natural-language": "Find roads that are at most 2 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2000"
    },
    {
        "natural-language": "Find roads that are at most 3 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3000"
    },
    {
        "natural-language": "Find roads that are at most 4 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4000"
    },
    {
        "natural-language": "Find roads that are at most 5 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5000"
    },
    {
        "natural-language": "Find roads that are at most 6 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6000"
    },
    {
        "natural-language": "Find roads that are at most 7 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7000"
    },
    {
        "natural-language": "Find roads that are at most 8 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8000"
    },
    {
        "natural-language": "Find roads that are at most 9 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9000"
    },
    {
        "natural-language": "Find roads that are at most 10 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10000"
    },
    {
        "natural-language": "Find roads that are at most 20 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20000"
    },
    {
        "natural-language": "Find roads that are at most 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 30000"
    },
    {
        "natural-language": "Find roads that are at most 40 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 40000"
    },
    {
        "natural-language": "Find roads that are at most 50 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 50000"
    },
    {
        "natural-language": "Find roads that are at most 60 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 60000"
    },
    {
        "natural-language": "Find roads that are at most 70 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 70000"
    },
    {
        "natural-language": "Find roads that are at most 80 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 80000"
    },
    {
        "natural-language": "Find roads that are at most 90 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 90000"
    },
    {
        "natural-language": "Find roads that are at most 100 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 100000"
    },
    {
        "natural-language": "Find roads that are at most 200 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 200000"
    },
    {
        "natural-language": "Find roads that are at most 1 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1000"
    },
    {
        "natural-language": "Find roads that are at most 2 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2000"
    },
    {
        "natural-language": "Find roads that are at most 3 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3000"
    },
    {
        "natural-language": "Find roads that are at most 4 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4000"
    },
    {
        "natural-language": "Find roads that are at most 5 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5000"
    },
    {
        "natural-language": "Find roads that are at most 6 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6000"
    },
    {
        "natural-language": "Find roads that are at most 7 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7000"
    },
    {
        "natural-language": "Find roads that are at most 8 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8000"
    },
    {
        "natural-language": "Find roads that are at most 9 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9000"
    },
    {
        "natural-language": "Find roads that are at most 10 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10000"
    },
    {
        "natural-language": "Find roads that are at most 20 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20000"
    },
    {
        "natural-language": "Find roads that are at most 30 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 30000"
    },
    {
        "natural-language": "Find roads that are at most 40 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 40000"
    },
    {
        "natural-language": "Find roads that are at most 50 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 50000"
    },
    {
        "natural-language": "Find roads that are at most 60 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 60000"
    },
    {
        "natural-language": "Find roads that are at most 70 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 70000"
    },
    {
        "natural-language": "Find roads that are at most 80 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 80000"
    },
    {
        "natural-language": "Find roads that are at most 90 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 90000"
    },
    {
        "natural-language": "Find roads that are at most 100 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 100000"
    },
    {
        "natural-language": "Find roads that are at most 200 km",
        "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 200000"
    },
    # Find roads by City (1 - 200 km)
    {
        "natural-language": "Find roads within a quarter of a kilometer of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    # End Words
    {
        "natural-language": "Find roads within .25 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within a quarter of a kilometer of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within half of a kilometer of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within one kilometer of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within one and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within two kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within two and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within three kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within three and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within four kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within four and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within five kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within five and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within six kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within six and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within seven kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within seven and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within eight kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within eight and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within nine kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within nine and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within ten kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within ten and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within eleven kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within eleven and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within twelve kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within twelve and a half kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within thirteen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within fourteen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within fifteen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within sixteen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within seventeen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within eighteen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within nineteen kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within twenty kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within twenty one kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within twenty two kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within twenty three kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within twenty four kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within twenty five kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within twenty six kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within twenty seven kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within twenty eight kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within twenty nine kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within thirty kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within forty kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within fifty kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within sixty kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within seventy kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within eighty kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within ninety kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within one hundred kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within two hundred kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads within .25 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 250)"
    },
    {
        "natural-language": "Find roads within .5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 500)"
    },
    {
        "natural-language": "Find roads within 1 kilometer of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1000)"
    },
    {
        "natural-language": "Find roads within 1.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 1500)"
    },
    {
        "natural-language": "Find roads within 2 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2000)"
    },
    {
        "natural-language": "Find roads within 2.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 2500)"
    },
    {
        "natural-language": "Find roads within 3 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3000)"
    },
    {
        "natural-language": "Find roads within 3.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 3500)"
    },
    {
        "natural-language": "Find roads within 4 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4000)"
    },
    {
        "natural-language": "Find roads within 4.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 4500)"
    },
    {
        "natural-language": "Find roads within 5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5000)"
    },
    {
        "natural-language": "Find roads within 5.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 5500)"
    },
    {
        "natural-language": "Find roads within 6 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6000)"
    },
    {
        "natural-language": "Find roads within 6.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 6500)"
    },
    {
        "natural-language": "Find roads within 7 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7000)"
    },
    {
        "natural-language": "Find roads within 7.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 7500)"
    },
    {
        "natural-language": "Find roads within 8 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8000)"
    },
    {
        "natural-language": "Find roads within 8.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 8500)"
    },
    {
        "natural-language": "Find roads within 9 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9000)"
    },
    {
        "natural-language": "Find roads within 9.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 9500)"
    },
    {
        "natural-language": "Find roads within 10 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10000)"
    },
    {
        "natural-language": "Find roads within 10.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 10500)"
    },
    {
        "natural-language": "Find roads within 11 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11000)"
    },
    {
        "natural-language": "Find roads within 11.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 11500)"
    },
    {
        "natural-language": "Find roads within 12 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12000)"
    },
    {
        "natural-language": "Find roads within 12.5 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 12500)"
    },
    {
        "natural-language": "Find roads within 13 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 13000)"
    },
    {
        "natural-language": "Find roads within 14 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 14000)"
    },
    {
        "natural-language": "Find roads within 15 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 15000)"
    },
    {
        "natural-language": "Find roads within 16 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 16000)"
    },
    {
        "natural-language": "Find roads within 17 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 17000)"
    },
    {
        "natural-language": "Find roads within 18 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 18000)"
    },
    {
        "natural-language": "Find roads within 19 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 19000)"
    },
    {
        "natural-language": "Find roads within 20 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 20000)"
    },
    {
        "natural-language": "Find roads within 21 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 21000)"
    },
    {
        "natural-language": "Find roads within 22 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 22000)"
    },
    {
        "natural-language": "Find roads within 23 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 23000)"
    },
    {
        "natural-language": "Find roads within 24 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 24000)"
    },
    {
        "natural-language": "Find roads within 25 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 25000)"
    },
    {
        "natural-language": "Find roads within 26 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 26000)"
    },
    {
        "natural-language": "Find roads within 27 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 27000)"
    },
    {
        "natural-language": "Find roads within 28 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 28000)"
    },
    {
        "natural-language": "Find roads within 29 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 29000)"
    },
    {
        "natural-language": "Find roads within 30 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 30000)"
    },
    {
        "natural-language": "Find roads within 40 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 40000)"
    },
    {
        "natural-language": "Find roads within 50 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 50000)"
    },
    {
        "natural-language": "Find roads within 60 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 60000)"
    },
    {
        "natural-language": "Find roads within 70 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 70000)"
    },
    {
        "natural-language": "Find roads within 80 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 80000)"
    },
    {
        "natural-language": "Find roads within 90 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 90000)"
    },
    {
        "natural-language": "Find roads within 100 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 100000)"
    },
    {
        "natural-language": "Find roads within 200 kilometers of Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_DWithin(ST_Transform(c.boundary, 2229), ST_Transform(r.route, 2229), 200000)"
    },
    {
        "natural-language": "Find roads in Ojai",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Camarillo",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Oxnard",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Ventura",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Fillmore",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Moorpark",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Simi Valley",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Santa Paula",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Thousand Oaks",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_Intersects(c.boundary, r.route)"
    },
    {
        "natural-language": "Find roads in Port Hueneme",
        "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_Intersects(c.boundary, r.route)"
    },
    # Find roads in City that are longer than, at least, shorter than and at most
    {
        "natural-language": "Find roads in Ventura that are longer than one kilometer",
        "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.name = 'Ventura' AND ST_Length(ST_Transform(r.route, 3857)) > 1000"
    }

]