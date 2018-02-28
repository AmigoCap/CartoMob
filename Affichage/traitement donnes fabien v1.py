# Quelques imports
import json
import pandas as pd
import matplotlib.pyplot as plt

#Lecture du fichier
file = "Historique des positions raphael 090118.json"
df = pd.read_json(file)
print(df)

donnee=df.get("locations")
print(donnee)

#Récupération des latitudes, longitudes et des dates
lat=[]
long=[]
temps=[]

for i in range(len(donnee)):
    lat.append(donnee[i]["latitudeE7"]/1e7)
    long.append(donnee[i]["longitudeE7"]/1e7)
    temps.append(donnee[i]["timestampMs"])
    
plt.plot(long,lat)
plt.xlabel('longitude')
plt.ylabel('latitude')

# Get current size
fig_size = plt.rcParams["figure.figsize"]
 
# Prints: [8.0, 6.0]
print("Current size:", fig_size)
 
# Set figure width to 12 and height to 9
fig_size[0] = 13.42
fig_size[1] = 12
plt.rcParams["figure.figsize"] = fig_size

datafile = 'france-political-map.jpg'
img = imread(datafile)
plt.scatter(x,y,zorder=1)
plt.imshow(img, zorder=0, extent=[-5.0, 10,40.41, 51.86])
#plt.show()

def ouca(donnee):
    n = len(donnee)
    for i in range(n):
        if donnee[i]["longitudeE7"]/1e7 <1:
            return i



#datafile = 'france-political-map.jpg'
#img = imread(datafile)
#plt.scatter(x,y,zorder=1)
#plt.imshow(img, zorder=0, extent=[-5.219663, 9.820620,40.267598, 51.727552])
#plt.show()

#Point bas droite 40.267598, 9.820620
#Point haut gauche 51.727552, -5.219663
#Ordre [left, right, bottom, top]
        
