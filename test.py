import urllib, json
import folium

map = folium.Map(location=[49.838319, 6.4748])

key = "016f1b38-62f0-4a2b-88f7-dc5b743a9b56"
url = "https://graphhopper.com/api/1/route?point=49.156562%2C6.47644&point=49.837982%2C6.47644&type=json&points_encoded=false&key=" + key

response = urllib.urlopen(url)
data = json.loads(response.read())
tmp = data["paths"][0]["points"]
# print tmp
geo_data = { "type": "LineString", "coordinates": tmp["coordinates"] };

folium.GeoJson(geo_data).add_to(map)

map.save('osm.html')
