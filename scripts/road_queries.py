ROAD_QUERIES = [
  # Roads that intersect the point
  {
    "natural-language": "Find roads that intersect the point at (34.26507894016965, -119.26915119600329)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.26915119600329, 34.26507894016965), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.26805038529929, -119.19346984885188)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.19346984885188, 34.26805038529929), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.205300863788004, -119.15968622949566)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.15968622949566, 34.205300863788004), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.15048144761413, -118.82530359647478)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.82530359647478, 34.15048144761413), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.27681840840993, -119.28239503708643)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.28239503708643, 34.27681840840993), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.27950050473732, -119.30074932077764)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.30074932077764, 34.27950050473732), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.44886646434795, -119.22831722096964)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.22831722096964, 34.44886646434795), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.53002604716552, -119.26533992332458)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.26533992332458, 34.53002604716552), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.45257055531265, -119.24638941653723)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.24638941653723, 34.45257055531265), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.24177602838427, -119.02968049260319)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.02968049260319, 34.24177602838427), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.439684074273174, -119.28492364964283)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.28492364964283, 34.439684074273174), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.18975111144517, -119.17746610977325)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.17746610977325, 34.18975111144517), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.21889915415481, -119.15828061225007)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.15828061225007, 34.21889915415481), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.31517917389791, -118.92140871797332)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.92140871797332, 34.31517917389791), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.33723599152054, -119.08285389431659)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.08285389431659, 34.33723599152054), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.1733989602336, -119.17755588768398)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.17755588768398, 34.1733989602336), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.228386764809706, -119.20564564992891)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.20564564992891, 34.228386764809706), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.20842363831797, -119.20787290174934)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.20787290174934, 34.20842363831797), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.21887713094734, -119.06974938376794)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.06974938376794, 34.21887713094734), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.21825540312903, -119.0050446763035)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.0050446763035, 34.21825540312903), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.25845391618182, -118.9956221482037)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.9956221482037, 34.25845391618182), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.277880525598114, -119.16901264239188)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.16901264239188, 34.277880525598114), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.2399507078217, -118.984900625064)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.984900625064, 34.2399507078217), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.23737085361437, -119.04702605854114)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.04702605854114, 34.23737085361437), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.21726021957788, -119.03219326406408)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.03219326406408, 34.21726021957788), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.263748070745045, -119.01117298640172)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.01117298640172, 34.263748070745045), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.34075281014849, -119.1169716884745)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.1169716884745, 34.34075281014849), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.254514915995415, -119.19805080284718)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.19805080284718, 34.254514915995415), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.27304241845619, -119.24773771959808)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.24773771959808, 34.27304241845619), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.421111178370474, -119.30393945027923)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.30393945027923, 34.421111178370474), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.3987203504065, -118.92794303901464)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.92794303901464, 34.3987203504065), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.20620156077104, -119.14447740529138)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.14447740529138, 34.20620156077104), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.29604089933662, -118.84969638442925)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.84969638442925, 34.29604089933662), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.226535877457316, -119.05122706598993)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.05122706598993, 34.226535877457316), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.406807317194634, -118.9150133497815)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.9150133497815, 34.406807317194634), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.378780133551075, -118.91577347565624)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.91577347565624, 34.378780133551075), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.174751869554825, -119.23223160268773)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.23223160268773, 34.174751869554825), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.2211382359803, -119.18011543749964)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.18011543749964, 34.2211382359803), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.282560743353145, -118.67086097200007)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.67086097200007, 34.282560743353145), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.296036257545154, -118.84181714915407)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.84181714915407, 34.296036257545154), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.2064813707438, -119.16427752328438)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.16427752328438, 34.2064813707438), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.17894623977626, -118.87721671398127)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.87721671398127, 34.17894623977626), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.27890072051965, -118.9008783702391)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-118.9008783702391, 34.27890072051965), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.4556125227839, -119.2062038878815)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.2062038878815, 34.4556125227839), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.39584528195177, -119.45095793475929)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.45095793475929, 34.39584528195177), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.35270711075476, -119.30524405335618)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.30524405335618, 34.35270711075476), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.288990619588695, -119.29550947134541)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.29550947134541, 34.288990619588695), 4326))"
  },
  {
    "natural-language": "Find roads that intersect the point at (34.27282167316378, -119.09376425752103)",
    "sql": "SELECT name FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_SetSRID(ST_MakePoint(-119.09376425752103, 34.27282167316378), 4326))"
  },
  # Roads that are km long
  {
    "natural-language": "Find roads that are longer than half of a kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 500"
  },
  {
    "natural-language": "Find roads that are longer than one kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1000"
  },
  {
    "natural-language": "Find roads that are longer than one and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1500"
  },
  {
    "natural-language": "Find roads that are longer than two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
  },
  {
    "natural-language": "Find roads that are longer than two and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2500"
  },
  {
    "natural-language": "Find roads that are longer than three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3000"
  },
  {
    "natural-language": "Find roads that are longer than three and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3500"
  },
  {
    "natural-language": "Find roads that are longer than four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
  },
  {
    "natural-language": "Find roads that are longer than four and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4500"
  },
  {
    "natural-language": "Find roads that are longer than five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
  },
  {
    "natural-language": "Find roads that are longer than five and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5500"
  },
  {
    "natural-language": "Find roads that are longer than six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
  },
  {
    "natural-language": "Find roads that are longer than six and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6500"
  },
  {
    "natural-language": "Find roads that are longer than seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7000"
  },
  {
    "natural-language": "Find roads that are longer than seven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7500"
  },
  {
    "natural-language": "Find roads that are longer than eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8000"
  },
  {
    "natural-language": "Find roads that are longer than eight and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8500"
  },
  {
    "natural-language": "Find roads that are longer than nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9000"
  },
  {
    "natural-language": "Find roads that are longer than nine and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9500"
  },
  {
    "natural-language": "Find roads that are longer than ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10000"
  },
  {
    "natural-language": "Find roads that are longer than ten and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10500"
  },
  {
    "natural-language": "Find roads that are longer than eleven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 11000"
  },
  {
    "natural-language": "Find roads that are longer than eleven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 11500"
  },
  {
    "natural-language": "Find roads that are longer than twelve kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 12000"
  },
  {
    "natural-language": "Find roads that are longer than twelve and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 12500"
  },
  {
    "natural-language": "Find roads that are longer than thirteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 13000"
  },
  {
    "natural-language": "Find roads that are longer than thirteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 13500"
  },
  {
    "natural-language": "Find roads that are longer than fourteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 14000"
  },
  {
    "natural-language": "Find roads that are longer than fourteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 14500"
  },
  {
    "natural-language": "Find roads that are longer than fifteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 15000"
  },
  {
    "natural-language": "Find roads that are longer than fifteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 15500"
  },
  {
    "natural-language": "Find roads that are longer than sixteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 16000"
  },
  {
    "natural-language": "Find roads that are longer than sixteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 16500"
  },
  {
    "natural-language": "Find roads that are longer than seventeen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 17000"
  },
  {
    "natural-language": "Find roads that are longer than seventeen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 17500"
  },
  {
    "natural-language": "Find roads that are longer than eighteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 18000"
  },
  {
    "natural-language": "Find roads that are longer than eighteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 18500"
  },
  {
    "natural-language": "Find roads that are longer than nineteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 19000"
  },
  {
    "natural-language": "Find roads that are longer than nineteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 19500"
  },
  {
    "natural-language": "Find roads that are longer than twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20000"
  },
  {
    "natural-language": "Find roads that are longer than twenty and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20500"
  },
  {
    "natural-language": "Find roads that are longer than twenty one kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 21000"
  },
  {
    "natural-language": "Find roads that are longer than twenty two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 22000"
  },
  {
    "natural-language": "Find roads that are longer than twenty three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 23000"
  },
  {
    "natural-language": "Find roads that are longer than twenty four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 24000"
  },
  {
    "natural-language": "Find roads that are longer than twenty five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 25000"
  },
  {
    "natural-language": "Find roads that are longer than twenty six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 26000"
  },
  {
    "natural-language": "Find roads that are longer than twenty seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 27000"
  },
  {
    "natural-language": "Find roads that are longer than twenty eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 28000"
  },
  {
    "natural-language": "Find roads that are longer than twenty nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 29000"
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
    "natural-language": "Find roads that are longer than one hundred ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 110000"
  },
  {
    "natural-language": "Find roads that are longer than one hundred twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 120000"
  },
  {
    "natural-language": "Find roads that are longer than one hundred thirty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 130000"
  },
  {
    "natural-language": "Find roads that are longer than one hundred forty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 140000"
  },
  {
    "natural-language": "Find roads that are longer than one hundred fifty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 150000"
  },
  {
    "natural-language": "Find roads that are longer than two hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 200000"
  },
  {
    "natural-language": "Find roads that are longer than three hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 300000"
  },
  {
    "natural-language": "Find roads that are longer than .5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 500"
  },
  {
    "natural-language": "Find roads that are longer than 1 kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1000"
  },
  {
    "natural-language": "Find roads that are longer than 1.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 1500"
  },
  {
    "natural-language": "Find roads that are longer than 2 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2000"
  },
  {
    "natural-language": "Find roads that are longer than 2.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 2500"
  },
  {
    "natural-language": "Find roads that are longer than 3 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3000"
  },
  {
    "natural-language": "Find roads that are longer than 3.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 3500"
  },
  {
    "natural-language": "Find roads that are longer than 4 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4000"
  },
  {
    "natural-language": "Find roads that are longer than 4.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 4500"
  },
  {
    "natural-language": "Find roads that are longer than 5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5000"
  },
  {
    "natural-language": "Find roads that are longer than 5.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 5500"
  },
  {
    "natural-language": "Find roads that are longer than 6 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6000"
  },
  {
    "natural-language": "Find roads that are longer than 6.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 6500"
  },
  {
    "natural-language": "Find roads that are longer than 7 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7000"
  },
  {
    "natural-language": "Find roads that are longer than 7.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 7500"
  },
  {
    "natural-language": "Find roads that are longer than 8 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8000"
  },
  {
    "natural-language": "Find roads that are longer than 8.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 8500"
  },
  {
    "natural-language": "Find roads that are longer than 9 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9000"
  },
  {
    "natural-language": "Find roads that are longer than 9.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 9500"
  },
  {
    "natural-language": "Find roads that are longer than 10 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10000"
  },
  {
    "natural-language": "Find roads that are longer than 10.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 10500"
  },
  {
    "natural-language": "Find roads that are longer than 11 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 11000"
  },
  {
    "natural-language": "Find roads that are longer than 11.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 11500"
  },
  {
    "natural-language": "Find roads that are longer than 12 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 12000"
  },
  {
    "natural-language": "Find roads that are longer than 12.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 12500"
  },
  {
    "natural-language": "Find roads that are longer than 13 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 13000"
  },
  {
    "natural-language": "Find roads that are longer than 13.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 13500"
  },
  {
    "natural-language": "Find roads that are longer than 14 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 14000"
  },
  {
    "natural-language": "Find roads that are longer than 14.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 14500"
  },
  {
    "natural-language": "Find roads that are longer than 15 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 15000"
  },
  {
    "natural-language": "Find roads that are longer than 15.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 15500"
  },
  {
    "natural-language": "Find roads that are longer than 16 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 16000"
  },
  {
    "natural-language": "Find roads that are longer than 16.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 16500"
  },
  {
    "natural-language": "Find roads that are longer than 17 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 17000"
  },
  {
    "natural-language": "Find roads that are longer than 17.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 17500"
  },
  {
    "natural-language": "Find roads that are longer than 18 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 18000"
  },
  {
    "natural-language": "Find roads that are longer than 18.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 18500"
  },
  {
    "natural-language": "Find roads that are longer than 19 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 19000"
  },
  {
    "natural-language": "Find roads that are longer than 19.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 19500"
  },
  {
    "natural-language": "Find roads that are longer than 20 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20000"
  },
  {
    "natural-language": "Find roads that are longer than 20.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 20500"
  },
  {
    "natural-language": "Find roads that are longer than 21 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 21000"
  },
  {
    "natural-language": "Find roads that are longer than 22 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 22000"
  },
  {
    "natural-language": "Find roads that are longer than 23 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 23000"
  },
  {
    "natural-language": "Find roads that are longer than 24 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 24000"
  },
  {
    "natural-language": "Find roads that are longer than 25 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 25000"
  },
  {
    "natural-language": "Find roads that are longer than 26 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 26000"
  },
  {
    "natural-language": "Find roads that are longer than 27 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 27000"
  },
  {
    "natural-language": "Find roads that are longer than 28 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 28000"
  },
  {
    "natural-language": "Find roads that are longer than 29 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 29000"
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
    "natural-language": "Find roads that are longer than 100 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 100000"
  },
  {
    "natural-language": "Find roads that are longer than 110 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 110000"
  },
  {
    "natural-language": "Find roads that are longer than 120 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 120000"
  },
  {
    "natural-language": "Find roads that are longer than 130 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 130000"
  },
  {
    "natural-language": "Find roads that are longer than 140 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 140000"
  },
  {
    "natural-language": "Find roads that are longer than 150 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 150000"
  },
  {
    "natural-language": "Find roads that are longer than 200 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 200000"
  },
  {
    "natural-language": "Find roads that are longer than 300 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) > 300000"
  },
  {
    "natural-language": "Find roads that are at least half of a kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 500"
  },
  {
    "natural-language": "Find roads that are at least one kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads that are at least one and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1500"
  },
  {
    "natural-language": "Find roads that are at least two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
  },
  {
    "natural-language": "Find roads that are at least two and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2500"
  },
  {
    "natural-language": "Find roads that are at least three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3000"
  },
  {
    "natural-language": "Find roads that are at least three and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3500"
  },
  {
    "natural-language": "Find roads that are at least four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
  },
  {
    "natural-language": "Find roads that are at least four and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4500"
  },
  {
    "natural-language": "Find roads that are at least five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
  },
  {
    "natural-language": "Find roads that are at least five and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5500"
  },
  {
    "natural-language": "Find roads that are at least six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
  },
  {
    "natural-language": "Find roads that are at least six and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6500"
  },
  {
    "natural-language": "Find roads that are at least seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7000"
  },
  {
    "natural-language": "Find roads that are at least seven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7500"
  },
  {
    "natural-language": "Find roads that are at least eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8000"
  },
  {
    "natural-language": "Find roads that are at least eight and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8500"
  },
  {
    "natural-language": "Find roads that are at least nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9000"
  },
  {
    "natural-language": "Find roads that are at least nine and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9500"
  },
  {
    "natural-language": "Find roads that are at least ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10000"
  },
  {
    "natural-language": "Find roads that are at least ten and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10500"
  },
  {
    "natural-language": "Find roads that are at least eleven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 11000"
  },
  {
    "natural-language": "Find roads that are at least eleven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 11500"
  },
  {
    "natural-language": "Find roads that are at least twelve kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 12000"
  },
  {
    "natural-language": "Find roads that are at least twelve and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 12500"
  },
  {
    "natural-language": "Find roads that are at least thirteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 13000"
  },
  {
    "natural-language": "Find roads that are at least thirteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 13500"
  },
  {
    "natural-language": "Find roads that are at least fourteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 14000"
  },
  {
    "natural-language": "Find roads that are at least fourteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 14500"
  },
  {
    "natural-language": "Find roads that are at least fifteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 15000"
  },
  {
    "natural-language": "Find roads that are at least fifteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 15500"
  },
  {
    "natural-language": "Find roads that are at least sixteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 16000"
  },
  {
    "natural-language": "Find roads that are at least sixteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 16500"
  },
  {
    "natural-language": "Find roads that are at least seventeen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 17000"
  },
  {
    "natural-language": "Find roads that are at least seventeen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 17500"
  },
  {
    "natural-language": "Find roads that are at least eighteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 18000"
  },
  {
    "natural-language": "Find roads that are at least eighteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 18500"
  },
  {
    "natural-language": "Find roads that are at least nineteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 19000"
  },
  {
    "natural-language": "Find roads that are at least nineteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 19500"
  },
  {
    "natural-language": "Find roads that are at least twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20000"
  },
  {
    "natural-language": "Find roads that are at least twenty and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20500"
  },
  {
    "natural-language": "Find roads that are at least twenty one kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 21000"
  },
  {
    "natural-language": "Find roads that are at least twenty two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 22000"
  },
  {
    "natural-language": "Find roads that are at least twenty three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 23000"
  },
  {
    "natural-language": "Find roads that are at least twenty four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 24000"
  },
  {
    "natural-language": "Find roads that are at least twenty five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 25000"
  },
  {
    "natural-language": "Find roads that are at least twenty six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 26000"
  },
  {
    "natural-language": "Find roads that are at least twenty seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 27000"
  },
  {
    "natural-language": "Find roads that are at least twenty eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 28000"
  },
  {
    "natural-language": "Find roads that are at least twenty nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 29000"
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
    "natural-language": "Find roads that are at least one hundred ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 110000"
  },
  {
    "natural-language": "Find roads that are at least one hundred twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 120000"
  },
  {
    "natural-language": "Find roads that are at least one hundred thirty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 130000"
  },
  {
    "natural-language": "Find roads that are at least one hundred forty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 140000"
  },
  {
    "natural-language": "Find roads that are at least one hundred fifty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 150000"
  },
  {
    "natural-language": "Find roads that are at least two hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 200000"
  },
  {
    "natural-language": "Find roads that are at least three hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 300000"
  },
  {
    "natural-language": "Find roads that are at least .5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 500"
  },
  {
    "natural-language": "Find roads that are at least 1 kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1000"
  },
  {
    "natural-language": "Find roads that are at least 1.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 1500"
  },
  {
    "natural-language": "Find roads that are at least 2 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2000"
  },
  {
    "natural-language": "Find roads that are at least 2.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 2500"
  },
  {
    "natural-language": "Find roads that are at least 3 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3000"
  },
  {
    "natural-language": "Find roads that are at least 3.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 3500"
  },
  {
    "natural-language": "Find roads that are at least 4 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4000"
  },
  {
    "natural-language": "Find roads that are at least 4.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 4500"
  },
  {
    "natural-language": "Find roads that are at least 5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5000"
  },
  {
    "natural-language": "Find roads that are at least 5.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 5500"
  },
  {
    "natural-language": "Find roads that are at least 6 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6000"
  },
  {
    "natural-language": "Find roads that are at least 6.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 6500"
  },
  {
    "natural-language": "Find roads that are at least 7 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7000"
  },
  {
    "natural-language": "Find roads that are at least 7.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 7500"
  },
  {
    "natural-language": "Find roads that are at least 8 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8000"
  },
  {
    "natural-language": "Find roads that are at least 8.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 8500"
  },
  {
    "natural-language": "Find roads that are at least 9 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9000"
  },
  {
    "natural-language": "Find roads that are at least 9.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 9500"
  },
  {
    "natural-language": "Find roads that are at least 10 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10000"
  },
  {
    "natural-language": "Find roads that are at least 10.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 10500"
  },
  {
    "natural-language": "Find roads that are at least 11 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 11000"
  },
  {
    "natural-language": "Find roads that are at least 11.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 11500"
  },
  {
    "natural-language": "Find roads that are at least 12 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 12000"
  },
  {
    "natural-language": "Find roads that are at least 12.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 12500"
  },
  {
    "natural-language": "Find roads that are at least 13 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 13000"
  },
  {
    "natural-language": "Find roads that are at least 13.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 13500"
  },
  {
    "natural-language": "Find roads that are at least 14 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 14000"
  },
  {
    "natural-language": "Find roads that are at least 14.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 14500"
  },
  {
    "natural-language": "Find roads that are at least 15 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 15000"
  },
  {
    "natural-language": "Find roads that are at least 15.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 15500"
  },
  {
    "natural-language": "Find roads that are at least 16 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 16000"
  },
  {
    "natural-language": "Find roads that are at least 16.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 16500"
  },
  {
    "natural-language": "Find roads that are at least 17 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 17000"
  },
  {
    "natural-language": "Find roads that are at least 17.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 17500"
  },
  {
    "natural-language": "Find roads that are at least 18 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 18000"
  },
  {
    "natural-language": "Find roads that are at least 18.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 18500"
  },
  {
    "natural-language": "Find roads that are at least 19 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 19000"
  },
  {
    "natural-language": "Find roads that are at least 19.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 19500"
  },
  {
    "natural-language": "Find roads that are at least 20 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20000"
  },
  {
    "natural-language": "Find roads that are at least 20.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 20500"
  },
  {
    "natural-language": "Find roads that are at least 21 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 21000"
  },
  {
    "natural-language": "Find roads that are at least 22 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 22000"
  },
  {
    "natural-language": "Find roads that are at least 23 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 23000"
  },
  {
    "natural-language": "Find roads that are at least 24 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 24000"
  },
  {
    "natural-language": "Find roads that are at least 25 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 25000"
  },
  {
    "natural-language": "Find roads that are at least 26 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 26000"
  },
  {
    "natural-language": "Find roads that are at least 27 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 27000"
  },
  {
    "natural-language": "Find roads that are at least 28 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 28000"
  },
  {
    "natural-language": "Find roads that are at least 29 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 29000"
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
    "natural-language": "Find roads that are at least 110 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 110000"
  },
  {
    "natural-language": "Find roads that are at least 120 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 120000"
  },
  {
    "natural-language": "Find roads that are at least 130 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 130000"
  },
  {
    "natural-language": "Find roads that are at least 140 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 140000"
  },
  {
    "natural-language": "Find roads that are at least 150 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 150000"
  },
  {
    "natural-language": "Find roads that are at least 200 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 200000"
  },
  {
    "natural-language": "Find roads that are at least 300 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) >= 300000"
  },
  {
    "natural-language": "Find roads that are shorter than half of a kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 500"
  },
  {
    "natural-language": "Find roads that are shorter than one kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1000"
  },
  {
    "natural-language": "Find roads that are shorter than one and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1500"
  },
  {
    "natural-language": "Find roads that are shorter than two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
  },
  {
    "natural-language": "Find roads that are shorter than two and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2500"
  },
  {
    "natural-language": "Find roads that are shorter than three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3000"
  },
  {
    "natural-language": "Find roads that are shorter than three and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3500"
  },
  {
    "natural-language": "Find roads that are shorter than four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
  },
  {
    "natural-language": "Find roads that are shorter than four and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4500"
  },
  {
    "natural-language": "Find roads that are shorter than five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
  },
  {
    "natural-language": "Find roads that are shorter than five and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5500"
  },
  {
    "natural-language": "Find roads that are shorter than six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
  },
  {
    "natural-language": "Find roads that are shorter than six and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6500"
  },
  {
    "natural-language": "Find roads that are shorter than seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7000"
  },
  {
    "natural-language": "Find roads that are shorter than seven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7500"
  },
  {
    "natural-language": "Find roads that are shorter than eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8000"
  },
  {
    "natural-language": "Find roads that are shorter than eight and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8500"
  },
  {
    "natural-language": "Find roads that are shorter than nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9000"
  },
  {
    "natural-language": "Find roads that are shorter than nine and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9500"
  },
  {
    "natural-language": "Find roads that are shorter than ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10000"
  },
  {
    "natural-language": "Find roads that are shorter than ten and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10500"
  },
  {
    "natural-language": "Find roads that are shorter than eleven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 11000"
  },
  {
    "natural-language": "Find roads that are shorter than eleven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 11500"
  },
  {
    "natural-language": "Find roads that are shorter than twelve kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 12000"
  },
  {
    "natural-language": "Find roads that are shorter than twelve and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 12500"
  },
  {
    "natural-language": "Find roads that are shorter than thirteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 13000"
  },
  {
    "natural-language": "Find roads that are shorter than thirteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 13500"
  },
  {
    "natural-language": "Find roads that are shorter than fourteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 14000"
  },
  {
    "natural-language": "Find roads that are shorter than fourteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 14500"
  },
  {
    "natural-language": "Find roads that are shorter than fifteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 15000"
  },
  {
    "natural-language": "Find roads that are shorter than fifteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 15500"
  },
  {
    "natural-language": "Find roads that are shorter than sixteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 16000"
  },
  {
    "natural-language": "Find roads that are shorter than sixteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 16500"
  },
  {
    "natural-language": "Find roads that are shorter than seventeen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 17000"
  },
  {
    "natural-language": "Find roads that are shorter than seventeen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 17500"
  },
  {
    "natural-language": "Find roads that are shorter than eighteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 18000"
  },
  {
    "natural-language": "Find roads that are shorter than eighteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 18500"
  },
  {
    "natural-language": "Find roads that are shorter than nineteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 19000"
  },
  {
    "natural-language": "Find roads that are shorter than nineteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 19500"
  },
  {
    "natural-language": "Find roads that are shorter than twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20500"
  },
  {
    "natural-language": "Find roads that are shorter than twenty one kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 21000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 22000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 23000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 24000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 25000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 26000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 27000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 28000"
  },
  {
    "natural-language": "Find roads that are shorter than twenty nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 29000"
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
    "natural-language": "Find roads that are shorter than one hundred ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 110000"
  },
  {
    "natural-language": "Find roads that are shorter than one hundred twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 120000"
  },
  {
    "natural-language": "Find roads that are shorter than one hundred thirty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 130000"
  },
  {
    "natural-language": "Find roads that are shorter than one hundred forty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 140000"
  },
  {
    "natural-language": "Find roads that are shorter than one hundred fifty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 150000"
  },
  {
    "natural-language": "Find roads that are shorter than two hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 200000"
  },
  {
    "natural-language": "Find roads that are shorter than three hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 300000"
  },
  {
    "natural-language": "Find roads that are shorter than .5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 500"
  },
  {
    "natural-language": "Find roads that are shorter than 1 kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1000"
  },
  {
    "natural-language": "Find roads that are shorter than 1.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 1500"
  },
  {
    "natural-language": "Find roads that are shorter than 2 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2000"
  },
  {
    "natural-language": "Find roads that are shorter than 2.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 2500"
  },
  {
    "natural-language": "Find roads that are shorter than 3 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3000"
  },
  {
    "natural-language": "Find roads that are shorter than 3.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 3500"
  },
  {
    "natural-language": "Find roads that are shorter than 4 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4000"
  },
  {
    "natural-language": "Find roads that are shorter than 4.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 4500"
  },
  {
    "natural-language": "Find roads that are shorter than 5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5000"
  },
  {
    "natural-language": "Find roads that are shorter than 5.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 5500"
  },
  {
    "natural-language": "Find roads that are shorter than 6 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6000"
  },
  {
    "natural-language": "Find roads that are shorter than 6.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 6500"
  },
  {
    "natural-language": "Find roads that are shorter than 7 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7000"
  },
  {
    "natural-language": "Find roads that are shorter than 7.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 7500"
  },
  {
    "natural-language": "Find roads that are shorter than 8 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8000"
  },
  {
    "natural-language": "Find roads that are shorter than 8.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 8500"
  },
  {
    "natural-language": "Find roads that are shorter than 9 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9000"
  },
  {
    "natural-language": "Find roads that are shorter than 9.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 9500"
  },
  {
    "natural-language": "Find roads that are shorter than 10 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10000"
  },
  {
    "natural-language": "Find roads that are shorter than 10.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 10500"
  },
  {
    "natural-language": "Find roads that are shorter than 11 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 11000"
  },
  {
    "natural-language": "Find roads that are shorter than 11.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 11500"
  },
  {
    "natural-language": "Find roads that are shorter than 12 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 12000"
  },
  {
    "natural-language": "Find roads that are shorter than 12.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 12500"
  },
  {
    "natural-language": "Find roads that are shorter than 13 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 13000"
  },
  {
    "natural-language": "Find roads that are shorter than 13.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 13500"
  },
  {
    "natural-language": "Find roads that are shorter than 14 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 14000"
  },
  {
    "natural-language": "Find roads that are shorter than 14.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 14500"
  },
  {
    "natural-language": "Find roads that are shorter than 15 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 15000"
  },
  {
    "natural-language": "Find roads that are shorter than 15.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 15500"
  },
  {
    "natural-language": "Find roads that are shorter than 16 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 16000"
  },
  {
    "natural-language": "Find roads that are shorter than 16.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 16500"
  },
  {
    "natural-language": "Find roads that are shorter than 17 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 17000"
  },
  {
    "natural-language": "Find roads that are shorter than 17.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 17500"
  },
  {
    "natural-language": "Find roads that are shorter than 18 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 18000"
  },
  {
    "natural-language": "Find roads that are shorter than 18.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 18500"
  },
  {
    "natural-language": "Find roads that are shorter than 19 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 19000"
  },
  {
    "natural-language": "Find roads that are shorter than 19.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 19500"
  },
  {
    "natural-language": "Find roads that are shorter than 20 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20000"
  },
  {
    "natural-language": "Find roads that are shorter than 20.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 20500"
  },
  {
    "natural-language": "Find roads that are shorter than 21 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 21000"
  },
  {
    "natural-language": "Find roads that are shorter than 22 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 22000"
  },
  {
    "natural-language": "Find roads that are shorter than 23 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 23000"
  },
  {
    "natural-language": "Find roads that are shorter than 24 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 24000"
  },
  {
    "natural-language": "Find roads that are shorter than 25 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 25000"
  },
  {
    "natural-language": "Find roads that are shorter than 26 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 26000"
  },
  {
    "natural-language": "Find roads that are shorter than 27 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 27000"
  },
  {
    "natural-language": "Find roads that are shorter than 28 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 28000"
  },
  {
    "natural-language": "Find roads that are shorter than 29 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 29000"
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
    "natural-language": "Find roads that are shorter than 110 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 110000"
  },
  {
    "natural-language": "Find roads that are shorter than 120 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 120000"
  },
  {
    "natural-language": "Find roads that are shorter than 130 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 130000"
  },
  {
    "natural-language": "Find roads that are shorter than 140 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 140000"
  },
  {
    "natural-language": "Find roads that are shorter than 150 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 150000"
  },
  {
    "natural-language": "Find roads that are shorter than 200 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 200000"
  },
  {
    "natural-language": "Find roads that are shorter than 300 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) < 300000"
  },
  {
    "natural-language": "Find roads that are at most half of a kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 500"
  },
  {
    "natural-language": "Find roads that are at most one kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1000"
  },
  {
    "natural-language": "Find roads that are at most one and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1500"
  },
  {
    "natural-language": "Find roads that are at most two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2000"
  },
  {
    "natural-language": "Find roads that are at most two and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2500"
  },
  {
    "natural-language": "Find roads that are at most three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3000"
  },
  {
    "natural-language": "Find roads that are at most three and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3500"
  },
  {
    "natural-language": "Find roads that are at most four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4000"
  },
  {
    "natural-language": "Find roads that are at most four and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4500"
  },
  {
    "natural-language": "Find roads that are at most five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5000"
  },
  {
    "natural-language": "Find roads that are at most five and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5500"
  },
  {
    "natural-language": "Find roads that are at most six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6000"
  },
  {
    "natural-language": "Find roads that are at most six and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6500"
  },
  {
    "natural-language": "Find roads that are at most seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7000"
  },
  {
    "natural-language": "Find roads that are at most seven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7500"
  },
  {
    "natural-language": "Find roads that are at most eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8000"
  },
  {
    "natural-language": "Find roads that are at most eight and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8500"
  },
  {
    "natural-language": "Find roads that are at most nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9000"
  },
  {
    "natural-language": "Find roads that are at most nine and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9500"
  },
  {
    "natural-language": "Find roads that are at most ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10000"
  },
  {
    "natural-language": "Find roads that are at most ten and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10500"
  },
  {
    "natural-language": "Find roads that are at most eleven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 11000"
  },
  {
    "natural-language": "Find roads that are at most eleven and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 11500"
  },
  {
    "natural-language": "Find roads that are at most twelve kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 12000"
  },
  {
    "natural-language": "Find roads that are at most twelve and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 12500"
  },
  {
    "natural-language": "Find roads that are at most thirteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 13000"
  },
  {
    "natural-language": "Find roads that are at most thirteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 13500"
  },
  {
    "natural-language": "Find roads that are at most fourteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 14000"
  },
  {
    "natural-language": "Find roads that are at most fourteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 14500"
  },
  {
    "natural-language": "Find roads that are at most fifteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 15000"
  },
  {
    "natural-language": "Find roads that are at most fifteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 15500"
  },
  {
    "natural-language": "Find roads that are at most sixteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 16000"
  },
  {
    "natural-language": "Find roads that are at most sixteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 16500"
  },
  {
    "natural-language": "Find roads that are at most seventeen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 17000"
  },
  {
    "natural-language": "Find roads that are at most seventeen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 17500"
  },
  {
    "natural-language": "Find roads that are at most eighteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 18000"
  },
  {
    "natural-language": "Find roads that are at most eighteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 18500"
  },
  {
    "natural-language": "Find roads that are at most nineteen kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 19000"
  },
  {
    "natural-language": "Find roads that are at most nineteen and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 19500"
  },
  {
    "natural-language": "Find roads that are at most twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20000"
  },
  {
    "natural-language": "Find roads that are at most twenty and a half kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20500"
  },
  {
    "natural-language": "Find roads that are at most twenty one kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 21000"
  },
  {
    "natural-language": "Find roads that are at most twenty two kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 22000"
  },
  {
    "natural-language": "Find roads that are at most twenty three kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 23000"
  },
  {
    "natural-language": "Find roads that are at most twenty four kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 24000"
  },
  {
    "natural-language": "Find roads that are at most twenty five kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 25000"
  },
  {
    "natural-language": "Find roads that are at most twenty six kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 26000"
  },
  {
    "natural-language": "Find roads that are at most twenty seven kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 27000"
  },
  {
    "natural-language": "Find roads that are at most twenty eight kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 28000"
  },
  {
    "natural-language": "Find roads that are at most twenty nine kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 29000"
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
    "natural-language": "Find roads that are at most one hundred ten kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 110000"
  },
  {
    "natural-language": "Find roads that are at most one hundred twenty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 120000"
  },
  {
    "natural-language": "Find roads that are at most one hundred thirty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 130000"
  },
  {
    "natural-language": "Find roads that are at most one hundred forty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 140000"
  },
  {
    "natural-language": "Find roads that are at most one hundred fifty kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 150000"
  },
  {
    "natural-language": "Find roads that are at most two hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 200000"
  },
  {
    "natural-language": "Find roads that are at most three hundred kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 300000"
  },
  {
    "natural-language": "Find roads that are at most .5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 500"
  },
  {
    "natural-language": "Find roads that are at most 1 kilometer",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1000"
  },
  {
    "natural-language": "Find roads that are at most 1.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 1500"
  },
  {
    "natural-language": "Find roads that are at most 2 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2000"
  },
  {
    "natural-language": "Find roads that are at most 2.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 2500"
  },
  {
    "natural-language": "Find roads that are at most 3 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3000"
  },
  {
    "natural-language": "Find roads that are at most 3.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 3500"
  },
  {
    "natural-language": "Find roads that are at most 4 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4000"
  },
  {
    "natural-language": "Find roads that are at most 4.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 4500"
  },
  {
    "natural-language": "Find roads that are at most 5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5000"
  },
  {
    "natural-language": "Find roads that are at most 5.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 5500"
  },
  {
    "natural-language": "Find roads that are at most 6 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6000"
  },
  {
    "natural-language": "Find roads that are at most 6.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 6500"
  },
  {
    "natural-language": "Find roads that are at most 7 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7000"
  },
  {
    "natural-language": "Find roads that are at most 7.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 7500"
  },
  {
    "natural-language": "Find roads that are at most 8 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8000"
  },
  {
    "natural-language": "Find roads that are at most 8.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 8500"
  },
  {
    "natural-language": "Find roads that are at most 9 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9000"
  },
  {
    "natural-language": "Find roads that are at most 9.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 9500"
  },
  {
    "natural-language": "Find roads that are at most 10 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10000"
  },
  {
    "natural-language": "Find roads that are at most 10.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 10500"
  },
  {
    "natural-language": "Find roads that are at most 11 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 11000"
  },
  {
    "natural-language": "Find roads that are at most 11.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 11500"
  },
  {
    "natural-language": "Find roads that are at most 12 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 12000"
  },
  {
    "natural-language": "Find roads that are at most 12.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 12500"
  },
  {
    "natural-language": "Find roads that are at most 13 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 13000"
  },
  {
    "natural-language": "Find roads that are at most 13.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 13500"
  },
  {
    "natural-language": "Find roads that are at most 14 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 14000"
  },
  {
    "natural-language": "Find roads that are at most 14.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 14500"
  },
  {
    "natural-language": "Find roads that are at most 15 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 15000"
  },
  {
    "natural-language": "Find roads that are at most 15.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 15500"
  },
  {
    "natural-language": "Find roads that are at most 16 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 16000"
  },
  {
    "natural-language": "Find roads that are at most 16.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 16500"
  },
  {
    "natural-language": "Find roads that are at most 17 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 17000"
  },
  {
    "natural-language": "Find roads that are at most 17.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 17500"
  },
  {
    "natural-language": "Find roads that are at most 18 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 18000"
  },
  {
    "natural-language": "Find roads that are at most 18.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 18500"
  },
  {
    "natural-language": "Find roads that are at most 19 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 19000"
  },
  {
    "natural-language": "Find roads that are at most 19.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 19500"
  },
  {
    "natural-language": "Find roads that are at most 20 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20000"
  },
  {
    "natural-language": "Find roads that are at most 20.5 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 20500"
  },
  {
    "natural-language": "Find roads that are at most 21 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 21000"
  },
  {
    "natural-language": "Find roads that are at most 22 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 22000"
  },
  {
    "natural-language": "Find roads that are at most 23 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 23000"
  },
  {
    "natural-language": "Find roads that are at most 24 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 24000"
  },
  {
    "natural-language": "Find roads that are at most 25 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 25000"
  },
  {
    "natural-language": "Find roads that are at most 26 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 26000"
  },
  {
    "natural-language": "Find roads that are at most 27 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 27000"
  },
  {
    "natural-language": "Find roads that are at most 28 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 28000"
  },
  {
    "natural-language": "Find roads that are at most 29 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 29000"
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
    "natural-language": "Find roads that are at most 110 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 110000"
  },
  {
    "natural-language": "Find roads that are at most 120 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 120000"
  },
  {
    "natural-language": "Find roads that are at most 130 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 130000"
  },
  {
    "natural-language": "Find roads that are at most 140 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 140000"
  },
  {
    "natural-language": "Find roads that are at most 150 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 150000"
  },
  {
    "natural-language": "Find roads that are at most 200 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 200000"
  },
  {
    "natural-language": "Find roads that are at most 300 kilometers",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Length(ST_Transform(route, 3857)) <= 300000"
  },
  {
    "natural-language": "Find the longest road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads ORDER BY ST_Length(route) ASC LIMIT 1"
  },

  # Roads that are km long and city with population
  {
    "natural-language": "Find roads that span at least one kilometer through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least one and a half kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least two kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least three kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least four kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least five kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least six kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least seven kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least eight kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least nine kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least ten kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least one kilometer through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least one and a half kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least two kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least three kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least four kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least five kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least six kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least seven kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least eight kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least nine kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least ten kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least one kilometer through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least one and a half kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least two kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least three kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least four kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least five kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least six kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least seven kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least eight kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least nine kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least ten kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least one kilometer through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least one and a half kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least two kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least three kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least four kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least five kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least six kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least seven kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least eight kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least nine kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least ten kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least 1 kilometer through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least 1.5 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least 2 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least 3 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least 4 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least 5 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least 6 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least 7 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least 8 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least 9 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least 10 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least 1 kilometer through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least 1.5 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least 2 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least 3 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least 4 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least 5 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least 6 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least 7 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least 8 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least 9 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least 10 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least 1 kilometer through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least 1.5 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least 2 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least 3 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least 4 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least 5 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least 6 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least 7 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least 8 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least 9 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least 10 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at least 1 kilometer through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1000"
  },
  {
    "natural-language": "Find roads that span at least 1.5 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 1500"
  },
  {
    "natural-language": "Find roads that span at least 2 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 2000"
  },
  {
    "natural-language": "Find roads that span at least 3 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 3000"
  },
  {
    "natural-language": "Find roads that span at least 4 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 4000"
  },
  {
    "natural-language": "Find roads that span at least 5 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 5000"
  },
  {
    "natural-language": "Find roads that span at least 6 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 6000"
  },
  {
    "natural-language": "Find roads that span at least 7 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 7000"
  },
  {
    "natural-language": "Find roads that span at least 8 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 8000"
  },
  {
    "natural-language": "Find roads that span at least 9 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 9000"
  },
  {
    "natural-language": "Find roads that span at least 10 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) >= 10000"
  },
  {
    "natural-language": "Find roads that span at most one kilometer through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most one and a half kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most two kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most three kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most four kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most five kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most six kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most seven kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most eight kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most nine kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most ten kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most one kilometer through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most one and a half kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most two kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most three kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most four kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most five kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most six kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most seven kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most eight kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most nine kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most ten kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most one kilometer through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most one and a half kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most two kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most three kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most four kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most five kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most six kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most seven kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most eight kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most nine kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most ten kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most one kilometer through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most one and a half kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most two kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most three kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most four kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most five kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most six kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most seven kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most eight kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most nine kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most ten kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most 1 kilometer through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most 1.5 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most 2 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most 3 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most 4 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most 5 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most 6 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most 7 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most 8 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most 9 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most 10 kilometers through a city with a population less than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population < 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most 1 kilometer through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most 1.5 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most 2 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most 3 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most 4 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most 5 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most 6 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most 7 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most 8 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most 9 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most 10 kilometers through a city with a population of at most one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population <= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most 1 kilometer through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most 1.5 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most 2 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most 3 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most 4 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most 5 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most 6 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most 7 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most 8 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most 9 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most 10 kilometers through a city with a population greater than one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population > 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },
  {
    "natural-language": "Find roads that span at most 1 kilometer through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1000"
  },
  {
    "natural-language": "Find roads that span at most 1.5 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 1500"
  },
  {
    "natural-language": "Find roads that span at most 2 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 2000"
  },
  {
    "natural-language": "Find roads that span at most 3 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 3000"
  },
  {
    "natural-language": "Find roads that span at most 4 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 4000"
  },
  {
    "natural-language": "Find roads that span at most 5 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 5000"
  },
  {
    "natural-language": "Find roads that span at most 6 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 6000"
  },
  {
    "natural-language": "Find roads that span at most 7 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 7000"
  },
  {
    "natural-language": "Find roads that span at most 8 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 8000"
  },
  {
    "natural-language": "Find roads that span at most 9 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 9000"
  },
  {
    "natural-language": "Find roads that span at most 10 kilometers through a city with a population of at least one hundred thousand people",
    "sql": "SELECT r.id, r.name, ST_Length(ST_Intersection(r.route, c.boundary)::geography) AS intersect_length_km FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population >= 100000 AND ST_Length(ST_Intersection(r.route, c.boundary)::geography) <= 10000"
  },

  # Roads within a distance of a park ( .25 - 100 km )
  {
    "natural-language": "Find roads within a quarter of a kilometer of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 250)"
  },
  {
    "natural-language": "Find roads within a half of a kilometer of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 500)"
  },
  {
    "natural-language": "Find roads within one kilometer of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 1000)"
  },
  {
    "natural-language": "Find roads within one and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 1500)"
  },
  {
    "natural-language": "Find roads within two kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 2000)"
  },
  {
    "natural-language": "Find roads within two and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 2500)"
  },
  {
    "natural-language": "Find roads within three kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 3000)"
  },
  {
    "natural-language": "Find roads within three and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 3500)"
  },
  {
    "natural-language": "Find roads within four kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 4000)"
  },
  {
    "natural-language": "Find roads within four and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 4500)"
  },
  {
    "natural-language": "Find roads within five kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 5000)"
  },
  {
    "natural-language": "Find roads within five and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 5500)"
  },
  {
    "natural-language": "Find roads within six kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 6000)"
  },
  {
    "natural-language": "Find roads within six and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 6500)"
  },
  {
    "natural-language": "Find roads within seven kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 7000)"
  },
  {
    "natural-language": "Find roads within seven and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 7500)"
  },
  {
    "natural-language": "Find roads within eight kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 8000)"
  },
  {
    "natural-language": "Find roads within eight and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 8500)"
  },
  {
    "natural-language": "Find roads within nine kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 9000)"
  },
  {
    "natural-language": "Find roads within nine and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 9500)"
  },
  {
    "natural-language": "Find roads within ten kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 10000)"
  },
  {
    "natural-language": "Find roads within ten and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 10500)"
  },
  {
    "natural-language": "Find roads within eleven kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 11000)"
  },
  {
    "natural-language": "Find roads within eleven and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 11500)"
  },
  {
    "natural-language": "Find roads within twelve kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 12000)"
  },
  {
    "natural-language": "Find roads within twelve and half kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 12500)"
  },
  {
    "natural-language": "Find roads within thirteen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 13000)"
  },
  {
    "natural-language": "Find roads within fourteen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 14000)"
  },
  {
    "natural-language": "Find roads within fifteen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 15000)"
  },
  {
    "natural-language": "Find roads within sixteen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 16000)"
  },
  {
    "natural-language": "Find roads within seventeen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 17000)"
  },
  {
    "natural-language": "Find roads within eighteen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 18000)"
  },
  {
    "natural-language": "Find roads within nineteen kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 19000)"
  },
  {
    "natural-language": "Find roads within twenty kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 20000)"
  },
  {
    "natural-language": "Find roads within twenty one kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 21000)"
  },
  {
    "natural-language": "Find roads within twenty two kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 22000)"
  },
  {
    "natural-language": "Find roads within twenty three kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 23000)"
  },
  {
    "natural-language": "Find roads within twenty four kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 24000)"
  },
  {
    "natural-language": "Find roads within twenty five kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 25000)"
  },
  {
    "natural-language": "Find roads within twenty six kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 26000)"
  },
  {
    "natural-language": "Find roads within twenty seven kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 27000)"
  },
  {
    "natural-language": "Find roads within twenty eight kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 28000)"
  },
  {
    "natural-language": "Find roads within twenty nine kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 29000)"
  },
  {
    "natural-language": "Find roads within thirty kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 30000)"
  },
  {
    "natural-language": "Find roads within forty kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 40000)"
  },
  {
    "natural-language": "Find roads within fifty kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 50000)"
  },
  {
    "natural-language": "Find roads within sixty kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 60000)"
  },
  {
    "natural-language": "Find roads within seventy kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 70000)"
  },
  {
    "natural-language": "Find roads within eighty kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 80000)"
  },
  {
    "natural-language": "Find roads within ninety kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 90000)"
  },
  {
    "natural-language": "Find roads within one hundred kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 100000)"
  },
  {
    "natural-language": "Find roads within .25 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 250)"
  },
  {
    "natural-language": "Find roads within .5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 500)"
  },
  {
    "natural-language": "Find roads within 1 kilometer of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 1000)"
  },
  {
    "natural-language": "Find roads within 1.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 1500)"
  },
  {
    "natural-language": "Find roads within 2 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 2000)"
  },
  {
    "natural-language": "Find roads within 2.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 2500)"
  },
  {
    "natural-language": "Find roads within 3 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 3000)"
  },
  {
    "natural-language": "Find roads within 3.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 3500)"
  },
  {
    "natural-language": "Find roads within 4 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 4000)"
  },
  {
    "natural-language": "Find roads within 4.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 4500)"
  },
  {
    "natural-language": "Find roads within 5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 5000)"
  },
  {
    "natural-language": "Find roads within 5.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 5500)"
  },
  {
    "natural-language": "Find roads within 6 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 6000)"
  },
  {
    "natural-language": "Find roads within 6.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 6500)"
  },
  {
    "natural-language": "Find roads within 7 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 7000)"
  },
  {
    "natural-language": "Find roads within 7.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 7500)"
  },
  {
    "natural-language": "Find roads within 8 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 8000)"
  },
  {
    "natural-language": "Find roads within 8.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 8500)"
  },
  {
    "natural-language": "Find roads within 9 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 9000)"
  },
  {
    "natural-language": "Find roads within 9.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 9500)"
  },
  {
    "natural-language": "Find roads within 10 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 10000)"
  },
  {
    "natural-language": "Find roads within 10.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 10500)"
  },
  {
    "natural-language": "Find roads within 11 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 11000)"
  },
  {
    "natural-language": "Find roads within 11.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 11500)"
  },
  {
    "natural-language": "Find roads within 12 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 12000)"
  },
  {
    "natural-language": "Find roads within 12.5 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 12500)"
  },
  {
    "natural-language": "Find roads within 13 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 13000)"
  },
  {
    "natural-language": "Find roads within 14 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 14000)"
  },
  {
    "natural-language": "Find roads within 15 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 15000)"
  },
  {
    "natural-language": "Find roads within 16 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 16000)"
  },
  {
    "natural-language": "Find roads within 17 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 17000)"
  },
  {
    "natural-language": "Find roads within 18 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 18000)"
  },
  {
    "natural-language": "Find roads within 19 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 19000)"
  },
  {
    "natural-language": "Find roads within 20 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 20000)"
  },
  {
    "natural-language": "Find roads within 21 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 21000)"
  },
  {
    "natural-language": "Find roads within 22 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 22000)"
  },
  {
    "natural-language": "Find roads within 23 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 23000)"
  },
  {
    "natural-language": "Find roads within 24 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 24000)"
  },
  {
    "natural-language": "Find roads within 25 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 25000)"
  },
  {
    "natural-language": "Find roads within 26 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 26000)"
  },
  {
    "natural-language": "Find roads within 27 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 27000)"
  },
  {
    "natural-language": "Find roads within 28 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 28000)"
  },
  {
    "natural-language": "Find roads within 29 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 29000)"
  },
  {
    "natural-language": "Find roads within 30 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 30000)"
  },
  {
    "natural-language": "Find roads within 40 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 40000)"
  },
  {
    "natural-language": "Find roads within 50 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 50000)"
  },
  {
    "natural-language": "Find roads within 60 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 60000)"
  },
  {
    "natural-language": "Find roads within 70 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 70000)"
  },
  {
    "natural-language": "Find roads within 80 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 80000)"
  },
  {
    "natural-language": "Find roads within 90 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 90000)"
  },
  {
    "natural-language": "Find roads within 100 kilometers of a park",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN parks p ON ST_DWithin(ST_Transform(r.route, 2229), ST_Transform(p.boundary, 2229), 100000)"
  },  

  # Roads by distance to city (.25 -20 km)
  
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

  # Find roads in city
  {
    "natural-language": "Find roads in Ojai",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ojai' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Camarillo",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Camarillo' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Oxnard",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Oxnard' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Ventura",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Ventura' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Fillmore",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Fillmore' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Moorpark",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Moorpark' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Simi Valley",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Simi Valley' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Santa Paula",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Santa Paula' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Thousand Oaks",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Thousand Oaks' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find roads in Port Hueneme",
    "sql": "SELECT r.* FROM roads r JOIN cities c ON c.name = 'Port Hueneme' WHERE ST_Intersects(c.boundary, r.route);"
  },
  {
    "natural-language": "Find the longest road in the city with the highest population",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population = (SELECT MAX(population) FROM cities) ORDER BY ST_Length(r.route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road in the city with the highest population",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population = (SELECT MAX(population) FROM cities) ORDER BY ST_Length(r.route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road in the city with the lowest population",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population = (SELECT MIN(population) FROM cities) ORDER BY ST_Length(r.route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road in the city with the lowest population",
    "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN cities c ON ST_Intersects(ST_Transform(r.route, 4326), ST_Transform(c.boundary, 4326)) WHERE c.population = (SELECT MIN(population) FROM cities) ORDER BY ST_Length(r.route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Ventura",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Ojai",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Oxnard",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Oxnard",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Camarillo",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Camarillo",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Fillmore",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Fillmore",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Moorpark",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Moorpark",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Simi Valley",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Simi Valley",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Santa Paula",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Santa Paula",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Port Hueneme",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Port Hueneme",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  {
    "natural-language": "Find the shortest road within Thousand Oaks",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) ASC LIMIT 1"
  },
  {
    "natural-language": "Find the longest road within Thousand Oaks",
    "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE ST_Intersects(ST_Transform(route, 4326), ST_Transform((SELECT boundary FROM cities WHERE name = 'Ventura'), 4326)) ORDER BY ST_Length(route) DESC LIMIT 1"
  },
  # Find roads by buildings TODO: Add queries V2
  # {
  #   "natural-language": "Find roads that have multiple buildings that are owned by the same group",
  #   "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326)) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = TRUE GROUP BY r.id HAVING COUNT(DISTINCT b.id) > 1"
  # },
  # {
  #   "natural-language": "Find roads that have buildings that are not owned by groups",
  #   "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326)) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE"
  # },
  # {
  #   "natural-language": "Find the road with the most buildings",
  #   "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326)) GROUP BY r.id ORDER BY COUNT(b.id) DESC LIMIT 1"
  # },
  # {
  #   "natural-language": "Find the road with the least buildings",
  #   "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326)) GROUP BY r.id ORDER BY COUNT(b.id) ASC LIMIT 1"
  # },
  # {
  #   "natural-language": "Find the road with the most individual owners",
  #   "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326)) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY r.id ORDER BY COUNT(DISTINCT b.owning_entity_id) DESC LIMIT 1"
  # },
  # {
  #   "natural-language": "Find the road with the least individual owners",
  #   "sql": "SELECT r.name, ST_AsGeoJSON(r.route) AS route FROM roads r JOIN buildings b ON ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(r.route, 4326)) JOIN owning_entities o ON b.owning_entity_id = o.id WHERE o.is_group = FALSE GROUP BY r.id ORDER BY COUNT(DISTINCT b.owning_entity_id) ASC LIMIT 1"
  # },
  # {
  #   "natural-language": "Find roads with no buildings",
  #   "sql": "SELECT name, ST_AsGeoJSON(route) AS route FROM roads WHERE NOT EXISTS (SELECT 1 FROM buildings b WHERE ST_Intersects(ST_Transform(b.location, 4326), ST_Transform(roads.route, 4326)))"
  # },

  # Easternmost, westernmost, etc.
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
  }
]