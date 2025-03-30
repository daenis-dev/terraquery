CITY_QUERIES = [
    # Find cities with a population greater than, at least, less than, at most (10,000 - 400,000)
    {
        "natural-language": "Find cities with a population greater than ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000"
    },
    {
        "natural-language": "Find cities with a population greater than twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000"
    },
    {
        "natural-language": "Find cities with a population greater than thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000"
    },
    {
        "natural-language": "Find cities with a population greater than forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000"
    },
    {
        "natural-language": "Find cities with a population greater than fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 500000"
    },
    {
        "natural-language": "Find cities with a population greater than sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 600000"
    },
    {
        "natural-language": "Find cities with a population greater than seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 700000"
    },
    {
        "natural-language": "Find cities with a population greater than eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 800000"
    },
    {
        "natural-language": "Find cities with a population greater than ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 900000"
    },
    {
        "natural-language": "Find cities with a population greater than one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 1000000"
    },
    {
        "natural-language": "Find cities with a population greater than two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 2000000"
    },
    {
        "natural-language": "Find cities with a population greater than three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 3000000"
    },
    {
        "natural-language": "Find cities with a population greater than four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 4000000"
    },
    {
        "natural-language": "Find cities with a population greater than 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000"
    },
    {
        "natural-language": "Find cities with a population greater than 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000"
    },
    {
        "natural-language": "Find cities with a population greater than 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000"
    },
    {
        "natural-language": "Find cities with a population greater than 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000"
    },
    {
        "natural-language": "Find cities with a population greater than 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 500000"
    },
    {
        "natural-language": "Find cities with a population greater than 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 600000"
    },
    {
        "natural-language": "Find cities with a population greater than 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 700000"
    },
    {
        "natural-language": "Find cities with a population greater than 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 800000"
    },
    {
        "natural-language": "Find cities with a population greater than 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 900000"
    },
    {
        "natural-language": "Find cities with a population greater than 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 1000000"
    },
    {
        "natural-language": "Find cities with a population greater than 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 2000000"
    },
    {
        "natural-language": "Find cities with a population greater than 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 3000000"
    },
    {
        "natural-language": "Find cities with a population greater than 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 4000000"
    },
    {
        "natural-language": "Find cities with a population greater than 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000"
    },
    {
        "natural-language": "Find cities with a population greater than 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000"
    },
    {
        "natural-language": "Find cities with a population greater than 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000"
    },
    {
        "natural-language": "Find cities with a population greater than 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000"
    },
    {
        "natural-language": "Find cities with a population greater than 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 500000"
    },
    {
        "natural-language": "Find cities with a population greater than 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 600000"
    },
    {
        "natural-language": "Find cities with a population greater than 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 700000"
    },
    {
        "natural-language": "Find cities with a population greater than 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 800000"
    },
    {
        "natural-language": "Find cities with a population greater than 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 900000"
    },
    {
        "natural-language": "Find cities with a population greater than 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 1000000"
    },
    {
        "natural-language": "Find cities with a population greater than 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 2000000"
    },
    {
        "natural-language": "Find cities with a population greater than 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 3000000"
    },
    {
        "natural-language": "Find cities with a population greater than 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 4000000"
    },
    {
        "natural-language": "Find cities with a population of at least ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000"
    },
    {
        "natural-language": "Find cities with a population of at least twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000"
    },
    {
        "natural-language": "Find cities with a population of at least thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000"
    },
    {
        "natural-language": "Find cities with a population of at least forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000"
    },
    {
        "natural-language": "Find cities with a population of at least fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 500000"
    },
    {
        "natural-language": "Find cities with a population of at least sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 600000"
    },
    {
        "natural-language": "Find cities with a population of at least seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 700000"
    },
    {
        "natural-language": "Find cities with a population of at least eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 800000"
    },
    {
        "natural-language": "Find cities with a population of at least ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 900000"
    },
    {
        "natural-language": "Find cities with a population of at least one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 1000000"
    },
    {
        "natural-language": "Find cities with a population of at least two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 2000000"
    },
    {
        "natural-language": "Find cities with a population of at least three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 3000000"
    },
    {
        "natural-language": "Find cities with a population of at least four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 4000000"
    },
    {
        "natural-language": "Find cities with a population of at least 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000"
    },
    {
        "natural-language": "Find cities with a population of at least 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000"
    },
    {
        "natural-language": "Find cities with a population of at least 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000"
    },
    {
        "natural-language": "Find cities with a population of at least 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000"
    },
    {
        "natural-language": "Find cities with a population of at least 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 500000"
    },
    {
        "natural-language": "Find cities with a population of at least 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 600000"
    },
    {
        "natural-language": "Find cities with a population of at least 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 700000"
    },
    {
        "natural-language": "Find cities with a population of at least 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 800000"
    },
    {
        "natural-language": "Find cities with a population of at least 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 900000"
    },
    {
        "natural-language": "Find cities with a population of at least 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 1000000"
    },
    {
        "natural-language": "Find cities with a population of at least 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 2000000"
    },
    {
        "natural-language": "Find cities with a population of at least 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 3000000"
    },
    {
        "natural-language": "Find cities with a population of at least 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 4000000"
    },
    {
        "natural-language": "Find cities with a population of at least 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000"
    },
    {
        "natural-language": "Find cities with a population of at least 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000"
    },
    {
        "natural-language": "Find cities with a population of at least 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000"
    },
    {
        "natural-language": "Find cities with a population of at least 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000"
    },
    {
        "natural-language": "Find cities with a population of at least 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 500000"
    },
    {
        "natural-language": "Find cities with a population of at least 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 600000"
    },
    {
        "natural-language": "Find cities with a population of at least 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 700000"
    },
    {
        "natural-language": "Find cities with a population of at least 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 800000"
    },
    {
        "natural-language": "Find cities with a population of at least 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 900000"
    },
    {
        "natural-language": "Find cities with a population of at least 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 1000000"
    },
    {
        "natural-language": "Find cities with a population of at least 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 2000000"
    },
    {
        "natural-language": "Find cities with a population of at least 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 3000000"
    },
    {
        "natural-language": "Find cities with a population of at least 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 4000000"
    },
    {
        "natural-language": "Find cities with a population less than ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000"
    },
    {
        "natural-language": "Find cities with a population less than twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000"
    },
    {
        "natural-language": "Find cities with a population less than thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000"
    },
    {
        "natural-language": "Find cities with a population less than forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000"
    },
    {
        "natural-language": "Find cities with a population less than fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 500000"
    },
    {
        "natural-language": "Find cities with a population less than sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 600000"
    },
    {
        "natural-language": "Find cities with a population less than seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 700000"
    },
    {
        "natural-language": "Find cities with a population less than eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 800000"
    },
    {
        "natural-language": "Find cities with a population less than ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 900000"
    },
    {
        "natural-language": "Find cities with a population less than one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 1000000"
    },
    {
        "natural-language": "Find cities with a population less than two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 2000000"
    },
    {
        "natural-language": "Find cities with a population less than three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 3000000"
    },
    {
        "natural-language": "Find cities with a population less than four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 4000000"
    },
    {
        "natural-language": "Find cities with a population less than 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000"
    },
    {
        "natural-language": "Find cities with a population less than 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000"
    },
    {
        "natural-language": "Find cities with a population less than 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000"
    },
    {
        "natural-language": "Find cities with a population less than 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000"
    },
    {
        "natural-language": "Find cities with a population less than 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 500000"
    },
    {
        "natural-language": "Find cities with a population less than 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 600000"
    },
    {
        "natural-language": "Find cities with a population less than 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 700000"
    },
    {
        "natural-language": "Find cities with a population less than 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 800000"
    },
    {
        "natural-language": "Find cities with a population less than 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 900000"
    },
    {
        "natural-language": "Find cities with a population less than 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 1000000"
    },
    {
        "natural-language": "Find cities with a population less than 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 2000000"
    },
    {
        "natural-language": "Find cities with a population less than 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 3000000"
    },
    {
        "natural-language": "Find cities with a population less than 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 4000000"
    },
    {
        "natural-language": "Find cities with a population less than 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000"
    },
    {
        "natural-language": "Find cities with a population less than 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000"
    },
    {
        "natural-language": "Find cities with a population less than 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000"
    },
    {
        "natural-language": "Find cities with a population less than 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000"
    },
    {
        "natural-language": "Find cities with a population less than 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 500000"
    },
    {
        "natural-language": "Find cities with a population less than 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 600000"
    },
    {
        "natural-language": "Find cities with a population less than 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 700000"
    },
    {
        "natural-language": "Find cities with a population less than 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 800000"
    },
    {
        "natural-language": "Find cities with a population less than 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 900000"
    },
    {
        "natural-language": "Find cities with a population less than 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 1000000"
    },
    {
        "natural-language": "Find cities with a population less than 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 2000000"
    },
    {
        "natural-language": "Find cities with a population less than 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 3000000"
    },
    {
        "natural-language": "Find cities with a population less than 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 4000000"
    },
    {
        "natural-language": "Find cities with a population of at most ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000"
    },
    {
        "natural-language": "Find cities with a population of at most twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000"
    },
    {
        "natural-language": "Find cities with a population of at most thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000"
    },
    {
        "natural-language": "Find cities with a population of at most forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000"
    },
    {
        "natural-language": "Find cities with a population of at most fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 500000"
    },
    {
        "natural-language": "Find cities with a population of at most sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 600000"
    },
    {
        "natural-language": "Find cities with a population of at most seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 700000"
    },
    {
        "natural-language": "Find cities with a population of at most eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 800000"
    },
    {
        "natural-language": "Find cities with a population of at most ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 900000"
    },
    {
        "natural-language": "Find cities with a population of at most one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 1000000"
    },
    {
        "natural-language": "Find cities with a population of at most two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 2000000"
    },
    {
        "natural-language": "Find cities with a population of at most three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 3000000"
    },
    {
        "natural-language": "Find cities with a population of at most four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 4000000"
    },
    {
        "natural-language": "Find cities with a population of at most 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000"
    },
    {
        "natural-language": "Find cities with a population of at most 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000"
    },
    {
        "natural-language": "Find cities with a population of at most 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000"
    },
    {
        "natural-language": "Find cities with a population of at most 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000"
    },
    {
        "natural-language": "Find cities with a population of at most 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 500000"
    },
    {
        "natural-language": "Find cities with a population of at most 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 600000"
    },
    {
        "natural-language": "Find cities with a population of at most 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 700000"
    },
    {
        "natural-language": "Find cities with a population of at most 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 800000"
    },
    {
        "natural-language": "Find cities with a population of at most 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 900000"
    },
    {
        "natural-language": "Find cities with a population of at most 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 1000000"
    },
    {
        "natural-language": "Find cities with a population of at most 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 2000000"
    },
    {
        "natural-language": "Find cities with a population of at most 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 3000000"
    },
    {
        "natural-language": "Find cities with a population of at most 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 4000000"
    },
    {
        "natural-language": "Find cities with a population of at most 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000"
    },
    {
        "natural-language": "Find cities with a population of at most 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000"
    },
    {
        "natural-language": "Find cities with a population of at most 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000"
    },
    {
        "natural-language": "Find cities with a population of at most 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000"
    },
    {
        "natural-language": "Find cities with a population of at most 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 500000"
    },
    {
        "natural-language": "Find cities with a population of at most 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 600000"
    },
    {
        "natural-language": "Find cities with a population of at most 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 700000"
    },
    {
        "natural-language": "Find cities with a population of at most 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 800000"
    },
    {
        "natural-language": "Find cities with a population of at most 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 900000"
    },
    {
        "natural-language": "Find cities with a population of at most 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 1000000"
    },
    {
        "natural-language": "Find cities with a population of at most 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 2000000"
    },
    {
        "natural-language": "Find cities with a population of at most 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 3000000"
    },
    {
        "natural-language": "Find cities with a population of at most 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 4000000"
    },
    # Find cities by area greater than, at least, less than and at most (1 - 200 sq km)
    {
        "natural-language": "Find cities with an area greater than one square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 1000000"
    },
    {
        "natural-language": "Find cities with an area greater than two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 2000000"
    },
    {
        "natural-language": "Find cities with an area greater than three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 3000000"
    },
    {
        "natural-language": "Find cities with an area greater than four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 4000000"
    },
    {
        "natural-language": "Find cities with an area greater than five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 5000000"
    },
    {
        "natural-language": "Find cities with an area greater than six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 6000000"
    },
    {
        "natural-language": "Find cities with an area greater than seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 7000000"
    },
    {
        "natural-language": "Find cities with an area greater than eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 8000000"
    },
    {
        "natural-language": "Find cities with an area greater than nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 9000000"
    },
    {
        "natural-language": "Find cities with an area greater than ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 10000000"
    },
    {
        "natural-language": "Find cities with an area greater than eleven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 11000000"
    },
    {
        "natural-language": "Find cities with an area greater than twelve square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 12000000"
    },
    {
        "natural-language": "Find cities with an area greater than thirteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 13000000"
    },
    {
        "natural-language": "Find cities with an area greater than fourteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 14000000"
    },
    {
        "natural-language": "Find cities with an area greater than fifteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 15000000"
    },
    {
        "natural-language": "Find cities with an area greater than sixteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 16000000"
    },
    {
        "natural-language": "Find cities with an area greater than seventeen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 17000000"
    },
    {
        "natural-language": "Find cities with an area greater than eighteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 18000000"
    },
    {
        "natural-language": "Find cities with an area greater than nineteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 19000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 20000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty one square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 21000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 22000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 23000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 24000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 25000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 26000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 27000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 28000000"
    },
    {
        "natural-language": "Find cities with an area greater than twenty nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 29000000"
    },
    {
        "natural-language": "Find cities with an area greater than thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 30000000"
    },
    {
        "natural-language": "Find cities with an area greater than forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 40000000"
    },
    {
        "natural-language": "Find cities with an area greater than fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 50000000"
    },
    {
        "natural-language": "Find cities with an area greater than sixty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 60000000"
    },
    {
        "natural-language": "Find cities with an area greater than seventy square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 70000000"
    },
    {
        "natural-language": "Find cities with an area greater than eighty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 80000000"
    },
    {
        "natural-language": "Find cities with an area greater than ninety square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 90000000"
    },
    {
        "natural-language": "Find cities with an area greater than one hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 100000000"
    },
    {
        "natural-language": "Find cities with an area greater than one hundred ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 110000000"
    },
    {
        "natural-language": "Find cities with an area greater than one hundred twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 120000000"
    },
    {
        "natural-language": "Find cities with an area greater than one hundred thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 130000000"
    },
    {
        "natural-language": "Find cities with an area greater than one hundred forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 140000000"
    },
    {
        "natural-language": "Find cities with an area greater than one hundred fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 150000000"
    },
    {
        "natural-language": "Find cities with an area greater than two hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 200000000"
    },
    {
        "natural-language": "Find cities with an area greater than 1 square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 1000000"
    },
    {
        "natural-language": "Find cities with an area greater than 2 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 2000000"
    },
    {
        "natural-language": "Find cities with an area greater than 3 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 3000000"
    },
    {
        "natural-language": "Find cities with an area greater than 4 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 4000000"
    },
    {
        "natural-language": "Find cities with an area greater than 5 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 5000000"
    },
    {
        "natural-language": "Find cities with an area greater than 6 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 6000000"
    },
    {
        "natural-language": "Find cities with an area greater than 7 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 7000000"
    },
    {
        "natural-language": "Find cities with an area greater than 8 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 8000000"
    },
    {
        "natural-language": "Find cities with an area greater than 9 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 9000000"
    },
    {
        "natural-language": "Find cities with an area greater than 10 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 10000000"
    },
    {
        "natural-language": "Find cities with an area greater than 11 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 11000000"
    },
    {
        "natural-language": "Find cities with an area greater than 12 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 12000000"
    },
    {
        "natural-language": "Find cities with an area greater than 13 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 13000000"
    },
    {
        "natural-language": "Find cities with an area greater than 14 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 14000000"
    },
    {
        "natural-language": "Find cities with an area greater than 15 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 15000000"
    },
    {
        "natural-language": "Find cities with an area greater than 16 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 16000000"
    },
    {
        "natural-language": "Find cities with an area greater than 17 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 17000000"
    },
    {
        "natural-language": "Find cities with an area greater than 18 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 18000000"
    },
    {
        "natural-language": "Find cities with an area greater than 19 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 19000000"
    },
    {
        "natural-language": "Find cities with an area greater than 20 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 20000000"
    },
    {
        "natural-language": "Find cities with an area greater than 21 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 21000000"
    },
    {
        "natural-language": "Find cities with an area greater than 22 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 22000000"
    },
    {
        "natural-language": "Find cities with an area greater than 23 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 23000000"
    },
    {
        "natural-language": "Find cities with an area greater than 24 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 24000000"
    },
    {
        "natural-language": "Find cities with an area greater than 25 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 25000000"
    },
    {
        "natural-language": "Find cities with an area greater than 26 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 26000000"
    },
    {
        "natural-language": "Find cities with an area greater than 27 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 27000000"
    },
    {
        "natural-language": "Find cities with an area greater than 28 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 28000000"
    },
    {
        "natural-language": "Find cities with an area greater than 29 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 29000000"
    },
    {
        "natural-language": "Find cities with an area greater than 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 30000000"
    },
    {
        "natural-language": "Find cities with an area greater than 40 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 40000000"
    },
    {
        "natural-language": "Find cities with an area greater than 50 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 50000000"
    },
    {
        "natural-language": "Find cities with an area greater than 60 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 60000000"
    },
    {
        "natural-language": "Find cities with an area greater than 70 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 70000000"
    },
    {
        "natural-language": "Find cities with an area greater than 80 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 80000000"
    },
    {
        "natural-language": "Find cities with an area greater than 90 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 90000000"
    },
    {
        "natural-language": "Find cities with an area greater than 100 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 100000000"
    },
    {
        "natural-language": "Find cities with an area greater than 110 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 110000000"
    },
    {
        "natural-language": "Find cities with an area greater than 120 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 120000000"
    },
    {
        "natural-language": "Find cities with an area greater than 130 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 130000000"
    },
    {
        "natural-language": "Find cities with an area greater than 140 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 140000000"
    },
    {
        "natural-language": "Find cities with an area greater than 150 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 150000000"
    },
    {
        "natural-language": "Find cities with an area greater than 200 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) > 200000000"
    },
    {
        "natural-language": "Find cities with an area of at least one square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 1000000"
    },
    {
        "natural-language": "Find cities with an area of at least two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 2000000"
    },
    {
        "natural-language": "Find cities with an area of at least three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 3000000"
    },
    {
        "natural-language": "Find cities with an area of at least four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 4000000"
    },
    {
        "natural-language": "Find cities with an area of at least five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 5000000"
    },
    {
        "natural-language": "Find cities with an area of at least six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 6000000"
    },
    {
        "natural-language": "Find cities with an area of at least seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 7000000"
    },
    {
        "natural-language": "Find cities with an area of at least eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 8000000"
    },
    {
        "natural-language": "Find cities with an area of at least nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 9000000"
    },
    {
        "natural-language": "Find cities with an area of at least ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 10000000"
    },
    {
        "natural-language": "Find cities with an area of at least eleven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 11000000"
    },
    {
        "natural-language": "Find cities with an area of at least twelve square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 12000000"
    },
    {
        "natural-language": "Find cities with an area of at least thirteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 13000000"
    },
    {
        "natural-language": "Find cities with an area of at least fourteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 14000000"
    },
    {
        "natural-language": "Find cities with an area of at least fifteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 15000000"
    },
    {
        "natural-language": "Find cities with an area of at least sixteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 16000000"
    },
    {
        "natural-language": "Find cities with an area of at least seventeen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 17000000"
    },
    {
        "natural-language": "Find cities with an area of at least eighteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 18000000"
    },
    {
        "natural-language": "Find cities with an area of at least nineteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 19000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 20000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty one square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 21000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 22000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 23000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 24000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 25000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 26000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 27000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 28000000"
    },
    {
        "natural-language": "Find cities with an area of at least twenty nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 29000000"
    },
    {
        "natural-language": "Find cities with an area of at least thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 30000000"
    },
    {
        "natural-language": "Find cities with an area of at least forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 40000000"
    },
    {
        "natural-language": "Find cities with an area of at least fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 50000000"
    },
    {
        "natural-language": "Find cities with an area of at least sixty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 60000000"
    },
    {
        "natural-language": "Find cities with an area of at least seventy square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 70000000"
    },
    {
        "natural-language": "Find cities with an area of at least eighty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 80000000"
    },
    {
        "natural-language": "Find cities with an area of at least ninety square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 90000000"
    },
    {
        "natural-language": "Find cities with an area of at least one hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 100000000"
    },
    {
        "natural-language": "Find cities with an area of at least one hundred ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 110000000"
    },
    {
        "natural-language": "Find cities with an area of at least one hundred twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 120000000"
    },
    {
        "natural-language": "Find cities with an area of at least one hundred thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 130000000"
    },
    {
        "natural-language": "Find cities with an area of at least one hundred forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 140000000"
    },
    {
        "natural-language": "Find cities with an area of at least one hundred fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 150000000"
    },
    {
        "natural-language": "Find cities with an area of at least two hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 200000000"
    },
    {
        "natural-language": "Find cities with an area of at least 1 square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 1000000"
    },
    {
        "natural-language": "Find cities with an area of at least 2 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 2000000"
    },
    {
        "natural-language": "Find cities with an area of at least 3 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 3000000"
    },
    {
        "natural-language": "Find cities with an area of at least 4 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 4000000"
    },
    {
        "natural-language": "Find cities with an area of at least 5 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 5000000"
    },
    {
        "natural-language": "Find cities with an area of at least 6 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 6000000"
    },
    {
        "natural-language": "Find cities with an area of at least 7 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 7000000"
    },
    {
        "natural-language": "Find cities with an area of at least 8 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 8000000"
    },
    {
        "natural-language": "Find cities with an area of at least 9 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 9000000"
    },
    {
        "natural-language": "Find cities with an area of at least 10 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 10000000"
    },
    {
        "natural-language": "Find cities with an area of at least 11 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 11000000"
    },
    {
        "natural-language": "Find cities with an area of at least 12 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 12000000"
    },
    {
        "natural-language": "Find cities with an area of at least 13 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 13000000"
    },
    {
        "natural-language": "Find cities with an area of at least 14 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 14000000"
    },
    {
        "natural-language": "Find cities with an area of at least 15 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 15000000"
    },
    {
        "natural-language": "Find cities with an area of at least 16 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 16000000"
    },
    {
        "natural-language": "Find cities with an area of at least 17 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 17000000"
    },
    {
        "natural-language": "Find cities with an area of at least 18 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 18000000"
    },
    {
        "natural-language": "Find cities with an area of at least 19 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 19000000"
    },
    {
        "natural-language": "Find cities with an area of at least 20 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 20000000"
    },
    {
        "natural-language": "Find cities with an area of at least 21 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 21000000"
    },
    {
        "natural-language": "Find cities with an area of at least 22 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 22000000"
    },
    {
        "natural-language": "Find cities with an area of at least 23 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 23000000"
    },
    {
        "natural-language": "Find cities with an area of at least 24 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 24000000"
    },
    {
        "natural-language": "Find cities with an area of at least 25 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 25000000"
    },
    {
        "natural-language": "Find cities with an area of at least 26 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 26000000"
    },
    {
        "natural-language": "Find cities with an area of at least 27 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 27000000"
    },
    {
        "natural-language": "Find cities with an area of at least 28 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 28000000"
    },
    {
        "natural-language": "Find cities with an area of at least 29 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 29000000"
    },
    {
        "natural-language": "Find cities with an area of at least 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 30000000"
    },
    {
        "natural-language": "Find cities with an area of at least 40 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 40000000"
    },
    {
        "natural-language": "Find cities with an area of at least 50 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 50000000"
    },
    {
        "natural-language": "Find cities with an area of at least 60 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 60000000"
    },
    {
        "natural-language": "Find cities with an area of at least 70 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 70000000"
    },
    {
        "natural-language": "Find cities with an area of at least 80 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 80000000"
    },
    {
        "natural-language": "Find cities with an area of at least 90 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 90000000"
    },
    {
        "natural-language": "Find cities with an area of at least 100 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 100000000"
    },
    {
        "natural-language": "Find cities with an area of at least 110 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 110000000"
    },
    {
        "natural-language": "Find cities with an area of at least 120 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 120000000"
    },
    {
        "natural-language": "Find cities with an area of at least 130 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 130000000"
    },
    {
        "natural-language": "Find cities with an area of at least 140 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 140000000"
    },
    {
        "natural-language": "Find cities with an area of at least 150 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 150000000"
    },
    {
        "natural-language": "Find cities with an area of at least 200 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) >= 200000000"
    },
    {
        "natural-language": "Find cities with an area less than one square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 1000000"
    },
    {
        "natural-language": "Find cities with an area less than two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 2000000"
    },
    {
        "natural-language": "Find cities with an area less than three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 3000000"
    },
    {
        "natural-language": "Find cities with an area less than four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 4000000"
    },
    {
        "natural-language": "Find cities with an area less than five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 5000000"
    },
    {
        "natural-language": "Find cities with an area less than six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 6000000"
    },
    {
        "natural-language": "Find cities with an area less than seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 7000000"
    },
    {
        "natural-language": "Find cities with an area less than eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 8000000"
    },
    {
        "natural-language": "Find cities with an area less than nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 9000000"
    },
    {
        "natural-language": "Find cities with an area less than ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 10000000"
    },
    {
        "natural-language": "Find cities with an area less than eleven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 11000000"
    },
    {
        "natural-language": "Find cities with an area less than twelve square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 12000000"
    },
    {
        "natural-language": "Find cities with an area less than thirteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 13000000"
    },
    {
        "natural-language": "Find cities with an area less than fourteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 14000000"
    },
    {
        "natural-language": "Find cities with an area less than fifteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 15000000"
    },
    {
        "natural-language": "Find cities with an area less than sixteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 16000000"
    },
    {
        "natural-language": "Find cities with an area less than seventeen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 17000000"
    },
    {
        "natural-language": "Find cities with an area less than eighteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 18000000"
    },
    {
        "natural-language": "Find cities with an area less than nineteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 19000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 20000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty one square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 21000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 22000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 23000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 24000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 25000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 26000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 27000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 28000000"
    },
    {
        "natural-language": "Find cities with an area less than twenty nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 29000000"
    },
    {
        "natural-language": "Find cities with an area less than thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 30000000"
    },
    {
        "natural-language": "Find cities with an area less than forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 40000000"
    },
    {
        "natural-language": "Find cities with an area less than fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 50000000"
    },
    {
        "natural-language": "Find cities with an area less than sixty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 60000000"
    },
    {
        "natural-language": "Find cities with an area less than seventy square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 70000000"
    },
    {
        "natural-language": "Find cities with an area less than eighty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 80000000"
    },
    {
        "natural-language": "Find cities with an area less than ninety square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 90000000"
    },
    {
        "natural-language": "Find cities with an area less than one hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 100000000"
    },
    {
        "natural-language": "Find cities with an area less than one hundred ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 110000000"
    },
    {
        "natural-language": "Find cities with an area less than one hundred twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 120000000"
    },
    {
        "natural-language": "Find cities with an area less than one hundred thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 130000000"
    },
    {
        "natural-language": "Find cities with an area less than one hundred forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 140000000"
    },
    {
        "natural-language": "Find cities with an area less than one hundred fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 150000000"
    },
    {
        "natural-language": "Find cities with an area less than two hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 200000000"
    },
    {
        "natural-language": "Find cities with an area less than 1 square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 1000000"
    },
    {
        "natural-language": "Find cities with an area less than 2 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 2000000"
    },
    {
        "natural-language": "Find cities with an area less than 3 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 3000000"
    },
    {
        "natural-language": "Find cities with an area less than 4 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 4000000"
    },
    {
        "natural-language": "Find cities with an area less than 5 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 5000000"
    },
    {
        "natural-language": "Find cities with an area less than 6 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 6000000"
    },
    {
        "natural-language": "Find cities with an area less than 7 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 7000000"
    },
    {
        "natural-language": "Find cities with an area less than 8 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 8000000"
    },
    {
        "natural-language": "Find cities with an area less than 9 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 9000000"
    },
    {
        "natural-language": "Find cities with an area less than 10 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 10000000"
    },
    {
        "natural-language": "Find cities with an area less than 11 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 11000000"
    },
    {
        "natural-language": "Find cities with an area less than 12 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 12000000"
    },
    {
        "natural-language": "Find cities with an area less than 13 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 13000000"
    },
    {
        "natural-language": "Find cities with an area less than 14 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 14000000"
    },
    {
        "natural-language": "Find cities with an area less than 15 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 15000000"
    },
    {
        "natural-language": "Find cities with an area less than 16 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 16000000"
    },
    {
        "natural-language": "Find cities with an area less than 17 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 17000000"
    },
    {
        "natural-language": "Find cities with an area less than 18 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 18000000"
    },
    {
        "natural-language": "Find cities with an area less than 19 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 19000000"
    },
    {
        "natural-language": "Find cities with an area less than 20 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 20000000"
    },
    {
        "natural-language": "Find cities with an area less than 21 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 21000000"
    },
    {
        "natural-language": "Find cities with an area less than 22 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 22000000"
    },
    {
        "natural-language": "Find cities with an area less than 23 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 23000000"
    },
    {
        "natural-language": "Find cities with an area less than 24 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 24000000"
    },
    {
        "natural-language": "Find cities with an area less than 25 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 25000000"
    },
    {
        "natural-language": "Find cities with an area less than 26 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 26000000"
    },
    {
        "natural-language": "Find cities with an area less than 27 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 27000000"
    },
    {
        "natural-language": "Find cities with an area less than 28 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 28000000"
    },
    {
        "natural-language": "Find cities with an area less than 29 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 29000000"
    },
    {
        "natural-language": "Find cities with an area less than 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 30000000"
    },
    {
        "natural-language": "Find cities with an area less than 40 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 40000000"
    },
    {
        "natural-language": "Find cities with an area less than 50 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 50000000"
    },
    {
        "natural-language": "Find cities with an area less than 60 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 60000000"
    },
    {
        "natural-language": "Find cities with an area less than 70 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 70000000"
    },
    {
        "natural-language": "Find cities with an area less than 80 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 80000000"
    },
    {
        "natural-language": "Find cities with an area less than 90 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 90000000"
    },
    {
        "natural-language": "Find cities with an area less than 100 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 100000000"
    },
    {
        "natural-language": "Find cities with an area less than 110 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 110000000"
    },
    {
        "natural-language": "Find cities with an area less than 120 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 120000000"
    },
    {
        "natural-language": "Find cities with an area less than 130 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 130000000"
    },
    {
        "natural-language": "Find cities with an area less than 140 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 140000000"
    },
    {
        "natural-language": "Find cities with an area less than 150 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 150000000"
    },
    {
        "natural-language": "Find cities with an area less than 200 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) < 200000000"
    },
    {
        "natural-language": "Find cities with an area of at most one square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 1000000"
    },
    {
        "natural-language": "Find cities with an area of at most two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 2000000"
    },
    {
        "natural-language": "Find cities with an area of at most three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 3000000"
    },
    {
        "natural-language": "Find cities with an area of at most four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 4000000"
    },
    {
        "natural-language": "Find cities with an area of at most five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 5000000"
    },
    {
        "natural-language": "Find cities with an area of at most six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 6000000"
    },
    {
        "natural-language": "Find cities with an area of at most seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 7000000"
    },
    {
        "natural-language": "Find cities with an area of at most eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 8000000"
    },
    {
        "natural-language": "Find cities with an area of at most nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 9000000"
    },
    {
        "natural-language": "Find cities with an area of at most ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 10000000"
    },
    {
        "natural-language": "Find cities with an area of at most eleven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 11000000"
    },
    {
        "natural-language": "Find cities with an area of at most twelve square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 12000000"
    },
    {
        "natural-language": "Find cities with an area of at most thirteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 13000000"
    },
    {
        "natural-language": "Find cities with an area of at most fourteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 14000000"
    },
    {
        "natural-language": "Find cities with an area of at most fifteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 15000000"
    },
    {
        "natural-language": "Find cities with an area of at most sixteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 16000000"
    },
    {
        "natural-language": "Find cities with an area of at most seventeen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 17000000"
    },
    {
        "natural-language": "Find cities with an area of at most eighteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 18000000"
    },
    {
        "natural-language": "Find cities with an area of at most nineteen square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 19000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 20000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty one square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 21000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty two square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 22000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty three square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 23000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty four square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 24000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty five square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 25000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty six square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 26000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty seven square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 27000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty eight square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 28000000"
    },
    {
        "natural-language": "Find cities with an area of at most twenty nine square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 29000000"
    },
    {
        "natural-language": "Find cities with an area of at most thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 30000000"
    },
    {
        "natural-language": "Find cities with an area of at most forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 40000000"
    },
    {
        "natural-language": "Find cities with an area of at most fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 50000000"
    },
    {
        "natural-language": "Find cities with an area of at most sixty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 60000000"
    },
    {
        "natural-language": "Find cities with an area of at most seventy square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 70000000"
    },
    {
        "natural-language": "Find cities with an area of at most eighty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 80000000"
    },
    {
        "natural-language": "Find cities with an area of at most ninety square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 90000000"
    },
    {
        "natural-language": "Find cities with an area of at most one hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 100000000"
    },
    {
        "natural-language": "Find cities with an area of at most one hundred ten square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 110000000"
    },
    {
        "natural-language": "Find cities with an area of at most one hundred twenty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 120000000"
    },
    {
        "natural-language": "Find cities with an area of at most one hundred thirty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 130000000"
    },
    {
        "natural-language": "Find cities with an area of at most one hundred forty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 140000000"
    },
    {
        "natural-language": "Find cities with an area of at most one hundred fifty square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 150000000"
    },
    {
        "natural-language": "Find cities with an area of at most two hundred square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 200000000"
    },
    {
        "natural-language": "Find cities with an area of at most 1 square kilometer",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 1000000"
    },
    {
        "natural-language": "Find cities with an area of at most 2 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 2000000"
    },
    {
        "natural-language": "Find cities with an area of at most 3 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 3000000"
    },
    {
        "natural-language": "Find cities with an area of at most 4 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 4000000"
    },
    {
        "natural-language": "Find cities with an area of at most 5 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 5000000"
    },
    {
        "natural-language": "Find cities with an area of at most 6 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 6000000"
    },
    {
        "natural-language": "Find cities with an area of at most 7 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 7000000"
    },
    {
        "natural-language": "Find cities with an area of at most 8 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 8000000"
    },
    {
        "natural-language": "Find cities with an area of at most 9 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 9000000"
    },
    {
        "natural-language": "Find cities with an area of at most 10 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 10000000"
    },
    {
        "natural-language": "Find cities with an area of at most 11 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 11000000"
    },
    {
        "natural-language": "Find cities with an area of at most 12 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 12000000"
    },
    {
        "natural-language": "Find cities with an area of at most 13 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 13000000"
    },
    {
        "natural-language": "Find cities with an area of at most 14 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 14000000"
    },
    {
        "natural-language": "Find cities with an area of at most 15 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 15000000"
    },
    {
        "natural-language": "Find cities with an area of at most 16 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 16000000"
    },
    {
        "natural-language": "Find cities with an area of at most 17 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 17000000"
    },
    {
        "natural-language": "Find cities with an area of at most 18 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 18000000"
    },
    {
        "natural-language": "Find cities with an area of at most 19 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 19000000"
    },
    {
        "natural-language": "Find cities with an area of at most 20 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 20000000"
    },
    {
        "natural-language": "Find cities with an area of at most 21 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 21000000"
    },
    {
        "natural-language": "Find cities with an area of at most 22 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 22000000"
    },
    {
        "natural-language": "Find cities with an area of at most 23 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 23000000"
    },
    {
        "natural-language": "Find cities with an area of at most 24 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 24000000"
    },
    {
        "natural-language": "Find cities with an area of at most 25 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 25000000"
    },
    {
        "natural-language": "Find cities with an area of at most 26 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 26000000"
    },
    {
        "natural-language": "Find cities with an area of at most 27 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 27000000"
    },
    {
        "natural-language": "Find cities with an area of at most 28 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 28000000"
    },
    {
        "natural-language": "Find cities with an area of at most 29 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 29000000"
    },
    {
        "natural-language": "Find cities with an area of at most 30 kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 30000000"
    },
    {
        "natural-language": "Find cities with an area of at most 40 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 40000000"
    },
    {
        "natural-language": "Find cities with an area of at most 50 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 50000000"
    },
    {
        "natural-language": "Find cities with an area of at most 60 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 60000000"
    },
    {
        "natural-language": "Find cities with an area of at most 70 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 70000000"
    },
    {
        "natural-language": "Find cities with an area of at most 80 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 80000000"
    },
    {
        "natural-language": "Find cities with an area of at most 90 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 90000000"
    },
    {
        "natural-language": "Find cities with an area of at most 100 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 100000000"
    },
    {
        "natural-language": "Find cities with an area of at most 110 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 110000000"
    },
    {
        "natural-language": "Find cities with an area of at most 120 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 120000000"
    },
    {
        "natural-language": "Find cities with an area of at most 130 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 130000000"
    },
    {
        "natural-language": "Find cities with an area of at most 140 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 140000000"
    },
    {
        "natural-language": "Find cities with an area of at most 150 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 150000000"
    },
    {
        "natural-language": "Find cities with an area of at most 200 square kilometers",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_Area(ST_Transform(boundary, 3857)) <= 200000000"
    },
    # Find cities by area and population
    {
        "natural-language": "Find the city with the smallest area and a population greater than five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population greater than 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at least 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population less than 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 5000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 10000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 15000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 20000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 25000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 35000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 40000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 55000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 60000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 65000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 75000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 85000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 95000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 115000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 125000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 130000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 140000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 205000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 210000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 215000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 225000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 230000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 305000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 310000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 315000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 325000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 330000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the smallest area and a population of at most 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population greater than 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at least 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population less than 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most thirty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most forty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most fifty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most sixty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most sixty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most seventy thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most seventy five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most eighty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most eighty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most ninety thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most ninety five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred forty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most one hundred fifty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most two hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred ten thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred fifteen thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred twenty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred twenty five thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most three hundred thirty thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most four hundred thousand people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 5000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 10000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 15000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 20000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 25000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 30000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 35000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 40000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 45000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 50000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 55000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 60000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 65000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 70000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 75000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 80000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 85000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 90000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 95000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 100000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 105000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 110000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 115000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 120000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 125000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 130000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 140000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 150000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 200000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 205000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 210000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 215000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 220000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 225000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 230000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 300000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 305000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 310000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 315000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 320000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 325000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 330000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 400000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 5,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 5000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 10,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 10000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 15,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 15000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 20,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 20000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 25,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 25000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 30,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 35,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 35000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 40,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 40000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 45,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 50,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 55,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 55000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 60,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 60000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 65,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 65000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 70,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 70000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 75,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 75000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 80,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 85,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 85000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 90,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 95,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 95000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 100,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 105,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 110,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 115,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 115000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 120,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 125,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 125000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 130,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 130000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 140,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 140000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 150,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 200,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 205,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 205000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 210,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 210000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 215,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 215000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 220,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 225,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 225000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 230,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 230000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 300,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 305,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 305000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 310,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 310000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 315,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 315000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 320,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 325,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 325000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 330,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 330000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
    {
        "natural-language": "Find the city with the largest area and a population of at most 400,000 people",
        "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000 ORDER BY ST_Area(boundary) DESC LIMIT 1"
    },
]