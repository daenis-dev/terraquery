BASE_QUERIES = [
  {
    "natural-language": "Find cities within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find cities within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326))"
  },
  {
    "natural-language": "Find cities within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
  {
    "natural-language": "Find cities within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c WHERE ST_Within(c.boundary, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326))"
  },
  # Find cities by matching criteria around population (0 - 400000)
  {
    "natural-language": "Find cities with a population greater than one hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000"
  },
  {
    "natural-language": "Find cities with a population greater than eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000"
  },
  {
    "natural-language": "Find cities with a population greater than forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100"
  },
  {
    "natural-language": "Find cities with a population greater than ninety people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90"
  },
  {
    "natural-language": "Find cities with a population greater than fourteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 14"
  },
  {
    "natural-language": "Find cities with a population greater than seventy nine thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 79000"
  },
  {
    "natural-language": "Find cities with a population greater than fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000"
  },
  {
    "natural-language": "Find cities with a population greater than seven hundred sixty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 762"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 319"
  },
  {
    "natural-language": "Find cities with a population greater than eight hundred forty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 846"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 268000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred thousand four hundred sixteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100416"
  },
  {
    "natural-language": "Find cities with a population greater than two thousand four hundred fifty nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 2459"
  },
  {
    "natural-language": "Find cities with a population greater than thirty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population greater than seven hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 700"
  },
  {
    "natural-language": "Find cities with a population greater than eighty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 86"
  },
  {
    "natural-language": "Find cities with a population greater than thirty eight people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 38"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred twenty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred thousand nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300019"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100500"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred five thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105500"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred fifty thousand five hundred fifty five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 155555"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 250000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred ten thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred ten thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110111"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred eleven thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 111111"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred thirty three thousand nine hundred seventy people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 133970"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 368000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred thirty three thousand three hundred thirty three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 333333"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 355000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 390000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 380000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 308000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 345000"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 340005"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 350206"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 347903"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred sixteen thousand three hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 316399"
  },
  {
    "natural-language": "Find cities with a population greater than three hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320712"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred twenty two thousand two hundred twenty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 222222"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 255000"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 290000"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 280000"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 208000"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 245000"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 240005"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 250206"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 247903"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 216299"
  },
  {
    "natural-language": "Find cities with a population greater than two hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220712"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 468000"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred forty four thousand four hundred fourty four people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 444444"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 455000"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 490000"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 480000"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 408000"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 445000"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 440005"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 450206"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 447903"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 416299"
  },
  {
    "natural-language": "Find cities with a population greater than four hundred twenty thousand seven hundred forteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 420714"
  },
  {
    "natural-language": "Find cities with a population greater than one hundred and fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population greater than 100000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000"
  },
  {
    "natural-language": "Find cities with a population greater than 80000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000"
  },
  {
    "natural-language": "Find cities with a population greater than 45000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000"
  },
  {
    "natural-language": "Find cities with a population greater than 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100"
  },
  {
    "natural-language": "Find cities with a population greater than 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90"
  },
  {
    "natural-language": "Find cities with a population greater than 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 14"
  },
  {
    "natural-language": "Find cities with a population greater than 79000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 79000"
  },
  {
    "natural-language": "Find cities with a population greater than 50000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000"
  },
  {
    "natural-language": "Find cities with a population greater than 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 762"
  },
  {
    "natural-language": "Find cities with a population greater than 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 319"
  },
  {
    "natural-language": "Find cities with a population greater than 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 846"
  },
  {
    "natural-language": "Find cities with a population greater than 268000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 268000"
  },
  {
    "natural-language": "Find cities with a population greater than 100416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100416"
  },
  {
    "natural-language": "Find cities with a population greater than 2459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 2459"
  },
  {
    "natural-language": "Find cities with a population greater than 30000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000"
  },
  {
    "natural-language": "Find cities with a population greater than 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population greater than 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 700"
  },
  {
    "natural-language": "Find cities with a population greater than 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 86"
  },
  {
    "natural-language": "Find cities with a population greater than 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 38"
  },
  {
    "natural-language": "Find cities with a population greater than 400000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000"
  },
  {
    "natural-language": "Find cities with a population greater than 120000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000"
  },
  {
    "natural-language": "Find cities with a population greater than 300019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300019"
  },
  {
    "natural-language": "Find cities with a population greater than 200000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000"
  },
  {
    "natural-language": "Find cities with a population greater than 100500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100500"
  },
  {
    "natural-language": "Find cities with a population greater than 105000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000"
  },
  {
    "natural-language": "Find cities with a population greater than 105500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105500"
  },
  {
    "natural-language": "Find cities with a population greater than 155555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 155555"
  },
  {
    "natural-language": "Find cities with a population greater than 250000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 250000"
  },
  {
    "natural-language": "Find cities with a population greater than 110000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000"
  },
  {
    "natural-language": "Find cities with a population greater than 110111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110111"
  },
  {
    "natural-language": "Find cities with a population greater than 111111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 111111"
  },
  {
    "natural-language": "Find cities with a population greater than 133970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 133970"
  },
  {
    "natural-language": "Find cities with a population greater than 300000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000"
  },
  {
    "natural-language": "Find cities with a population greater than 368000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 368000"
  },
  {
    "natural-language": "Find cities with a population greater than 333333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 333333"
  },
  {
    "natural-language": "Find cities with a population greater than 355000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 355000"
  },
  {
    "natural-language": "Find cities with a population greater than 390000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 390000"
  },
  {
    "natural-language": "Find cities with a population greater than 380000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 380000"
  },
  {
    "natural-language": "Find cities with a population greater than 308000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 308000"
  },
  {
    "natural-language": "Find cities with a population greater than 345000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 345000"
  },
  {
    "natural-language": "Find cities with a population greater than 340005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 340005"
  },
  {
    "natural-language": "Find cities with a population greater than 350206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 350206"
  },
  {
    "natural-language": "Find cities with a population greater than 347903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 347903"
  },
  {
    "natural-language": "Find cities with a population greater than 316399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 316399"
  },
  {
    "natural-language": "Find cities with a population greater than 320712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320712"
  },
  {
    "natural-language": "Find cities with a population greater than 222222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 222222"
  },
  {
    "natural-language": "Find cities with a population greater than 255000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 255000"
  },
  {
    "natural-language": "Find cities with a population greater than 290000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 290000"
  },
  {
    "natural-language": "Find cities with a population greater than 280000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 280000"
  },
  {
    "natural-language": "Find cities with a population greater than 208000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 208000"
  },
  {
    "natural-language": "Find cities with a population greater than 245000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 245000"
  },
  {
    "natural-language": "Find cities with a population greater than 240005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 240005"
  },
  {
    "natural-language": "Find cities with a population greater than 250206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 250206"
  },
  {
    "natural-language": "Find cities with a population greater than 247903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 247903"
  },
  {
    "natural-language": "Find cities with a population greater than 216299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 216299"
  },
  {
    "natural-language": "Find cities with a population greater than 220712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220712"
  },
  {
    "natural-language": "Find cities with a population greater than 468000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 468000"
  },
  {
    "natural-language": "Find cities with a population greater than 444444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 444444"
  },
  {
    "natural-language": "Find cities with a population greater than 455000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 455000"
  },
  {
    "natural-language": "Find cities with a population greater than 490000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 490000"
  },
  {
    "natural-language": "Find cities with a population greater than 480000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 480000"
  },
  {
    "natural-language": "Find cities with a population greater than 408000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 408000"
  },
  {
    "natural-language": "Find cities with a population greater than 445000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 445000"
  },
  {
    "natural-language": "Find cities with a population greater than 440005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 440005"
  },
  {
    "natural-language": "Find cities with a population greater than 450206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 450206"
  },
  {
    "natural-language": "Find cities with a population greater than 447903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 447903"
  },
  {
    "natural-language": "Find cities with a population greater than 416299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 416299"
  },
  {
    "natural-language": "Find cities with a population greater than 420714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 420714"
  },
  {
    "natural-language": "Find cities with a population greater than 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population greater than 100,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000"
  },
  {
    "natural-language": "Find cities with a population greater than 80,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000"
  },
  {
    "natural-language": "Find cities with a population greater than 45,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 45000"
  },
  {
    "natural-language": "Find cities with a population greater than 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100"
  },
  {
    "natural-language": "Find cities with a population greater than 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90"
  },
  {
    "natural-language": "Find cities with a population greater than 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 14"
  },
  {
    "natural-language": "Find cities with a population greater than 79,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 79000"
  },
  {
    "natural-language": "Find cities with a population greater than 50,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 50000"
  },
  {
    "natural-language": "Find cities with a population greater than 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 762"
  },
  {
    "natural-language": "Find cities with a population greater than 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 319"
  },
  {
    "natural-language": "Find cities with a population greater than 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 846"
  },
  {
    "natural-language": "Find cities with a population greater than 268,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 268000"
  },
  {
    "natural-language": "Find cities with a population greater than 100,416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100416"
  },
  {
    "natural-language": "Find cities with a population greater than 2,459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 2459"
  },
  {
    "natural-language": "Find cities with a population greater than 30,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 30000"
  },
  {
    "natural-language": "Find cities with a population greater than 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population greater than 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 700"
  },
  {
    "natural-language": "Find cities with a population greater than 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 86"
  },
  {
    "natural-language": "Find cities with a population greater than 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 38"
  },
  {
    "natural-language": "Find cities with a population greater than 400,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 400000"
  },
  {
    "natural-language": "Find cities with a population greater than 120,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 120000"
  },
  {
    "natural-language": "Find cities with a population greater than 300,019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300019"
  },
  {
    "natural-language": "Find cities with a population greater than 200,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 200000"
  },
  {
    "natural-language": "Find cities with a population greater than 100,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100500"
  },
  {
    "natural-language": "Find cities with a population greater than 105,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105000"
  },
  {
    "natural-language": "Find cities with a population greater than 105,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 105500"
  },
  {
    "natural-language": "Find cities with a population greater than 155,555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 155555"
  },
  {
    "natural-language": "Find cities with a population greater than 250,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 250000"
  },
  {
    "natural-language": "Find cities with a population greater than 110,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110000"
  },
  {
    "natural-language": "Find cities with a population greater than 110,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 110111"
  },
  {
    "natural-language": "Find cities with a population greater than 111,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 111111"
  },
  {
    "natural-language": "Find cities with a population greater than 133,970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 133970"
  },
  {
    "natural-language": "Find cities with a population greater than 300,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 300000"
  },
  {
    "natural-language": "Find cities with a population greater than 368,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 368000"
  },
  {
    "natural-language": "Find cities with a population greater than 333,333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 333333"
  },
  {
    "natural-language": "Find cities with a population greater than 355,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 355000"
  },
  {
    "natural-language": "Find cities with a population greater than 390,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 390000"
  },
  {
    "natural-language": "Find cities with a population greater than 380,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 380000"
  },
  {
    "natural-language": "Find cities with a population greater than 308,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 308000"
  },
  {
    "natural-language": "Find cities with a population greater than 345,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 345000"
  },
  {
    "natural-language": "Find cities with a population greater than 340,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 340005"
  },
  {
    "natural-language": "Find cities with a population greater than 350,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 350206"
  },
  {
    "natural-language": "Find cities with a population greater than 347,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 347903"
  },
  {
    "natural-language": "Find cities with a population greater than 316,399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 316399"
  },
  {
    "natural-language": "Find cities with a population greater than 320,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 320712"
  },
  {
    "natural-language": "Find cities with a population greater than 222,222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 222222"
  },
  {
    "natural-language": "Find cities with a population greater than 255,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 255000"
  },
  {
    "natural-language": "Find cities with a population greater than 290,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 290000"
  },
  {
    "natural-language": "Find cities with a population greater than 280,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 280000"
  },
  {
    "natural-language": "Find cities with a population greater than 208,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 208000"
  },
  {
    "natural-language": "Find cities with a population greater than 245,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 245000"
  },
  {
    "natural-language": "Find cities with a population greater than 240,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 240005"
  },
  {
    "natural-language": "Find cities with a population greater than 250,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 250206"
  },
  {
    "natural-language": "Find cities with a population greater than 247,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 247903"
  },
  {
    "natural-language": "Find cities with a population greater than 216,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 216299"
  },
  {
    "natural-language": "Find cities with a population greater than 220,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 220712"
  },
  {
    "natural-language": "Find cities with a population greater than 468,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 468000"
  },
  {
    "natural-language": "Find cities with a population greater than 444,444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 444444"
  },
  {
    "natural-language": "Find cities with a population greater than 455,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 455000"
  },
  {
    "natural-language": "Find cities with a population greater than 490,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 490000"
  },
  {
    "natural-language": "Find cities with a population greater than 480,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 480000"
  },
  {
    "natural-language": "Find cities with a population greater than 408,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 408000"
  },
  {
    "natural-language": "Find cities with a population greater than 445,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 445000"
  },
  {
    "natural-language": "Find cities with a population greater than 440,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 440005"
  },
  {
    "natural-language": "Find cities with a population greater than 450,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 450206"
  },
  {
    "natural-language": "Find cities with a population greater than 447,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 447903"
  },
  {
    "natural-language": "Find cities with a population greater than 416,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 416299"
  },
  {
    "natural-language": "Find cities with a population greater than 420,714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 420714"
  },
  {
    "natural-language": "Find cities with a population greater than 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 150000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000"
  },
  {
    "natural-language": "Find cities with a population of at least eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000"
  },
  {
    "natural-language": "Find cities with a population of at least forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100"
  },
  {
    "natural-language": "Find cities with a population of at least ninety people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90"
  },
  {
    "natural-language": "Find cities with a population of at least fourteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 14"
  },
  {
    "natural-language": "Find cities with a population of at least seventy nine thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 79000"
  },
  {
    "natural-language": "Find cities with a population of at least fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000"
  },
  {
    "natural-language": "Find cities with a population of at least seven hundred sixty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 762"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 319"
  },
  {
    "natural-language": "Find cities with a population of at least eight hundred forty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 846"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 268000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred thousand four hundred sixteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100416"
  },
  {
    "natural-language": "Find cities with a population of at least two thousand four hundred fifty nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 2459"
  },
  {
    "natural-language": "Find cities with a population of at least thirty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000"
  },
  {
    "natural-language": "Find cities with a population of at least seven hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 700"
  },
  {
    "natural-language": "Find cities with a population of at least eighty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 86"
  },
  {
    "natural-language": "Find cities with a population of at least thirty eight people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 38"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred twenty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred thousand nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300019"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100500"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred five thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105500"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred fifty thousand five hundred fifty five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 155555"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 250000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred ten thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred ten thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110111"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred eleven thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 111111"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred thirty three thousand nine hundred seventy people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 133970"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 368000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred thirty three thousand three hundred thirty three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 333333"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 355000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 390000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 380000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 308000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 345000"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 340005"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 350206"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 347903"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred sixteen thousand three hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 316399"
  },
  {
    "natural-language": "Find cities with a population of at least three hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320712"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred twenty two thousand two hundred twenty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 222222"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 255000"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 290000"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 280000"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 208000"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 245000"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 240005"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 250206"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 247903"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 216299"
  },
  {
    "natural-language": "Find cities with a population of at least two hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220712"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 468000"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred forty four thousand four hundred fourty four people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 444444"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 455000"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 490000"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 480000"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 408000"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 445000"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 440005"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 450206"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 447903"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 416299"
  },
  {
    "natural-language": "Find cities with a population of at least four hundred twenty thousand seven hundred forteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 420714"
  },
  {
    "natural-language": "Find cities with a population of at least one hundred and fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000"
  },
  {
    "natural-language": "Find cities with a population of at least 100000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000"
  },
  {
    "natural-language": "Find cities with a population of at least 80000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000"
  },
  {
    "natural-language": "Find cities with a population of at least 45000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000"
  },
  {
    "natural-language": "Find cities with a population of at least 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100"
  },
  {
    "natural-language": "Find cities with a population of at least 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90"
  },
  {
    "natural-language": "Find cities with a population of at least 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 14"
  },
  {
    "natural-language": "Find cities with a population of at least 79000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 79000"
  },
  {
    "natural-language": "Find cities with a population of at least 50000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000"
  },
  {
    "natural-language": "Find cities with a population of at least 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 762"
  },
  {
    "natural-language": "Find cities with a population of at least 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 319"
  },
  {
    "natural-language": "Find cities with a population of at least 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 846"
  },
  {
    "natural-language": "Find cities with a population of at least 268000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 268000"
  },
  {
    "natural-language": "Find cities with a population of at least 100416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100416"
  },
  {
    "natural-language": "Find cities with a population of at least 2459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 2459"
  },
  {
    "natural-language": "Find cities with a population of at least 30000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000"
  },
  {
    "natural-language": "Find cities with a population of at least 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000"
  },
  {
    "natural-language": "Find cities with a population of at least 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 700"
  },
  {
    "natural-language": "Find cities with a population of at least 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 86"
  },
  {
    "natural-language": "Find cities with a population of at least 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 38"
  },
  {
    "natural-language": "Find cities with a population of at least 400000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000"
  },
  {
    "natural-language": "Find cities with a population of at least 120000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000"
  },
  {
    "natural-language": "Find cities with a population of at least 300019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300019"
  },
  {
    "natural-language": "Find cities with a population of at least 200000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000"
  },
  {
    "natural-language": "Find cities with a population of at least 100500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100500"
  },
  {
    "natural-language": "Find cities with a population of at least 105000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000"
  },
  {
    "natural-language": "Find cities with a population of at least 105500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105500"
  },
  {
    "natural-language": "Find cities with a population of at least 155555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 155555"
  },
  {
    "natural-language": "Find cities with a population of at least 250000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 250000"
  },
  {
    "natural-language": "Find cities with a population of at least 110000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000"
  },
  {
    "natural-language": "Find cities with a population of at least 110111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110111"
  },
  {
    "natural-language": "Find cities with a population of at least 111111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 111111"
  },
  {
    "natural-language": "Find cities with a population of at least 133970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 133970"
  },
  {
    "natural-language": "Find cities with a population of at least 300000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000"
  },
  {
    "natural-language": "Find cities with a population of at least 368000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 368000"
  },
  {
    "natural-language": "Find cities with a population of at least 333333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 333333"
  },
  {
    "natural-language": "Find cities with a population of at least 355000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 355000"
  },
  {
    "natural-language": "Find cities with a population of at least 390000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 390000"
  },
  {
    "natural-language": "Find cities with a population of at least 380000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 380000"
  },
  {
    "natural-language": "Find cities with a population of at least 308000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 308000"
  },
  {
    "natural-language": "Find cities with a population of at least 345000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 345000"
  },
  {
    "natural-language": "Find cities with a population of at least 340005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 340005"
  },
  {
    "natural-language": "Find cities with a population of at least 350206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 350206"
  },
  {
    "natural-language": "Find cities with a population of at least 347903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 347903"
  },
  {
    "natural-language": "Find cities with a population of at least 316399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 316399"
  },
  {
    "natural-language": "Find cities with a population of at least 320712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320712"
  },
  {
    "natural-language": "Find cities with a population of at least 222222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 222222"
  },
  {
    "natural-language": "Find cities with a population of at least 255000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 255000"
  },
  {
    "natural-language": "Find cities with a population of at least 290000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 290000"
  },
  {
    "natural-language": "Find cities with a population of at least 280000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 280000"
  },
  {
    "natural-language": "Find cities with a population of at least 208000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 208000"
  },
  {
    "natural-language": "Find cities with a population of at least 245000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 245000"
  },
  {
    "natural-language": "Find cities with a population of at least 240005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 240005"
  },
  {
    "natural-language": "Find cities with a population of at least 250206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 250206"
  },
  {
    "natural-language": "Find cities with a population of at least 247903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 247903"
  },
  {
    "natural-language": "Find cities with a population of at least 216299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 216299"
  },
  {
    "natural-language": "Find cities with a population of at least 220712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220712"
  },
  {
    "natural-language": "Find cities with a population of at least 468000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 468000"
  },
  {
    "natural-language": "Find cities with a population of at least 444444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 444444"
  },
  {
    "natural-language": "Find cities with a population of at least 455000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 455000"
  },
  {
    "natural-language": "Find cities with a population of at least 490000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 490000"
  },
  {
    "natural-language": "Find cities with a population of at least 480000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 480000"
  },
  {
    "natural-language": "Find cities with a population of at least 408000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 408000"
  },
  {
    "natural-language": "Find cities with a population of at least 445000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 445000"
  },
  {
    "natural-language": "Find cities with a population of at least 440005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 440005"
  },
  {
    "natural-language": "Find cities with a population of at least 450206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 450206"
  },
  {
    "natural-language": "Find cities with a population of at least 447903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 447903"
  },
  {
    "natural-language": "Find cities with a population of at least 416299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 416299"
  },
  {
    "natural-language": "Find cities with a population of at least 420714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 420714"
  },
  {
    "natural-language": "Find cities with a population of at least 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000"
  },
  {
    "natural-language": "Find cities with a population of at least 100,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100000"
  },
  {
    "natural-language": "Find cities with a population of at least 80,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 80000"
  },
  {
    "natural-language": "Find cities with a population of at least 45,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 45000"
  },
  {
    "natural-language": "Find cities with a population of at least 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100"
  },
  {
    "natural-language": "Find cities with a population of at least 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 90"
  },
  {
    "natural-language": "Find cities with a population of at least 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 14"
  },
  {
    "natural-language": "Find cities with a population of at least 79,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 79000"
  },
  {
    "natural-language": "Find cities with a population of at least 50,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 50000"
  },
  {
    "natural-language": "Find cities with a population of at least 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 762"
  },
  {
    "natural-language": "Find cities with a population of at least 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 319"
  },
  {
    "natural-language": "Find cities with a population of at least 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 846"
  },
  {
    "natural-language": "Find cities with a population of at least 268,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 268000"
  },
  {
    "natural-language": "Find cities with a population of at least 100,416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100416"
  },
  {
    "natural-language": "Find cities with a population of at least 2,459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 2459"
  },
  {
    "natural-language": "Find cities with a population of at least 30,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 30000"
  },
  {
    "natural-language": "Find cities with a population of at least 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000"
  },
  {
    "natural-language": "Find cities with a population of at least 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 700"
  },
  {
    "natural-language": "Find cities with a population of at least 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 86"
  },
  {
    "natural-language": "Find cities with a population of at least 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 38"
  },
  {
    "natural-language": "Find cities with a population of at least 400,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 400000"
  },
  {
    "natural-language": "Find cities with a population of at least 120,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 120000"
  },
  {
    "natural-language": "Find cities with a population of at least 300,019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300019"
  },
  {
    "natural-language": "Find cities with a population of at least 200,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 200000"
  },
  {
    "natural-language": "Find cities with a population of at least 100,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 100500"
  },
  {
    "natural-language": "Find cities with a population of at least 105,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105000"
  },
  {
    "natural-language": "Find cities with a population of at least 105,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 105500"
  },
  {
    "natural-language": "Find cities with a population of at least 155,555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 155555"
  },
  {
    "natural-language": "Find cities with a population of at least 250,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 250000"
  },
  {
    "natural-language": "Find cities with a population of at least 110,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110000"
  },
  {
    "natural-language": "Find cities with a population of at least 110,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 110111"
  },
  {
    "natural-language": "Find cities with a population of at least 111,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 111111"
  },
  {
    "natural-language": "Find cities with a population of at least 133,970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 133970"
  },
  {
    "natural-language": "Find cities with a population of at least 300,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 300000"
  },
  {
    "natural-language": "Find cities with a population of at least 368,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 368000"
  },
  {
    "natural-language": "Find cities with a population of at least 333,333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 333333"
  },
  {
    "natural-language": "Find cities with a population of at least 355,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 355000"
  },
  {
    "natural-language": "Find cities with a population of at least 390,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 390000"
  },
  {
    "natural-language": "Find cities with a population of at least 380,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 380000"
  },
  {
    "natural-language": "Find cities with a population of at least 308,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 308000"
  },
  {
    "natural-language": "Find cities with a population of at least 345,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 345000"
  },
  {
    "natural-language": "Find cities with a population of at least 340,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 340005"
  },
  {
    "natural-language": "Find cities with a population of at least 350,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 350206"
  },
  {
    "natural-language": "Find cities with a population of at least 347,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 347903"
  },
  {
    "natural-language": "Find cities with a population of at least 316,399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 316399"
  },
  {
    "natural-language": "Find cities with a population of at least 320,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 320712"
  },
  {
    "natural-language": "Find cities with a population of at least 222,222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 222222"
  },
  {
    "natural-language": "Find cities with a population of at least 255,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 255000"
  },
  {
    "natural-language": "Find cities with a population of at least 290,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 290000"
  },
  {
    "natural-language": "Find cities with a population of at least 280,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 280000"
  },
  {
    "natural-language": "Find cities with a population of at least 208,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 208000"
  },
  {
    "natural-language": "Find cities with a population of at least 245,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 245000"
  },
  {
    "natural-language": "Find cities with a population of at least 240,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 240005"
  },
  {
    "natural-language": "Find cities with a population of at least 250,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 250206"
  },
  {
    "natural-language": "Find cities with a population of at least 247,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 247903"
  },
  {
    "natural-language": "Find cities with a population of at least 216,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 216299"
  },
  {
    "natural-language": "Find cities with a population of at least 220,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 220712"
  },
  {
    "natural-language": "Find cities with a population of at least 468,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 468000"
  },
  {
    "natural-language": "Find cities with a population of at least 444,444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 444444"
  },
  {
    "natural-language": "Find cities with a population of at least 455,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 455000"
  },
  {
    "natural-language": "Find cities with a population of at least 490,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 490000"
  },
  {
    "natural-language": "Find cities with a population of at least 480,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 480000"
  },
  {
    "natural-language": "Find cities with a population of at least 408,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 408000"
  },
  {
    "natural-language": "Find cities with a population of at least 445,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 445000"
  },
  {
    "natural-language": "Find cities with a population of at least 440,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 440005"
  },
  {
    "natural-language": "Find cities with a population of at least 450,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 450206"
  },
  {
    "natural-language": "Find cities with a population of at least 447,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 447903"
  },
  {
    "natural-language": "Find cities with a population of at least 416,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 416299"
  },
  {
    "natural-language": "Find cities with a population of at least 420,714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 420714"
  },
  {
    "natural-language": "Find cities with a population of at least 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population >= 150000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000"
  },
  {
    "natural-language": "Find cities with a population less than eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000"
  },
  {
    "natural-language": "Find cities with a population less than forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100"
  },
  {
    "natural-language": "Find cities with a population less than ninety people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90"
  },
  {
    "natural-language": "Find cities with a population less than fourteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 14"
  },
  {
    "natural-language": "Find cities with a population less than seventy nine thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 79000"
  },
  {
    "natural-language": "Find cities with a population less than fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000"
  },
  {
    "natural-language": "Find cities with a population less than seven hundred sixty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 762"
  },
  {
    "natural-language": "Find cities with a population less than three hundred nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 319"
  },
  {
    "natural-language": "Find cities with a population less than eight hundred forty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 846"
  },
  {
    "natural-language": "Find cities with a population less than two hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 268000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred thousand four hundred sixteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100416"
  },
  {
    "natural-language": "Find cities with a population less than two thousand four hundred fifty nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 2459"
  },
  {
    "natural-language": "Find cities with a population less than thirty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000"
  },
  {
    "natural-language": "Find cities with a population less than seven hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 700"
  },
  {
    "natural-language": "Find cities with a population less than eighty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 86"
  },
  {
    "natural-language": "Find cities with a population less than thirty eight people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 38"
  },
  {
    "natural-language": "Find cities with a population less than four hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred twenty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred thousand nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300019"
  },
  {
    "natural-language": "Find cities with a population less than two hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100500"
  },
  {
    "natural-language": "Find cities with a population less than one hundred five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred five thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105500"
  },
  {
    "natural-language": "Find cities with a population less than one hundred fifty thousand five hundred fifty five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 155555"
  },
  {
    "natural-language": "Find cities with a population less than two hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 250000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred ten thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000"
  },
  {
    "natural-language": "Find cities with a population less than one hundred ten thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110111"
  },
  {
    "natural-language": "Find cities with a population less than one hundred eleven thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 111111"
  },
  {
    "natural-language": "Find cities with a population less than one hundred thirty three thousand nine hundred seventy people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 133970"
  },
  {
    "natural-language": "Find cities with a population less than three hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 368000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred thirty three thousand three hundred thirty three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 333333"
  },
  {
    "natural-language": "Find cities with a population less than three hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 355000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 390000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 380000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 308000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 345000"
  },
  {
    "natural-language": "Find cities with a population less than three hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 340005"
  },
  {
    "natural-language": "Find cities with a population less than three hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 350206"
  },
  {
    "natural-language": "Find cities with a population less than three hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 347903"
  },
  {
    "natural-language": "Find cities with a population less than three hundred sixteen thousand three hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 316399"
  },
  {
    "natural-language": "Find cities with a population less than three hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320712"
  },
  {
    "natural-language": "Find cities with a population less than two hundred twenty two thousand two hundred twenty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 222222"
  },
  {
    "natural-language": "Find cities with a population less than two hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 255000"
  },
  {
    "natural-language": "Find cities with a population less than two hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 290000"
  },
  {
    "natural-language": "Find cities with a population less than two hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 280000"
  },
  {
    "natural-language": "Find cities with a population less than two hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 208000"
  },
  {
    "natural-language": "Find cities with a population less than two hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 245000"
  },
  {
    "natural-language": "Find cities with a population less than two hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 240005"
  },
  {
    "natural-language": "Find cities with a population less than two hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 250206"
  },
  {
    "natural-language": "Find cities with a population less than two hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 247903"
  },
  {
    "natural-language": "Find cities with a population less than two hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 216299"
  },
  {
    "natural-language": "Find cities with a population less than two hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220712"
  },
  {
    "natural-language": "Find cities with a population less than four hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 468000"
  },
  {
    "natural-language": "Find cities with a population less than four hundred forty four thousand four hundred fourty four people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 444444"
  },
  {
    "natural-language": "Find cities with a population less than four hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 455000"
  },
  {
    "natural-language": "Find cities with a population less than four hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 490000"
  },
  {
    "natural-language": "Find cities with a population less than four hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 480000"
  },
  {
    "natural-language": "Find cities with a population less than four hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 408000"
  },
  {
    "natural-language": "Find cities with a population less than four hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 445000"
  },
  {
    "natural-language": "Find cities with a population less than four hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 440005"
  },
  {
    "natural-language": "Find cities with a population less than four hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 450206"
  },
  {
    "natural-language": "Find cities with a population less than four hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 447903"
  },
  {
    "natural-language": "Find cities with a population less than four hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 416299"
  },
  {
    "natural-language": "Find cities with a population less than four hundred twenty thousand seven hundred forteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 420714"
  },
  {
    "natural-language": "Find cities with a population less than one hundred and fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000"
  },
  {
    "natural-language": "Find cities with a population less than 100000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000"
  },
  {
    "natural-language": "Find cities with a population less than 80000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000"
  },
  {
    "natural-language": "Find cities with a population less than 45000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000"
  },
  {
    "natural-language": "Find cities with a population less than 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100"
  },
  {
    "natural-language": "Find cities with a population less than 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90"
  },
  {
    "natural-language": "Find cities with a population less than 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 14"
  },
  {
    "natural-language": "Find cities with a population less than 79000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 79000"
  },
  {
    "natural-language": "Find cities with a population less than 50000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000"
  },
  {
    "natural-language": "Find cities with a population less than 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 762"
  },
  {
    "natural-language": "Find cities with a population less than 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 319"
  },
  {
    "natural-language": "Find cities with a population less than 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 846"
  },
  {
    "natural-language": "Find cities with a population less than 268000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 268000"
  },
  {
    "natural-language": "Find cities with a population less than 100416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100416"
  },
  {
    "natural-language": "Find cities with a population less than 2459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 2459"
  },
  {
    "natural-language": "Find cities with a population less than 30000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000"
  },
  {
    "natural-language": "Find cities with a population less than 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000"
  },
  {
    "natural-language": "Find cities with a population less than 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 700"
  },
  {
    "natural-language": "Find cities with a population less than 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 86"
  },
  {
    "natural-language": "Find cities with a population less than 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 38"
  },
  {
    "natural-language": "Find cities with a population less than 400000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000"
  },
  {
    "natural-language": "Find cities with a population less than 120000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000"
  },
  {
    "natural-language": "Find cities with a population less than 300019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300019"
  },
  {
    "natural-language": "Find cities with a population less than 200000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000"
  },
  {
    "natural-language": "Find cities with a population less than 100500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100500"
  },
  {
    "natural-language": "Find cities with a population less than 105000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000"
  },
  {
    "natural-language": "Find cities with a population less than 105500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105500"
  },
  {
    "natural-language": "Find cities with a population less than 155555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 155555"
  },
  {
    "natural-language": "Find cities with a population less than 250000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 250000"
  },
  {
    "natural-language": "Find cities with a population less than 110000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000"
  },
  {
    "natural-language": "Find cities with a population less than 110111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110111"
  },
  {
    "natural-language": "Find cities with a population less than 111111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 111111"
  },
  {
    "natural-language": "Find cities with a population less than 133970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 133970"
  },
  {
    "natural-language": "Find cities with a population less than 300000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000"
  },
  {
    "natural-language": "Find cities with a population less than 368000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 368000"
  },
  {
    "natural-language": "Find cities with a population less than 333333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 333333"
  },
  {
    "natural-language": "Find cities with a population less than 355000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 355000"
  },
  {
    "natural-language": "Find cities with a population less than 390000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 390000"
  },
  {
    "natural-language": "Find cities with a population less than 380000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 380000"
  },
  {
    "natural-language": "Find cities with a population less than 308000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 308000"
  },
  {
    "natural-language": "Find cities with a population less than 345000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 345000"
  },
  {
    "natural-language": "Find cities with a population less than 340005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 340005"
  },
  {
    "natural-language": "Find cities with a population less than 350206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 350206"
  },
  {
    "natural-language": "Find cities with a population less than 347903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 347903"
  },
  {
    "natural-language": "Find cities with a population less than 316399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 316399"
  },
  {
    "natural-language": "Find cities with a population less than 320712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320712"
  },
  {
    "natural-language": "Find cities with a population less than 222222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 222222"
  },
  {
    "natural-language": "Find cities with a population less than 255000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 255000"
  },
  {
    "natural-language": "Find cities with a population less than 290000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 290000"
  },
  {
    "natural-language": "Find cities with a population less than 280000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 280000"
  },
  {
    "natural-language": "Find cities with a population less than 208000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 208000"
  },
  {
    "natural-language": "Find cities with a population less than 245000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 245000"
  },
  {
    "natural-language": "Find cities with a population less than 240005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 240005"
  },
  {
    "natural-language": "Find cities with a population less than 250206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 250206"
  },
  {
    "natural-language": "Find cities with a population less than 247903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 247903"
  },
  {
    "natural-language": "Find cities with a population less than 216299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 216299"
  },
  {
    "natural-language": "Find cities with a population less than 220712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220712"
  },
  {
    "natural-language": "Find cities with a population less than 468000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 468000"
  },
  {
    "natural-language": "Find cities with a population less than 444444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 444444"
  },
  {
    "natural-language": "Find cities with a population less than 455000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 455000"
  },
  {
    "natural-language": "Find cities with a population less than 490000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 490000"
  },
  {
    "natural-language": "Find cities with a population less than 480000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 480000"
  },
  {
    "natural-language": "Find cities with a population less than 408000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 408000"
  },
  {
    "natural-language": "Find cities with a population less than 445000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 445000"
  },
  {
    "natural-language": "Find cities with a population less than 440005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 440005"
  },
  {
    "natural-language": "Find cities with a population less than 450206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 450206"
  },
  {
    "natural-language": "Find cities with a population less than 447903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 447903"
  },
  {
    "natural-language": "Find cities with a population less than 416299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 416299"
  },
  {
    "natural-language": "Find cities with a population less than 420714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 420714"
  },
  {
    "natural-language": "Find cities with a population less than 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000"
  },
  {
    "natural-language": "Find cities with a population less than 100,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100000"
  },
  {
    "natural-language": "Find cities with a population less than 80,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 80000"
  },
  {
    "natural-language": "Find cities with a population less than 45,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 45000"
  },
  {
    "natural-language": "Find cities with a population less than 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100"
  },
  {
    "natural-language": "Find cities with a population less than 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 90"
  },
  {
    "natural-language": "Find cities with a population less than 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 14"
  },
  {
    "natural-language": "Find cities with a population less than 79,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 79000"
  },
  {
    "natural-language": "Find cities with a population less than 50,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 50000"
  },
  {
    "natural-language": "Find cities with a population less than 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 762"
  },
  {
    "natural-language": "Find cities with a population less than 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 319"
  },
  {
    "natural-language": "Find cities with a population less than 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 846"
  },
  {
    "natural-language": "Find cities with a population less than 268,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 268000"
  },
  {
    "natural-language": "Find cities with a population less than 100,416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100416"
  },
  {
    "natural-language": "Find cities with a population less than 2,459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 2459"
  },
  {
    "natural-language": "Find cities with a population less than 30,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 30000"
  },
  {
    "natural-language": "Find cities with a population less than 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000"
  },
  {
    "natural-language": "Find cities with a population less than 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 700"
  },
  {
    "natural-language": "Find cities with a population less than 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 86"
  },
  {
    "natural-language": "Find cities with a population less than 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 38"
  },
  {
    "natural-language": "Find cities with a population less than 400,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 400000"
  },
  {
    "natural-language": "Find cities with a population less than 120,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 120000"
  },
  {
    "natural-language": "Find cities with a population less than 300,019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300019"
  },
  {
    "natural-language": "Find cities with a population less than 200,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 200000"
  },
  {
    "natural-language": "Find cities with a population less than 100,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 100500"
  },
  {
    "natural-language": "Find cities with a population less than 105,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105000"
  },
  {
    "natural-language": "Find cities with a population less than 105,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 105500"
  },
  {
    "natural-language": "Find cities with a population less than 155,555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 155555"
  },
  {
    "natural-language": "Find cities with a population less than 250,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 250000"
  },
  {
    "natural-language": "Find cities with a population less than 110,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110000"
  },
  {
    "natural-language": "Find cities with a population less than 110,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 110111"
  },
  {
    "natural-language": "Find cities with a population less than 111,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 111111"
  },
  {
    "natural-language": "Find cities with a population less than 133,970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 133970"
  },
  {
    "natural-language": "Find cities with a population less than 300,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 300000"
  },
  {
    "natural-language": "Find cities with a population less than 368,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 368000"
  },
  {
    "natural-language": "Find cities with a population less than 333,333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 333333"
  },
  {
    "natural-language": "Find cities with a population less than 355,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 355000"
  },
  {
    "natural-language": "Find cities with a population less than 390,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 390000"
  },
  {
    "natural-language": "Find cities with a population less than 380,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 380000"
  },
  {
    "natural-language": "Find cities with a population less than 308,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 308000"
  },
  {
    "natural-language": "Find cities with a population less than 345,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 345000"
  },
  {
    "natural-language": "Find cities with a population less than 340,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 340005"
  },
  {
    "natural-language": "Find cities with a population less than 350,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 350206"
  },
  {
    "natural-language": "Find cities with a population less than 347,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 347903"
  },
  {
    "natural-language": "Find cities with a population less than 316,399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 316399"
  },
  {
    "natural-language": "Find cities with a population less than 320,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 320712"
  },
  {
    "natural-language": "Find cities with a population less than 222,222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 222222"
  },
  {
    "natural-language": "Find cities with a population less than 255,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 255000"
  },
  {
    "natural-language": "Find cities with a population less than 290,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 290000"
  },
  {
    "natural-language": "Find cities with a population less than 280,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 280000"
  },
  {
    "natural-language": "Find cities with a population less than 208,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 208000"
  },
  {
    "natural-language": "Find cities with a population less than 245,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 245000"
  },
  {
    "natural-language": "Find cities with a population less than 240,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 240005"
  },
  {
    "natural-language": "Find cities with a population less than 250,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 250206"
  },
  {
    "natural-language": "Find cities with a population less than 247,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 247903"
  },
  {
    "natural-language": "Find cities with a population less than 216,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 216299"
  },
  {
    "natural-language": "Find cities with a population less than 220,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 220712"
  },
  {
    "natural-language": "Find cities with a population less than 468,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 468000"
  },
  {
    "natural-language": "Find cities with a population less than 444,444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 444444"
  },
  {
    "natural-language": "Find cities with a population less than 455,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 455000"
  },
  {
    "natural-language": "Find cities with a population less than 490,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 490000"
  },
  {
    "natural-language": "Find cities with a population less than 480,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 480000"
  },
  {
    "natural-language": "Find cities with a population less than 408,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 408000"
  },
  {
    "natural-language": "Find cities with a population less than 445,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 445000"
  },
  {
    "natural-language": "Find cities with a population less than 440,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 440005"
  },
  {
    "natural-language": "Find cities with a population less than 450,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 450206"
  },
  {
    "natural-language": "Find cities with a population less than 447,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 447903"
  },
  {
    "natural-language": "Find cities with a population less than 416,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 416299"
  },
  {
    "natural-language": "Find cities with a population less than 420,714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 420714"
  },
  {
    "natural-language": "Find cities with a population less than 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population < 150000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000"
  },
  {
    "natural-language": "Find cities with a population of at most eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000"
  },
  {
    "natural-language": "Find cities with a population of at most forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100"
  },
  {
    "natural-language": "Find cities with a population of at most ninety people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90"
  },
  {
    "natural-language": "Find cities with a population of at most fourteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 14"
  },
  {
    "natural-language": "Find cities with a population of at most seventy nine thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 79000"
  },
  {
    "natural-language": "Find cities with a population of at most fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000"
  },
  {
    "natural-language": "Find cities with a population of at most seven hundred sixty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 762"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 319"
  },
  {
    "natural-language": "Find cities with a population of at most eight hundred forty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 846"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 268000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred thousand four hundred sixteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100416"
  },
  {
    "natural-language": "Find cities with a population of at most two thousand four hundred fifty nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 2459"
  },
  {
    "natural-language": "Find cities with a population of at most thirty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000"
  },
  {
    "natural-language": "Find cities with a population of at most seven hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 700"
  },
  {
    "natural-language": "Find cities with a population of at most eighty six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 86"
  },
  {
    "natural-language": "Find cities with a population of at most thirty eight people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 38"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred twenty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred thousand nineteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300019"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100500"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred five thousand five hundred people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105500"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred fifty thousand five hundred fifty five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 155555"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 250000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred ten thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred ten thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110111"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred eleven thousand one hundred eleven people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 111111"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred thirty three thousand nine hundred seventy people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 133970"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 368000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred thirty three thousand three hundred thirty three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 333333"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 355000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 390000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 380000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 308000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 345000"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 340005"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 350206"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 347903"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred sixteen thousand three hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 316399"
  },
  {
    "natural-language": "Find cities with a population of at most three hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320712"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred twenty two thousand two hundred twenty two people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 222222"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 255000"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 290000"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 280000"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 208000"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 245000"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 240005"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 250206"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 247903"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 216299"
  },
  {
    "natural-language": "Find cities with a population of at most two hundred twenty thousand seven hundred twelve people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220712"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred sixty eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 468000"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred forty four thousand four hundred fourty four people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 444444"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred fifty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 455000"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred ninety thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 490000"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred eighty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 480000"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred eight thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 408000"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred forty five thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 445000"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred forty thousand five people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 440005"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred fifty thousand two hundred six people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 450206"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred forty seven thousand nine hundred three people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 447903"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred sixteen thousand two hundred ninety nine people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 416299"
  },
  {
    "natural-language": "Find cities with a population of at most four hundred twenty thousand seven hundred forteen people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 420714"
  },
  {
    "natural-language": "Find cities with a population of at most one hundred and fifty thousand people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000"
  },
  {
    "natural-language": "Find cities with a population of at most 100000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000"
  },
  {
    "natural-language": "Find cities with a population of at most 80000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000"
  },
  {
    "natural-language": "Find cities with a population of at most 45000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000"
  },
  {
    "natural-language": "Find cities with a population of at most 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100"
  },
  {
    "natural-language": "Find cities with a population of at most 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90"
  },
  {
    "natural-language": "Find cities with a population of at most 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 14"
  },
  {
    "natural-language": "Find cities with a population of at most 79000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 79000"
  },
  {
    "natural-language": "Find cities with a population of at most 50000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000"
  },
  {
    "natural-language": "Find cities with a population of at most 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 762"
  },
  {
    "natural-language": "Find cities with a population of at most 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 319"
  },
  {
    "natural-language": "Find cities with a population of at most 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 846"
  },
  {
    "natural-language": "Find cities with a population of at most 268000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 268000"
  },
  {
    "natural-language": "Find cities with a population of at most 100416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100416"
  },
  {
    "natural-language": "Find cities with a population of at most 2459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 2459"
  },
  {
    "natural-language": "Find cities with a population of at most 30000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000"
  },
  {
    "natural-language": "Find cities with a population of at most 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000"
  },
  {
    "natural-language": "Find cities with a population of at most 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 700"
  },
  {
    "natural-language": "Find cities with a population of at most 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 86"
  },
  {
    "natural-language": "Find cities with a population of at most 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 38"
  },
  {
    "natural-language": "Find cities with a population of at most 400000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000"
  },
  {
    "natural-language": "Find cities with a population of at most 120000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000"
  },
  {
    "natural-language": "Find cities with a population of at most 300019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300019"
  },
  {
    "natural-language": "Find cities with a population of at most 200000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000"
  },
  {
    "natural-language": "Find cities with a population of at most 100500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100500"
  },
  {
    "natural-language": "Find cities with a population of at most 105000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000"
  },
  {
    "natural-language": "Find cities with a population of at most 105500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105500"
  },
  {
    "natural-language": "Find cities with a population of at most 155555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 155555"
  },
  {
    "natural-language": "Find cities with a population of at most 250000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 250000"
  },
  {
    "natural-language": "Find cities with a population of at most 110000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000"
  },
  {
    "natural-language": "Find cities with a population of at most 110111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110111"
  },
  {
    "natural-language": "Find cities with a population of at most 111111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 111111"
  },
  {
    "natural-language": "Find cities with a population of at most 133970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 133970"
  },
  {
    "natural-language": "Find cities with a population of at most 300000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000"
  },
  {
    "natural-language": "Find cities with a population of at most 368000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 368000"
  },
  {
    "natural-language": "Find cities with a population of at most 333333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 333333"
  },
  {
    "natural-language": "Find cities with a population of at most 355000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 355000"
  },
  {
    "natural-language": "Find cities with a population of at most 390000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 390000"
  },
  {
    "natural-language": "Find cities with a population of at most 380000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 380000"
  },
  {
    "natural-language": "Find cities with a population of at most 308000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 308000"
  },
  {
    "natural-language": "Find cities with a population of at most 345000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 345000"
  },
  {
    "natural-language": "Find cities with a population of at most 340005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 340005"
  },
  {
    "natural-language": "Find cities with a population of at most 350206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 350206"
  },
  {
    "natural-language": "Find cities with a population of at most 347903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 347903"
  },
  {
    "natural-language": "Find cities with a population of at most 316399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 316399"
  },
  {
    "natural-language": "Find cities with a population of at most 320712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320712"
  },
  {
    "natural-language": "Find cities with a population of at most 222222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 222222"
  },
  {
    "natural-language": "Find cities with a population of at most 255000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 255000"
  },
  {
    "natural-language": "Find cities with a population of at most 290000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 290000"
  },
  {
    "natural-language": "Find cities with a population of at most 280000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 280000"
  },
  {
    "natural-language": "Find cities with a population of at most 208000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 208000"
  },
  {
    "natural-language": "Find cities with a population of at most 245000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 245000"
  },
  {
    "natural-language": "Find cities with a population of at most 240005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 240005"
  },
  {
    "natural-language": "Find cities with a population of at most 250206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 250206"
  },
  {
    "natural-language": "Find cities with a population of at most 247903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 247903"
  },
  {
    "natural-language": "Find cities with a population of at most 216299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 216299"
  },
  {
    "natural-language": "Find cities with a population of at most 220712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220712"
  },
  {
    "natural-language": "Find cities with a population of at most 468000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 468000"
  },
  {
    "natural-language": "Find cities with a population of at most 444444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 444444"
  },
  {
    "natural-language": "Find cities with a population of at most 455000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 455000"
  },
  {
    "natural-language": "Find cities with a population of at most 490000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 490000"
  },
  {
    "natural-language": "Find cities with a population of at most 480000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 480000"
  },
  {
    "natural-language": "Find cities with a population of at most 408000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 408000"
  },
  {
    "natural-language": "Find cities with a population of at most 445000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 445000"
  },
  {
    "natural-language": "Find cities with a population of at most 440005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 440005"
  },
  {
    "natural-language": "Find cities with a population of at most 450206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 450206"
  },
  {
    "natural-language": "Find cities with a population of at most 447903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 447903"
  },
  {
    "natural-language": "Find cities with a population of at most 416299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 416299"
  },
  {
    "natural-language": "Find cities with a population of at most 420714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 420714"
  },
  {
    "natural-language": "Find cities with a population of at most 150000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000"
  },
  {
    "natural-language": "Find cities with a population of at most 100,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100000"
  },
  {
    "natural-language": "Find cities with a population of at most 80,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 80000"
  },
  {
    "natural-language": "Find cities with a population of at most 45,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 45000"
  },
  {
    "natural-language": "Find cities with a population of at most 100 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100"
  },
  {
    "natural-language": "Find cities with a population of at most 90 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 90"
  },
  {
    "natural-language": "Find cities with a population of at most 14 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 14"
  },
  {
    "natural-language": "Find cities with a population of at most 79,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 79000"
  },
  {
    "natural-language": "Find cities with a population of at most 50,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 50000"
  },
  {
    "natural-language": "Find cities with a population of at most 762 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 762"
  },
  {
    "natural-language": "Find cities with a population of at most 319 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 319"
  },
  {
    "natural-language": "Find cities with a population of at most 846 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 846"
  },
  {
    "natural-language": "Find cities with a population of at most 268,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 268000"
  },
  {
    "natural-language": "Find cities with a population of at most 100,416 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100416"
  },
  {
    "natural-language": "Find cities with a population of at most 2,459 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 2459"
  },
  {
    "natural-language": "Find cities with a population of at most 30,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 30000"
  },
  {
    "natural-language": "Find cities with a population of at most 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000"
  },
  {
    "natural-language": "Find cities with a population of at most 700 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 700"
  },
  {
    "natural-language": "Find cities with a population of at most 86 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 86"
  },
  {
    "natural-language": "Find cities with a population of at most 38 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 38"
  },
  {
    "natural-language": "Find cities with a population of at most 400,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 400000"
  },
  {
    "natural-language": "Find cities with a population of at most 120,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 120000"
  },
  {
    "natural-language": "Find cities with a population of at most 300,019 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300019"
  },
  {
    "natural-language": "Find cities with a population of at most 200,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 200000"
  },
  {
    "natural-language": "Find cities with a population of at most 100,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 100500"
  },
  {
    "natural-language": "Find cities with a population of at most 105,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105000"
  },
  {
    "natural-language": "Find cities with a population of at most 105,500 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 105500"
  },
  {
    "natural-language": "Find cities with a population of at most 155,555 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 155555"
  },
  {
    "natural-language": "Find cities with a population of at most 250,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 250000"
  },
  {
    "natural-language": "Find cities with a population of at most 110,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110000"
  },
  {
    "natural-language": "Find cities with a population of at most 110,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 110111"
  },
  {
    "natural-language": "Find cities with a population of at most 111,111 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 111111"
  },
  {
    "natural-language": "Find cities with a population of at most 133,970 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 133970"
  },
  {
    "natural-language": "Find cities with a population of at most 300,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 300000"
  },
  {
    "natural-language": "Find cities with a population of at most 368,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 368000"
  },
  {
    "natural-language": "Find cities with a population of at most 333,333 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 333333"
  },
  {
    "natural-language": "Find cities with a population of at most 355,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 355000"
  },
  {
    "natural-language": "Find cities with a population of at most 390,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 390000"
  },
  {
    "natural-language": "Find cities with a population of at most 380,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 380000"
  },
  {
    "natural-language": "Find cities with a population of at most 308,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 308000"
  },
  {
    "natural-language": "Find cities with a population of at most 345,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 345000"
  },
  {
    "natural-language": "Find cities with a population of at most 340,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 340005"
  },
  {
    "natural-language": "Find cities with a population of at most 350,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 350206"
  },
  {
    "natural-language": "Find cities with a population of at most 347,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 347903"
  },
  {
    "natural-language": "Find cities with a population of at most 316,399 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 316399"
  },
  {
    "natural-language": "Find cities with a population of at most 320,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 320712"
  },
  {
    "natural-language": "Find cities with a population of at most 222,222 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 222222"
  },
  {
    "natural-language": "Find cities with a population of at most 255,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 255000"
  },
  {
    "natural-language": "Find cities with a population of at most 290,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 290000"
  },
  {
    "natural-language": "Find cities with a population of at most 280,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 280000"
  },
  {
    "natural-language": "Find cities with a population of at most 208,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 208000"
  },
  {
    "natural-language": "Find cities with a population of at most 245,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 245000"
  },
  {
    "natural-language": "Find cities with a population of at most 240,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 240005"
  },
  {
    "natural-language": "Find cities with a population of at most 250,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 250206"
  },
  {
    "natural-language": "Find cities with a population of at most 247,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 247903"
  },
  {
    "natural-language": "Find cities with a population of at most 216,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 216299"
  },
  {
    "natural-language": "Find cities with a population of at most 220,712 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 220712"
  },
  {
    "natural-language": "Find cities with a population of at most 468,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 468000"
  },
  {
    "natural-language": "Find cities with a population of at most 444,444 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 444444"
  },
  {
    "natural-language": "Find cities with a population of at most 455,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 455000"
  },
  {
    "natural-language": "Find cities with a population of at most 490,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 490000"
  },
  {
    "natural-language": "Find cities with a population of at most 480,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 480000"
  },
  {
    "natural-language": "Find cities with a population of at most 408,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 408000"
  },
  {
    "natural-language": "Find cities with a population of at most 445,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 445000"
  },
  {
    "natural-language": "Find cities with a population of at most 440,005 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 440005"
  },
  {
    "natural-language": "Find cities with a population of at most 450,206 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 450206"
  },
  {
    "natural-language": "Find cities with a population of at most 447,903 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 447903"
  },
  {
    "natural-language": "Find cities with a population of at most 416,299 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 416299"
  },
  {
    "natural-language": "Find cities with a population of at most 420,714 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 420714"
  },
  {
    "natural-language": "Find cities with a population of at most 150,000 people",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population <= 150000"
  },
  {
    "natural-language": "Find cities and order by population, descending",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY population DESC"
  },
  {
    "natural-language": "Find cities and order by size, descending",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY ST_Area(boundary) DESC"
  },
  {
    "natural-language": "Find cities and order by area, descending",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY ST_Area(boundary) DESC"
  },  
  # Find cities by matching criteria around buildings ( 1 - 20)
  {
    "natural-language": "Find cities that contain at least one building that is owned by an individual",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least two buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least three buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least four buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least five buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least six buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least seven buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least eight buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least nine buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least ten buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least eleven buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least twelve buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least thirteen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least fourteen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least fifteen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least sixteen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least seventeen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least eighteen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least nineteen buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least twenty buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain at least 1 building that is owned by an individual",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least 2 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least 3 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least 4 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least 5 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least 6 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least 7 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least 8 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least 9 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least 10 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least 11 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least 12 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least 13 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least 14 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least 15 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least 16 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least 17 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least 18 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least 19 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least 20 buildings that are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY c.id HAVING COUNT(b.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain at least one building that is owned by a group",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least two buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least three buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least four buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least five buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least six buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least seven buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least eight buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least nine buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least ten buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least eleven buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least twelve buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least thirteen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least fourteen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least fifteen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least sixteen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least seventeen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least eighteen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least nineteen buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least twenty buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain at least 1 building that is owned by an individual",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least 2 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least 3 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least 4 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least 5 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least 6 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least 7 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least 8 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least 9 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least 10 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least 11 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least 12 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least 13 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least 14 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least 15 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least 16 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least 17 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least 18 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least 19 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least 20 buildings that are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY c.id HAVING COUNT(b.id) >= 20"
  },
  {
    "natural-language": "Find cities where the majority of buildings are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING SUM(CASE WHEN o.is_group = FALSE THEN 1 ELSE 0 END) > SUM(CASE WHEN o.is_group = TRUE THEN 1 ELSE 0 END)"
  },
  {
    "natural-language": "Find cities where the minority of buildings are owned by individuals",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING SUM(CASE WHEN o.is_group = TRUE THEN 1 ELSE 0 END) > SUM(CASE WHEN o.is_group = FALSE THEN 1 ELSE 0 END)"
  },
  {
    "natural-language": "Find cities where the majority of buildings are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING COUNT(CASE WHEN o.is_group = TRUE THEN 1 END) > COUNT(CASE WHEN o.is_group = FALSE THEN 1 END)"
  },
  {
    "natural-language": "Find cities where the minority of buildings are owned by groups",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) JOIN owning_entities o ON b.owning_entity_id = o.id GROUP BY c.id HAVING COUNT(CASE WHEN o.is_group = FALSE THEN 1 END) > COUNT(CASE WHEN o.is_group = TRUE THEN 1 END)"
  },
  {
    "natural-language": "Find the city with the most buildings",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) GROUP BY c.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the least buildings",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN buildings b ON ST_Within(b.location, c.boundary) GROUP BY c.id ORDER BY COUNT(b.id) ASC LIMIT 1"
  },

  # Find cities by matching criteria around number of parks (1 - 20)
  {
    "natural-language": "Find the city with the greatest number of parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id ORDER BY COUNT(p.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest number of parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id ORDER BY COUNT(p.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find cities with no parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c WHERE NOT EXISTS (SELECT 1 FROM parks p WHERE ST_Within(p.boundary, c.boundary))"
  },
  {
    "natural-language": "Find cities with at least one park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 1 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least two parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 2 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least three parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 3 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least four parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 4 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least five parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 5 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least six parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 6 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least seven parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 7 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least eight parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 8 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least nine parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 9 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least ten parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 10 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least eleven parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 11 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least twelve parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 12 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least thirteen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 13 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least fourteen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 14 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least fifteen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 15 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least sixteen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 16 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least seventeen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 17 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least eighteen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 18 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least nineteen parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 19 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least twenty parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 20 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 1 park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 1 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 2 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 2 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 3 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 3 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 4 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 4 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 5 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 5 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 6 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 6 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 7 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 7 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 8 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 8 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 9 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 9 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 10 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 10 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 11 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 11 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 12 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 12 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 13 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 13 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 14 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 14 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 15 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 15 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 16 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 16 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 17 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 17 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 18 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 18 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 19 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 19 ORDER BY COUNT(p.id)"
  },
  {
    "natural-language": "Find cities with at least 20 parks",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING COUNT(p.id) >= 20 ORDER BY COUNT(p.id)"
  },

  # Find cities by matching criteria around park area (1 - 10)
  {
    "natural-language": "Find all cities that contain at least one square kilometer of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 1000"
  },
  {
    "natural-language": "Find all cities that contain at least two square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 2000"
  },
  {
    "natural-language": "Find all cities that contain at least three square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 3000"
  },
  {
    "natural-language": "Find all cities that contain at least four square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 4000"
  },
  {
    "natural-language": "Find all cities that contain at least five square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 5000"
  },
  {
    "natural-language": "Find all cities that contain at least six square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 6000"
  },
  {
    "natural-language": "Find all cities that contain at least seven square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 7000"
  },
  {
    "natural-language": "Find all cities that contain at least eight square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 8000"
  },
  {
    "natural-language": "Find all cities that contain at least nine square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 9000"
  },
  {
    "natural-language": "Find all cities that contain at least ten square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 10000"
  },
  {
    "natural-language": "Find all cities that contain at least 1 square kilometer of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 1000"
  },
  {
    "natural-language": "Find all cities that contain at least 2 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 2000"
  },
  {
    "natural-language": "Find all cities that contain at least 3 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 3000"
  },
  {
    "natural-language": "Find all cities that contain at least 4 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 4000"
  },
  {
    "natural-language": "Find all cities that contain at least 5 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 5000"
  },
  {
    "natural-language": "Find all cities that contain at least 6 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 6000"
  },
  {
    "natural-language": "Find all cities that contain at least 7 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 7000"
  },
  {
    "natural-language": "Find all cities that contain at least 8 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 8000"
  },
  {
    "natural-language": "Find all cities that contain at least 9 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 9000"
  },
  {
    "natural-language": "Find all cities that contain at least 10 square kilometers of park",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary, SUM(ST_Area(ST_Transform(p.boundary, 3857))) AS total_area FROM cities c JOIN parks p ON ST_Within(p.boundary, c.boundary) GROUP BY c.id HAVING SUM(ST_Area(ST_Transform(p.boundary, 3857))) >= 10000"
  },
 
  # Find cities by matching criteria around number of roads (1 - 20)
  {
    "natural-language": "Find the city with the fewest number roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the greatest number of roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find cities that contain at least one entire road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least two entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least three entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least four entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least five entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least six entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least seven entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least eight entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least nine entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least ten entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least eleven entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least twelve entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least thirteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least fourteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least fifteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least sixteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least seventeen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least eighteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least nineteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least twenty entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that fully contain at least one road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that fully contain at least two roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that fully contain at least three roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that fully contain at least four roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that fully contain at least five roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that fully contain at least six roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that fully contain at least seven roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that fully contain at least eight roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that fully contain at least nine roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that fully contain at least ten roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that fully contain at least eleven roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that fully contain at least twelve roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that fully contain at least thirteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that fully contain at least fourteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that fully contain at least fifteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that fully contain at least sixteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that fully contain at least seventeen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that fully contain at least eighteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that fully contain at least nineteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that fully contain at least twenty roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },

  {
    "natural-language": "Find cities that contain a part of at least one road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain a part of at least two roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain a part of at least three roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain a part of at least four roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain a part of at least five roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain a part of at least six roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain a part of at least seven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain a part of at least eight roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain a part of at least nine roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain a part of at least ten roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain a part of at least eleven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain a part of at least twelve roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain a part of at least thirteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain a part of at least fourteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain a part of at least fifteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain a part of at least sixteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain a part of at least seventeen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain a part of at least eighteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain a part of at least nineteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain a part of at least twenty roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain part of at least one road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain part of at least two roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain part of at least three roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain part of at least four roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain part of at least five roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain part of at least six roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain part of at least seven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain part of at least eight roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain part of at least nine roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain part of at least ten roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain part of at least eleven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain part of at least twelve roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain part of at least thirteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain part of at least fourteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain part of at least fifteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain part of at least sixteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain part of at least seventeen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain part of at least eighteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain part of at least nineteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain part of at least twenty roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain a section of at least one road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain a section of at least two roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain a section of at least three roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain a section of at least four roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain a section of at least five roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain a section of at least six roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain a section of at least seven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain a section of at least eight roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain a section of at least nine roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain a section of at least ten roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain a section of at least eleven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain a section of at least twelve roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain a section of at least thirteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain a section of at least fourteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain a section of at least fifteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain a section of at least sixteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain a section of at least seventeen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain a section of at least eighteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain a section of at least nineteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain a section of at least twenty roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain at least 1 entire road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least 2 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least 3 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least 4 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least 5 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least 6 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least 7 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least 8 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least 9 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least 10 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least 11 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least 12 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least 13 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least 14 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least 15 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least 16 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least 17 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least 18 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least 19 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least 20 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that fully contain at least 1 road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that fully contain at least 2 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that fully contain at least 3 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that fully contain at least 4 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that fully contain at least 5 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that fully contain at least 6 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that fully contain at least 7 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that fully contain at least 8 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that fully contain at least 9 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that fully contain at least 10 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that fully contain at least 11 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that fully contain at least 12 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that fully contain at least 13 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that fully contain at least 14 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that fully contain at least 15 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that fully contain at least 16 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that fully contain at least 17 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that fully contain at least 18 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that fully contain at least 19 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that fully contain at least 20 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain a part of at least 1 road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain a part of at least 2 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain a part of at least 3 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain a part of at least 4 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain a part of at least 5 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain a part of at least 6 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain a part of at least 7 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain a part of at least 8 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain a part of at least 9 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain a part of at least 10 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain a part of at least 11 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain a part of at least 12 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain a part of at least 13 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain a part of at least 14 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain a part of at least 15 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain a part of at least 16 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain a part of at least 17 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain a part of at least 18 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain a part of at least 19 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain a part of at least 20 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain part of at least 1 road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain part of at least 2 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain part of at least 3 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain part of at least 4 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain part of at least 5 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain part of at least 6 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain part of at least 7 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain part of at least 8 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain part of at least 9 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain part of at least 10 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain part of at least 11 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain part of at least 12 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain part of at least 13 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain part of at least 14 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain part of at least 15 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain part of at least 16 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain part of at least 17 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain part of at least 18 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain part of at least 19 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain part of at least 20 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain a section of at least 1 road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 1"
  },
  {
    "natural-language": "Find cities that contain a section of at least 2 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 2"
  },
  {
    "natural-language": "Find cities that contain a section of at least 3 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 3"
  },
  {
    "natural-language": "Find cities that contain a section of at least 4 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 4"
  },
  {
    "natural-language": "Find cities that contain a section of at least 5 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 5"
  },
  {
    "natural-language": "Find cities that contain a section of at least 6 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 6"
  },
  {
    "natural-language": "Find cities that contain a section of at least 7 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 7"
  },
  {
    "natural-language": "Find cities that contain a section of at least 8 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 8"
  },
  {
    "natural-language": "Find cities that contain a section of at least 9 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 9"
  },
  {
    "natural-language": "Find cities that contain a section of at least 10 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 10"
  },
  {
    "natural-language": "Find cities that contain a section of at least 11 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 11"
  },
  {
    "natural-language": "Find cities that contain a section of at least 12 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 12"
  },
  {
    "natural-language": "Find cities that contain a section of at least 13 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 13"
  },
  {
    "natural-language": "Find cities that contain a section of at least 14 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 14"
  },
  {
    "natural-language": "Find cities that contain a section of at least 15 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 15"
  },
  {
    "natural-language": "Find cities that contain a section of at least 16 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 16"
  },
  {
    "natural-language": "Find cities that contain a section of at least 17 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 17"
  },
  {
    "natural-language": "Find cities that contain a section of at least 18 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 18"
  },
  {
    "natural-language": "Find cities that contain a section of at least 19 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 19"
  },
  {
    "natural-language": "Find cities that contain a section of at least 20 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) >= 20"
  },
  {
    "natural-language": "Find cities that contain at most one entire road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain at most two entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain at most three entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain at most four entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain at most five entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain at most six entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain at most seven entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain at most eight entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain at most nine entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain at most ten entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain at most eleven entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain at most twelve entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain at most thirteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain at most fourteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain at most fifteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain at most sixteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain at most seventeen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain at most eighteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain at most nineteen entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain at most twenty entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that fully contain at most one road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that fully contain at most two roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that fully contain at most three roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that fully contain at most four roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that fully contain at most five roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that fully contain at most six roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that fully contain at most seven roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that fully contain at most eight roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that fully contain at most nine roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that fully contain at most ten roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that fully contain at most eleven roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that fully contain at most twelve roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that fully contain at most thirteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that fully contain at most fourteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that fully contain at most fifteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that fully contain at most sixteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that fully contain at most seventeen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that fully contain at most eighteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that fully contain at most nineteen roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that fully contain at most twenty roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain a part of at most one road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain a part of at most two roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain a part of at most three roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain a part of at most four roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain a part of at most five roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain a part of at most six roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain a part of at most seven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain a part of at most eight roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain a part of at most nine roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain a part of at most ten roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain a part of at most eleven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain a part of at most twelve roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain a part of at most thirteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain a part of at most fourteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain a part of at most fifteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain a part of at most sixteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain a part of at most seventeen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain a part of at most eighteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain a part of at most nineteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain a part of at most twenty roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain part of at most one road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain part of at most two roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain part of at most three roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain part of at most four roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain part of at most five roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain part of at most six roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain part of at most seven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain part of at most eight roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain part of at most nine roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain part of at most ten roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain part of at most eleven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain part of at most twelve roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain part of at most thirteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain part of at most fourteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain part of at most fifteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain part of at most sixteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain part of at most seventeen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain part of at most eighteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain part of at most nineteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain part of at most twenty roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain a section of at most one road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain a section of at most two roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain a section of at most three roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain a section of at most four roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain a section of at most five roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain a section of at most six roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain a section of at most seven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain a section of at most eight roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain a section of at most nine roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain a section of at most ten roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain a section of at most eleven roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain a section of at most twelve roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain a section of at most thirteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain a section of at most fourteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain a section of at most fifteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain a section of at most sixteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain a section of at most seventeen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain a section of at most eighteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain a section of at most nineteen roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain a section of at most twenty roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain at most 1 entire road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain at most 2 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain at most 3 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain at most 4 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain at most 5 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain at most 6 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain at most 7 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain at most 8 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain at most 9 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain at most 10 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain at most 11 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain at most 12 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain at most 13 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain at most 14 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain at most 15 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain at most 16 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain at most 17 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain at most 18 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain at most 19 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain at most 20 entire roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that fully contain at most 1 road",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that fully contain at most 2 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that fully contain at most 3 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that fully contain at most 4 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that fully contain at most 5 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that fully contain at most 6 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that fully contain at most 7 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that fully contain at most 8 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that fully contain at most 9 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that fully contain at most 10 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that fully contain at most 11 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that fully contain at most 12 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that fully contain at most 13 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that fully contain at most 14 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that fully contain at most 15 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that fully contain at most 16 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that fully contain at most 17 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that fully contain at most 18 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that fully contain at most 19 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that fully contain at most 20 roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Contains(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain a part of at most 1 road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain a part of at most 2 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain a part of at most 3 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain a part of at most 4 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain a part of at most 5 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain a part of at most 6 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain a part of at most 7 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain a part of at most 8 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain a part of at most 9 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain a part of at most 10 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain a part of at most 11 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain a part of at most 12 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain a part of at most 13 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain a part of at most 14 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain a part of at most 15 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain a part of at most 16 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain a part of at most 17 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain a part of at most 18 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain a part of at most 19 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain a part of at most 20 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain part of at most 1 road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain part of at most 2 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain part of at most 3 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain part of at most 4 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain part of at most 5 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain part of at most 6 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain part of at most 7 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain part of at most 8 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain part of at most 9 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain part of at most 10 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain part of at most 11 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain part of at most 12 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain part of at most 13 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain part of at most 14 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain part of at most 15 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain part of at most 16 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain part of at most 17 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain part of at most 18 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain part of at most 19 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain part of at most 20 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },
  {
    "natural-language": "Find cities that contain a section of at most 1 road",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 1"
  },
  {
    "natural-language": "Find cities that contain a section of at most 2 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 2"
  },
  {
    "natural-language": "Find cities that contain a section of at most 3 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 3"
  },
  {
    "natural-language": "Find cities that contain a section of at most 4 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 4"
  },
  {
    "natural-language": "Find cities that contain a section of at most 5 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 5"
  },
  {
    "natural-language": "Find cities that contain a section of at most 6 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 6"
  },
  {
    "natural-language": "Find cities that contain a section of at most 7 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 7"
  },
  {
    "natural-language": "Find cities that contain a section of at most 8 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 8"
  },
  {
    "natural-language": "Find cities that contain a section of at most 9 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 9"
  },
  {
    "natural-language": "Find cities that contain a section of at most 10 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 10"
  },
  {
    "natural-language": "Find cities that contain a section of at most 11 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 11"
  },
  {
    "natural-language": "Find cities that contain a section of at most 12 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 12"
  },
  {
    "natural-language": "Find cities that contain a section of at most 13 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 13"
  },
  {
    "natural-language": "Find cities that contain a section of at most 14 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 14"
  },
  {
    "natural-language": "Find cities that contain a section of at most 15 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 15"
  },
  {
    "natural-language": "Find cities that contain a section of at most 16 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 16"
  },
  {
    "natural-language": "Find cities that contain a section of at most 17 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 17"
  },
  {
    "natural-language": "Find cities that contain a section of at most 18 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 18"
  },
  {
    "natural-language": "Find cities that contain a section of at most 19 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 19"
  },
  {
    "natural-language": "Find cities that contain a section of at most 20 roads",
    "sql": "SELECT c.id, c.name, COUNT(r.id) AS road_count FROM cities c JOIN roads r ON ST_Intersects(c.boundary, r.route) GROUP BY c.id, c.name HAVING COUNT(r.id) <= 20"
  },

  # Find cities by matching criteria around intersecting roads (1 - 20)
  {
    "natural-language": "Find the city with the fewest number of intersecting roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(DISTINCT r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the greatest number of intersecting roads",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) GROUP BY c.id ORDER BY COUNT(DISTINCT r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find cities that contain at least one intersection",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least two intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least three intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least four intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least five intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least six intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least seven intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least eight intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least nine intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least ten intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least eleven intersection",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least twelve intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least thirteen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least fourteen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least fifteen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least sixteen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least seventeen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least eighteen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least nineteen intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least twenty intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 20"
  },
  {
    "natural-language": "Find cities that contain at least 1 intersection",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 1"
  },
  {
    "natural-language": "Find cities that contain at least 2 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 2"
  },
  {
    "natural-language": "Find cities that contain at least 3 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 3"
  },
  {
    "natural-language": "Find cities that contain at least 4 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 4"
  },
  {
    "natural-language": "Find cities that contain at least 5 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 5"
  },
  {
    "natural-language": "Find cities that contain at least 6 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 6"
  },
  {
    "natural-language": "Find cities that contain at least 7 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 7"
  },
  {
    "natural-language": "Find cities that contain at least 8 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 8"
  },
  {
    "natural-language": "Find cities that contain at least 9 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 9"
  },
  {
    "natural-language": "Find cities that contain at least 10 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 10"
  },
  {
    "natural-language": "Find cities that contain at least 11 intersection",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 11"
  },
  {
    "natural-language": "Find cities that contain at least 12 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 12"
  },
  {
    "natural-language": "Find cities that contain at least 13 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 13"
  },
  {
    "natural-language": "Find cities that contain at least 14 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 14"
  },
  {
    "natural-language": "Find cities that contain at least 15 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 15"
  },
  {
    "natural-language": "Find cities that contain at least 16 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 16"
  },
  {
    "natural-language": "Find cities that contain at least 17 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 17"
  },
  {
    "natural-language": "Find cities that contain at least 18 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 18"
  },
  {
    "natural-language": "Find cities that contain at least 19 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 19"
  },
  {
    "natural-language": "Find cities that contain at least 20 intersections",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE ST_NumGeometries(boundary) >= 20"
  },

  # Find cities with an area greater than (1 - 200 sq km)
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

  # Find cities with an area of at least (1 - 200 sq km)
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

  # Find cities with an area less than (1 - 200 sq km)
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

  # Find cities with an area of at most (1 - 200 sq km)
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

  # Find cities by matching criteria around roads and population
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 10000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 10000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 20000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 20000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 30000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 30000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 40000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 40000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 45000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 45000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 50000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 50000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 55000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 55000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 60000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 60000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 65000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 65000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 70000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 70000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 75000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 75000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 80000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 80000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 85000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 85000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 90000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 90000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 95000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 95000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 100000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 100000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 110000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 110000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 120000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 120000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 150000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 150000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 180000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 180000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 200000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 200000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 250000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 250000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 300000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 300000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than 400000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 400000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 10000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 20000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than thirty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 30000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than forty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 40000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than forty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 45000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 50000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than fifty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 55000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than sixty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 60000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than sixty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 65000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than seventy thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 70000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than seventy five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 75000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 80000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than eighty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 85000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than ninety thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 90000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than ninety five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 95000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than one hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 100000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than one hundred ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 110000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than one hundred twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 120000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than one hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 150000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than one hundred eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 180000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than two hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 200000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than two hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 250000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than three hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 300000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population greater than four hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 400000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 10000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 10000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 20000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 20000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 30000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 30000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 40000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 40000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 45000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 45000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 50000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 50000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 55000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 55000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 60000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 60000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 65000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 65000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 70000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 70000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 75000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 75000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 80000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 80000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 85000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 85000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 90000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 90000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 95000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 95000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 100000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 110000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 110000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 120000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 120000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 150000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 150000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 180000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 180000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 200000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 200000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 250000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 250000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 300000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 300000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than 400000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 400000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 10000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 20000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than thirty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 30000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than forty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 40000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than forty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 45000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 50000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than fifty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 55000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than sixty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 60000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than sixty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 65000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than seventy thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 70000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than seventy five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 75000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 80000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than eighty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 85000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than ninety thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 90000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than ninety five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 95000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than one hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than one hundred ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 110000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than one hundred twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 120000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than one hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 150000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than one hundred eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 180000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than two hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 200000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than two hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 250000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than three hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 300000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the fewest roads and a population less than four hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 400000 GROUP BY c.id ORDER BY COUNT(r.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 10000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 10000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 20000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 20000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 30000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 30000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 40000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 40000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 45000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 45000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 50000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 50000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 55000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 55000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 60000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 60000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 65000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 65000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 70000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 70000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 75000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 75000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 80000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 80000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 85000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 85000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 90000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 90000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 95000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 95000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 100000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 100000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 110000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 110000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 120000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 120000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 150000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 150000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 180000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 180000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 200000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 200000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 250000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 250000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 300000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 300000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than 400000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 400000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 10000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 20000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than thirty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 30000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than forty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 40000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than forty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 45000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 50000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than fifty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 55000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than sixty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 60000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than sixty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 65000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than seventy thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 70000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than seventy five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 75000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 80000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than eighty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 85000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than ninety thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 90000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than ninety five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 95000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than one hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 100000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than one hundred ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 110000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than one hundred twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 120000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than one hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 150000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than one hundred eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 180000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than two hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 200000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than two hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 250000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than three hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 300000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population greater than four hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population > 400000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 10000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 10000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 20000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 20000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 30000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 30000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 40000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 40000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 45000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 45000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 50000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 50000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 55000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 55000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 60000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 60000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 65000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 65000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 70000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 70000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 75000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 75000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 80000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 80000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 85000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 85000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 90000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 90000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 95000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 95000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 100000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 110000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 110000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 120000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 120000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 150000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 150000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 180000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 180000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 200000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 200000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 250000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 250000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 300000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 300000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than 400000 people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 400000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 10000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 20000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than thirty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 30000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than forty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 40000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than forty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 45000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 50000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than fifty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 55000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than sixty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 60000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than sixty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 65000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than seventy thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 70000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than seventy five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 75000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 80000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than eighty five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 85000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than ninety thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 90000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than ninety five thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 95000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than one hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than one hundred ten thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 110000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than one hundred twenty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 120000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than one hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 150000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than one hundred eighty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 180000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than two hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 200000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than two hundred fifty thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 250000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than three hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 300000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the most roads and a population less than four hundred thousand people",
    "sql": "SELECT c.name, ST_AsGeoJSON(c.boundary) AS boundary FROM cities c JOIN roads r ON ST_Intersects(r.route, c.boundary) WHERE c.population < 400000 GROUP BY c.id ORDER BY COUNT(r.id) DESC LIMIT 1"
  },

  # Find cities by matching criteria around area and population TODO: Add queries
  {
    "natural-language": "Find the city with the smallest area and a population greater than 70,000",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 70000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than eighty thousand",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 80000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than 90000",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 90000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the city with the smallest area and a population greater than 100,000",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities WHERE population > 100000 ORDER BY ST_Area(boundary) ASC LIMIT 1"
  },

  # Find cities by matching criteria around area and roads TODO: Add queries


  # Northernmost city, southermost city, etc.
  {
    "natural-language": "Find the northernmost city",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY ST_YMax(boundary) DESC LIMIT 1"
  },
   {
    "natural-language": "Find the southernmost city",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY ST_YMin(boundary) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the easternmost city",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY ST_XMax(boundary) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the westernmost city",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM cities ORDER BY ST_XMin(boundary) ASC LIMIT 1"
  },

  # Roads
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads with at least one kilometer crossing within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326)) AND ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads that intersect at (-119.2700, 34.2600)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_SetSRID(ST_Point(-119.2700, 34.2600), 4326))"
  },
  {
    "natural-language": "Find roads that intersect at (-119.2650, 34.2400)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_SetSRID(ST_Point(-119.2650, 34.2400), 4326))"
  },
  {
    "natural-language": "Find roads that intersect at (-119.2700, 34.2600) or (-119.2450, 34.2700)",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, ST_SetSRID(ST_Point(-119.2700, 34.2600), 4326)) OR ST_Intersects(route, ST_SetSRID(ST_Point(-119.2450, 34.2700), 4326))"
  },
  {
    "natural-language": "Find roads that span at least four kilometers through a city with a population of at least one hundred thousand",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads with at least 2 km through a city with a population less than one hundred thousand",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least one kilometer through a city with a population of at least one hundred thousand",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads with at least 1 km through a city with a population less than one hundred thousand",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads within two kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(r.route, p.boundary, 2000)"
  },
  {
    "natural-language": "Find roads that go through a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_Intersects(r.route, p.boundary)"
  },
  {
    "natural-language": "Find roads that are longer than 4 km",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
  },
  {
    "natural-language": "Find roads that are at least 4 km",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
  },
  {
    "natural-language": "Find roads that are shorter than 4 km",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
  },
  {
    "natural-language": "Find roads that are longer than two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
  },
  {
    "natural-language": "Find roads that are at least two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
  },
  {
    "natural-language": "Find roads that are shorter than two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
  },
  {
    "natural-language": "Find roads that are longer than five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
  },
  {
    "natural-language": "Find roads that are at least five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
  },
  {
    "natural-language": "Find roads that are shorter than five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
  },
  {
    "natural-language": "Find roads that are longer than 6 km",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
  },
  {
    "natural-language": "Find roads that are at least 6 km",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
  },
  {
    "natural-language": "Find roads that are shorter than 6 km",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
  },
  {
    "natural-language": "Find the longest road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ventura')) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road in Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ojai')) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Oxnard",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Oxnard')) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road in Camarillo",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Camarillo')) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within the busiest city",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MAX(population) FROM cities) ORDER BY ST_Length(r.route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road in the quietest city",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MIN(population) FROM cities) ORDER BY ST_Length(r.route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road in the busiest city",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MAX(population) FROM cities) ORDER BY ST_Length(r.route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within the quietest city",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) WHERE c.population = (SELECT MIN(population) FROM cities) ORDER BY ST_Length(r.route) ASC LIMIT 1"
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
    "natural-language": "Find roads in Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ojai'))"
  },
  {
    "natural-language": "Find all roads in Camarillo",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Camarillo'))"
  },
  {
    "natural-language": "Find roads in Oxnard",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Oxnard'))"
  },
  {
    "natural-language": "Find roads in Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(route, (SELECT boundary FROM cities WHERE name = 'Ventura'))"
  },
  {
    "natural-language": "Find all roads that have multiple buildings that are owned by the same group",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY r.id HAVING COUNT(DISTINCT b.id) > 1"
  },
  {
    "natural-language": "Find all roads that have buildings that are not owned by groups",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE"
  },
  {
    "natural-language": "Find the road with the most buildings",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) GROUP BY r.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the road with the least buildings",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) GROUP BY r.id ORDER BY COUNT(b.id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the road with the most individual owners",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY r.id ORDER BY COUNT(DISTINCT b.owning_entity_id) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the road with the least individual owners",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(b.location, r.route) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY r.id ORDER BY COUNT(DISTINCT b.owning_entity_id) ASC LIMIT 1"
  },
  {
    "natural-language": "Find roads with no buildings",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE NOT EXISTS (SELECT 1 FROM buildings b WHERE ST_Intersects(b.location, roads.route))"
  },
  {
    "natural-language": "Find the easternmost road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_X(ST_Transform(ST_StartPoint(route), 4326)) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the westernmost road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_X(ST_Transform(ST_StartPoint(route), 4326)) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the southernmost road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_Y(ST_Transform(ST_StartPoint(route), 4326)) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the norhternmost road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_Y(ST_Transform(ST_StartPoint(route), 4326)) DESC LIMIT 1"
  },

  {
    "natural-language": "Find parks within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(p.boundary, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find parks within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(p.boundary, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
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
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) >= 2000"
  },
  {
    "natural-language": "Find parks containing a road that is at least 5 km",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) >= 5000"
  },
  {
    "natural-language": "Find parks containing a road that is less than 4 km",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) < 4000"
  },
  {
    "natural-language": "Find parks containing a road that is at least nineteen kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) >= 19000"
  },
  {
    "natural-language": "Find parks containing a road that is less than three hundred kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) < 300000"
  },
  {
    "natural-language": "Find parks containing a road that is shorter than five kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) < 5000"
  },
  {
    "natural-language": "Find parks containing a road that is greater than six kilometers",
    "sql": "SELECT p.id, p.name FROM parks p JOIN roads r ON ST_Contains(p.boundary, r.route) WHERE ST_Length(r.route::geography) >= 6000"
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
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Ventura' LIMIT 1))"
  },
  {
    "natural-language": "Find all parks in Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Ojai' LIMIT 1))"
  },
  {
    "natural-language": "Find parks in Oxnard",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Oxnard' LIMIT 1))"
  },
  {
    "natural-language": "Find all parks in Camarillo",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Camarillo' LIMIT 1))"
  },
  {
    "natural-language": "Find parks within a city that has a population of less than two hundred thousand",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population < 200000"
  },
  {
    "natural-language": "Find parks within a city that has a population of less than 300,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population < 300000"
  },
  {
    "natural-language": "Find parks within a city that has a population of at least one hundred thousand",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population >= 100000"
  },
  {
    "natural-language": "Find parks within a city that has a population of at least 50,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population >= 50000"
  },
  {
    "natural-language": "Find parks within a city that has a population greater than ninety thousand",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population > 90000"
  },
  {
    "natural-language": "Find parks within a city that has a population greater than 115,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population > 115000"
  },
  {
    "natural-language": "Find parks in a city with a population that is greater than 200,000",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population > 200000"
  },
  {
    "natural-language": "Find parks within the city that has the highest population",
    "sql": "SELECT p.name, ST_AsGeoJSON(p.boundary) AS boundary FROM parks p JOIN cities c ON ST_Within(p.boundary, c.boundary) WHERE c.population = (SELECT MAX(population) FROM cities)"
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
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE NOT EXISTS (SELECT 1 FROM roads r WHERE ST_Intersects(p.boundary, r.route))"
  },
  {
    "natural-language": "Find all parks with at least one road running through them",
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE EXISTS (SELECT 1 FROM roads r WHERE ST_Intersects(p.boundary, r.route))"
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
    "sql": "SELECT name, ST_AsGeoJSON(boundary) AS boundary FROM parks p WHERE NOT ST_Within(p.boundary, (SELECT boundary FROM cities WHERE name = 'Ojai' LIMIT 1))"
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
    "natural-language": "Find buildings within the area bound by (-119.3047, 34.2805), (-119.2280, 34.2900), (-119.2265, 34.2400), (-119.2660, 34.2100), (-119.2940, 34.2385), and (-119.3047, 34.2805)",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.3047 34.2805, -119.2280 34.2900, -119.2265 34.2400, -119.2660 34.2100, -119.2940 34.2385, -119.3047 34.2805))', 4326))"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.3120, 34.4660), (-119.2630, 34.4720), (-119.2410, 34.4450), (-119.2690, 34.4260), (-119.2980, 34.4350), and (-119.3120, 34.4660)",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.3120 34.4660, -119.2630 34.4720, -119.2410 34.4450, -119.2690 34.4260, -119.2980 34.4350, -119.3120 34.4660))', 4326))"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.2450, 34.2320), (-119.1720, 34.2470), (-119.1540, 34.1970), (-119.2000, 34.1610), (-119.2370, 34.1760), and (-119.2450, 34.2320)",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.2450 34.2320, -119.1720 34.2470, -119.1540 34.1970, -119.2000 34.1610, -119.2370 34.1760, -119.2450 34.2320))', 4326))"
  },
  {
    "natural-language": "Find buildings within the area bound by (-119.0610, 34.2360), (-119.0170, 34.2370), (-118.9870, 34.2110), (-119.0110, 34.1850), (-119.0480, 34.1980), and (-119.0610, 34.2360)",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings b WHERE ST_Within(b.location, ST_GeomFromText('POLYGON((-119.0610 34.2360, -119.0170 34.2370, -118.9870 34.2110, -119.0110 34.1850, -119.0480 34.1980, -119.0610 34.2360))', 4326))"
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
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(r1.route, r2.route)), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, ST_AsGeoJSON(b.location) AS location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 2000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings within three kilometers of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(r1.route, r2.route)), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, ST_AsGeoJSON(b.location) AS location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 3000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
  },
  {
    "natural-language": "Find buildings within 4 km of any intersection",
    "sql": "WITH road_intersections AS (SELECT r1.id AS road1_id, r2.id AS road2_id, ST_Intersection(r1.route, r2.route) AS intersection_point FROM roads r1, roads r2 WHERE r1.id < r2.id AND ST_Intersects(r1.route, r2.route)), buildings_near_intersection AS (SELECT b.id AS building_id, b.street_number, ST_AsGeoJSON(b.location) AS location, b.road_id, ST_Distance(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857)) AS distance_to_intersection_in_meters FROM buildings b JOIN road_intersections ri ON ST_DWithin(ST_Transform(b.location, 3857), ST_Transform(ri.intersection_point, 3857), 4000)) SELECT bi.building_id, bi.street_number, bi.location, bi.distance_to_intersection_in_meters FROM buildings_near_intersection bi ORDER BY bi.distance_to_intersection_in_meters"
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
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id IN (SELECT r.id FROM roads r JOIN cities c1 ON ST_Intersects(r.route, c1.boundary) JOIN cities c2 ON ST_Intersects(r.route, c2.boundary) WHERE c1.id != c2.id)"
  },
  {
    "natural-language": "Find buildings on any road that spans a single city",
    "sql": "SELECT street_number, ST_AsGeoJSON(location) AS location FROM buildings WHERE road_id IN (SELECT r.id FROM roads r JOIN cities c ON ST_Intersects(r.route, c.boundary) GROUP BY r.id HAVING COUNT(DISTINCT c.id) = 1)"
  },
  {
    "natural-language": "Find buildings within one kilometer of three or more roads",
    "sql": "SELECT b.street_number, ST_AsGeoJSON(b.location) AS location FROM buildings b JOIN roads r ON ST_DWithin(b.location, r.route, 1000) GROUP BY b.id HAVING COUNT(r.id) >= 3"
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