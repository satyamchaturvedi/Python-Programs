import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_prod(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'


map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

#map.add_child(folium.Marker(location=[30, 77.5],popup="its a Marker",icon=folium.Icon(color='green')))   "or"
fgv=folium.FeatureGroup(name="VOLCANOES")
#for coordinates in [[30, 77.5],[26.922185, 75.690122]]:
    #fg.add_child(folium.Marker(location=coordinates,popup="its a Marker",icon=folium.Icon(color='green')))
for lt, ln ,el in zip(lat,lon,elev):
    #to change marker style simply add Circle with marker in the below statement
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6,popup=str(el) + "m",fill_color=color_prod(el),fill=True,color='grey',fill_opacity = 0.7))
fgp=folium.FeatureGroup(name="POPULATION")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<1000000 else 'orange' if 1000000<= x['properties']['POP2005']<2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")
