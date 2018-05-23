"""
Created on Wed Feb  7 15:51:49 2018
@author: fabienlyon
"""

import json
import pandas as pd
import chali

L=[]
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



def zone_labo(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone des laboratoires"""
    return(lat>((0.41)*(long)+43.8292) and lat<((0.393)*(long)+43.912) and lat<(-1.25*(long)+51.747) and lat>(-81.5*(long)+434.175))

def zone_W1(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone des bâtiments W1 et W1bis"""
    return(lat>((-1.1627)*(long)+51.32236) and lat<((-1.6666)*(long)+53.7361) and lat<(0.5699*(long)+43.06686) and lat>(0.611*(long)+42.86844))

def zone_M(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone des M14, M15, M16 et Gymnase"""
    return(lat>((-1.2778)*(long)+51.879) and lat<((-1.6)*(long)+53.41658) and lat<(0.175*(long)+44.9496525) and lat>(0.5*(long)+43.3909)) 


def zone_entree(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    return(lat>((0.42857)*(long)+43.74) and lat<((0.375)*(long)+43.9962) and lat<(-1*(long)+50.5508) and lat>4.7762)

def zone_residence(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    return(lat>((1.8333)*(long)+37.0358) and lat<((1.6923)*(long)+37.71) and lat<(-0.2*(long)+46.73768) and lat>(-1.66667*(long)+46.576233)) 

def entree_charriere_blanche(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    return(lat>((-0.3357)*(long)+47.38) and lat<((-0.575)*(long)+48.523) and lat<(0.6142857*(long)+42.8528814) and lat>(0.42*(long)+43.778))

def entree_chemin_mouilles(long,lat,temps):
    """Renvoie l'ensemble des points dans la zone de l'entrée principale"""
    return(lat>((-1.1)*(long)+51.03143) and lat<((-2.0667)*(long)+55.64414) and lat<(0.3125*(long)+44.294) and lat>(0.3*(long)+44.35301))
    
def quelle_zone(dict):
    """Prends en argument un dictionnaire {'lat','long','temps'} et renvoie un dictionnaire détaillant le nombre de points dans chaque zone"""
    out={'zone_labo':0,'zone_W1':0,'zone_M':0,'zone_entree':0,'zone_residence':0,'entree_chemin_mouilles':0,'entree_charriere_blanche':0}
    for i in range(len(dict['lat'])):
        if zone_W1(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['zone_W1']+=1
        elif zone_residence(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['zone_residence']+=1
        elif zone_labo(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['zone_labo']+=1
        elif zone_entree(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['zone_entree']+=1
        elif zone_M(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['zone_M']+=1
        elif entree_charriere_blanche(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['entree_charriere_blanche']+=1
        elif entree_chemin_mouilles(dict['long'][i],dict['lat'][i],dict['temps'][i]):
            out['entree_chemin_mouilles']+=1
    return out