import psycopg2
import folium
import json
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

m = folium.Map(location=[34.2490, -118.9651], zoom_start=11)

def add_layer(query, geom_type, color, fill_color=None, point_radius=5):
    """Add a layer to the map using the given query and geometry type."""
    cursor.execute(query)
    
    for row in cursor.fetchall():
        name, geom_geojson = row
        if geom_geojson is None:
            continue
        
        try:
            geom = json.loads(geom_geojson)
        except Exception as e:
            print(f"Error loading GeoJSON for {name}: {e}")
            continue

        if geom_type == "point" and geom['type'] == "Point":
            folium.Marker(
                location=[geom['coordinates'][1], geom['coordinates'][0]],
                popup=name,
                icon=folium.Icon(color=color)
            ).add_to(m)
        if geom_type == "polygon" and geom['type'] in ["Polygon", "MultiPolygon"]:
            folium.GeoJson(
                geom,
                name=name,
                style_function=lambda x: {
                    "color": color,
                    "fillColor": fill_color,
                    "fillOpacity": 0.2
                }
            ).add_to(m)
        if geom_type == "line" and geom['type'] == "MultiLineString":
            folium.GeoJson(
                geom,
                name=name,
                style_function=lambda x: {
                    "color": color,
                    "weight": 3,
                    "opacity": 1
                }
            ).add_to(m)

# TOOD: Execute one of these depending on the table being selected from in the SQL script
add_layer("SELECT name, ST_AsGeoJSON(boundary) FROM cities WHERE boundary IS NOT NULL", "polygon", "blue", "#0000ff")
# add_layer("SELECT name, ST_AsGeoJSON(route) FROM roads WHERE route IS NOT NULL", "line", "red")
# add_layer("SELECT name, ST_AsGeoJSON(boundary) FROM parks WHERE boundary IS NOT NULL", "polygon", "green", "#00FF00")
# add_layer("SELECT street_number, ST_AsGeoJSON(location) FROM buildings WHERE location IS NOT NULL", "point", "red")



m.save("webmap.html")
cursor.close()
conn.close()
print("Map saved as webmap.html")
