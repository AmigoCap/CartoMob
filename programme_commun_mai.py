# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:49:44 2018

@author: Raphaël
"""

###############################################################################
#
# Imports
#
###############################################################################
import json
import pandas as pd
import matplotlib.pyplot as plt
import time as time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import matplotlib.cbook as cbook

###############################################################################
#
# Lecture du fichier
#
###############################################################################
#Lecture du fichier
file = "Historique des positions raphael 140318.json"
df = pd.read_json(file)

donnee=df.get("locations")

###############################################################################
#
# Récupération des données
# Méthodes de nettoyage des données (Fabien) 
# Les données "propres" sont stockées dans lat, long, temps.
#
###############################################################################

#Récupération et nettoyage par différence de longitude et latitude entre les points
# Récupération des données
lat,long,temps=[],[],[] #Variables permettant de récupérer les données PROPRES
for i in range(1,len(donnee)):
    la=donnee[i]["latitudeE7"]/1e7 #Variables permettant de récupérer les données BRUTES
    lo=donnee[i]["longitudeE7"]/1e7
    t=donnee[i]["timestampMs"]
    t1=donnee[i-1]["timestampMs"]
    t,t1=float(t)/1000,float(t1)/1000 # Conversion des mesures de temps

#On considère qu'en 15 secondes, on ne peut traverser le campus (varation longitude~2.5e-3 et variation longitude~4e-3)
    if lo<=4.7775 and lo>=4.7650:
        if abs(t-t1)<=10 and (la-donnee[i-1]["latitudeE7"]/1e7)<=4e-3 and (lo-donnee[i-1]["longitudeE7"]/1e7)<=2.5e-3:
            lat.append(la)
            long.append(lo)
            temps.append(t)

###############################################################################
#
# Méthodes et scripts utilisant le module "time"
#
###############################################################################

#Pour obtenir les infos sur un temps (ex : jour, mois, heure...)
infos_temps = time.localtime(temps[67])
# Renvoie le tuple time.struct_time(tm_year=2018, tm_mon=2, tm_mday=17, tm_hour=17, tm_min=34, tm_sec=50, tm_wday=5, tm_yday=48, tm_isdst=0)

#Pour afficher les données sous un format plus lisible
string_temps= time.asctime(infos_temps)
# Renvoie le string 'Sat Feb 17 17:34:50 2018'


def j_annee(temps):
    """Donne la liste des jours de l'année correspondant aux temps de type "time" de la liste des temps"""
    n = len(temps)
    liste = [0]*n
    for i in range(n):
        liste[i]=time.localtime(temps[i])[7]
    return liste

jour_temps = j_annee(temps) #Ne regarde que l'information "A quel jour de l'année correspond ce temps?"
annuaire_jours = list(set(jour_temps)) #Annuaire des jours pour lesquels on a une mesure.

def i_min(liste,valeur):
    """Retourne l'indice à partir duquel apparaît la valeur dans la liste"""
    n = len(liste)
    for k in range(n):
        if liste[k]==valeur:
            return k
        
def i_max(liste,valeur,imin):
    """
    Hypothèse : liste de valeurs décroissante
    Retourne l'indice strict supérieur à partir duquel disparaît la valeur dans la liste"""
    n = len(liste)
    for k in range(imin,n):
        if liste[k]<valeur:
            return k

def affichage_jours(i,lat,long,temps):
    jour_temps = j_annee(temps)
    #annuaire_jours = list(set(jour_temps))
    imin = i_min(jour_temps,i)
    imax = i_max(jour_temps,i,imin)
    lat1 = lat[imin:imax]
    long1 = long[imin:imax]
    temps1 = temps[imin:imax]
    return lat1,long1,temps1

#Permet de récupérer les données temporelles d'une journée en particulier.
lat1,long1,temps1 = affichage_jours(313,lat,long,temps)

def affichage_heure(heure,lat,long,temps):
    """ heure : entier compris entre 0 et 23 inclus
        lat, long, temps : données paramétrées en début de script (attention, il faut prendre la liste des temps modifiée pour être utilisable par le module time.)
        
        Retourne une liste de tuples (latitude,longitude,temps) de points situés entre l'heure h et l'heure h+1. """
    n = len(temps)
    llt = []
    for i in range(n):
        if time.localtime(temps[i])[3] == heure:
            llt_i = (lat[i],long[i],temps[i])
            llt.append(llt_i)
    return llt

def annuaire_heures(lat,long,temps):
    """On fait une liste de listes qui trie les infos temporelles en fonction du créneau horaire
    
    Exemple : annuaire_heures(lat,long,temps)[17] renvoie les tuples (latitude,longitude,temps) de l'ensemble des données, situés entre 17h et 18h."""
    ann=[]
    for h in range(24):
        ann.append(affichage_heure(h,lat,long,temps))
    return ann

#Permet de récupérer les points d'une heure en particulier (dans Centrale, sur l'ensemble des données nettoyées)
annuaireHeures = annuaire_heures(lat,long,temps)

###############################################################################
#
#   Affichage carte de France
#
###############################################################################

#datafile1 = 'france-political-map.jpg'
#img1 = plt.imread(datafile1)
#plt.figure(1)
#plt.scatter(long,lat,zorder=1)
#plt.imshow(img1, zorder=0, extent=[-5.219663, 9.820620,40.267598, 51.727552])
#plt.show()

###############################################################################
#
# Affichage Campus Lyon Ouest
#
###############################################################################

#datafile2 = 'carte_centrale_grande.png'
#img2 = plt.imread(datafile2)
#plt.figure(2)
#plt.scatter(long,lat,zorder=1)
#plt.imshow(img2,zorder=0,extent = [4.76175,4.78386,45.77960,45.79011])
#plt.show()

###############################################################################
#
# Affichage des données sur le campus de Centrale
#
###############################################################################

#datafile3 = 'carte_centrale_petite.png'
#img3 = plt.imread(datafile2)
#plt.figure(3)
#plt.scatter(long,lat,zorder=1)
#plt.imshow(img3,zorder=0,extent = [4.76471,4.77209,45.78041,45.78603])
#plt.show()

###############################################################################
#
# Fonctions d'appartenance aux différentes zones
#
###############################################################################