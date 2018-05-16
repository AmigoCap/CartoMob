#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:51:49 2018

@author: fabienlyon
"""

import json
import pandas as pd

#Les lignes de code ci-dessus permettent de regrouper dans une seule et même liste de latitude l'ensemble des latitudes des participants
#et dans une liste longitude l'ensemble des longitudes des participants

L=[] #Cette liste est à compléter avec le nom des fichiers des différents participants ex: L=['Historique_theo.json','Historique_maude.json'...]
lat,long,temps=[],[],[]
for e in L:
    f=open(e)
    df = pd.read_json(f)
    donnee=df.get("locations")
    for i in range(len(donnee)):
        la=donnee[i]["latitudeE7"]/1e7
        lo=donnee[i]["longitudeE7"]/1e7
        t=donnee[i]["timestampMs"]
        if (la>((0.41)*(lo)+43.8292) and la<((0.393)*(lo)+43.912) and la<(-1.25*(lo)+51.747) and la>(-81.5*(lo)+434.175)) or (la>((-1.1627)*(lo)+51.32236) and la<((-1.6666)*(lo)+53.7361) and la<(0.5699*(lo)+43.06686) and la>(0.611*(lo)+42.86844)) or (la>((-1.2778)*(lo)+51.879) and la<((-1.6)*(lo)+53.41658) and la<(0.175*(lo)+44.9496525) and la>(0.5*(lo)+43.3909)) or (la>((0.42857)*(lo)+43.74) and la<((0.375)*(lo)+43.9962) and la<(-1*(lo)+50.5508) and la>4.7762) or (la>((1.8333)*(lo)+37.0358) and la<((1.6923)*(lo)+37.71) and la<(-0.2*(lo)+46.73768) and la>(-1.66667*(lo)+46.576233)) or (la>((-0.3357)*(lo)+47.38) and la<((-0.575)*(lo)+48.523) and la<(0.6142857*(lo)+42.8528814) and la>(0.42*(lo)+43.778)) or (la>((-1.1)*(lo)+51.03143) and la<((-2.0667)*(lo)+55.64414) and la<(0.3125*(lo)+44.294) and la>(0.3*(lo)+44.35301)): 
            lat.append(la)
            long.append(lo)
            temps.append(t)
    f.close()

#Pour la représentation graphique sur une carte
datafile3 = 'carte_centrale_petite.png'
img3 = plt.imread(datafile3)
plt.scatter(long,lat)
plt.axis('normal')
plt.axis.xlim = 7.55*1.4
plt.axis.ylim = 6.84*1.4
plt.imshow(img3,zorder=0,extent = [4.76471,4.77209,45.78041,45.78603])
plt.show()


def zone_labo(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone des laboratoires"""
    long_labo,lat_labo,temps_labo = [],[],[]
    for i in range(len(lat)):
        if lat[i]>((0.41)*(long[i])+43.8292) and lat[i]<((0.393)*(long[i])+43.912) and lat[i]<(-1.25*(long[i])+51.747) and lat[i]>(-81.5*(long[i])+434.175):
            long_labo.append(long[i])  
            lat_labo.append(lat[i])
            temps_labo.append(temps[i])
    return long_labo,lat_labo,temps_labo

def zone_W1(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone des bâtiments W1 et W1bis"""
    long_W1,lat_W1,temps_W1=[],[],[]
    for i in range(len(lat)):
        if lat[i]>((-1.1627)*(long[i])+51.32236) and lat[i]<((-1.6666)*(long[i])+53.7361) and lat[i]<(0.5699*(long[i])+43.06686) and lat[i]>(0.611*(long[i])+42.86844):
            long_W1.append(long[i])  
            lat_W1.append(lat[i])
            temps_W1.append(temps[i])
    return long_W1,lat_W1,temps_W1

def zone_M(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone des M14, M15, M16 et Gymnase"""
    long_M,lat_M,temps_M=[],[],[]
    for i in range(len(lat)):
        if lat[i]>((-1.2778)*(long[i])+51.879) and lat[i]<((-1.6)*(long[i])+53.41658) and lat[i]<(0.175*(long[i])+44.9496525) and lat[i]>(0.5*(long[i])+43.3909):  
            lat_M.append(lat[i])
            temps_M.append(temps[i])
            long_M.append(long[i])
    return long_M,lat_M,temps_M

def zone_entree(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    long_E,lat_E,temps_E=[],[],[]
    for i in range(len(lat)):
        if lat[i]>((0.42857)*(long[i])+43.74) and lat[i]<((0.375)*(long[i])+43.9962) and lat[i]<(-1*(long[i])+50.5508) and lat[i]>4.7762: 
            lat_E.append(lat[i])
            long_E.append(long[i])
            temps_E.append(temps[i])
    return long_E,lat_E,temps_E

def zone_residence(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    long_R,lat_R,temps_R=[],[],[]
    for i in range(len(lat)):
        if lat[i]>((1.8333)*(long[i])+37.0358) and lat[i]<((1.6923)*(long[i])+37.71) and lat[i]<(-0.2*(long[i])+46.73768) and lat[i]>(-1.66667*(long[i])+46.576233): 
            lat_R.append(lat[i])
            long_R.append(long[i])
            temps_R.append(temps[i])
    return long_R,lat_R,temps_R

def entree_charriere_blance(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    long_CB,lat_CB,temps_CB=[],[],[]
    for i in range(len(lat)):
        if lat[i]>((-0.3357)*(long[i])+47.38) and lat[i]<((-0.575)*(long[i])+48.523) and lat[i]<(0.6142857*(long[i])+42.8528814) and lat[i]>(0.42*(long[i])+43.778):
            lat_CB.append(lat[i])
            long_CB.append(long[i])
            temps_CB.append(temps[i])
    return long_CB,lat_CB,temps_CB

def entree_chemin_mouilles(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    long_CM,lat_CM,temps_CM=[],[],[]
    for i in range(len(lat)):
        if lat[i]>((-1.1)*(long[i])+51.03143) and lat[i]<((-2.0667)*(long[i])+55.64414) and lat[i]<(0.3125*(long[i])+44.294) and lat[i]>(0.3*(long[i])+44.35301):
            lat_CM.append(lat[i])
            long_CM.append(long[i])
            temps_CM.append(temps[i])
    return long_CM,lat_CM,temps_CM
