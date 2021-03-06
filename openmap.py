import requests
import json
import numpy as np
import matplotlib.pyplot as plt

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area["ISO3166-1"="IN"][admin_level=2];
(node["amenity"="parking"](area);
 way["amenity"="parking"](area);
 rel["amenity"="parking"](area);
);
out center;
"""

response = requests.get(overpass_url, 
                        params={'data': overpass_query})
data = response.json()

# Collect coords into list
coords = []
for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    coords.append((lon, lat))
# Convert coordinates into numpy array
X = np.array(coords)
plt.plot(X[:, 0], X[:, 1], 'o')
plt.title('Biergarten in Germany')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()
