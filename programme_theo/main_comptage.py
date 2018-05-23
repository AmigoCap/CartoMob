import os
import time

os.chdir('C:/Users/theot/Desktop/srcipt_pe')

import decompte
from loading_files import charger
import zone
import numpy as np
from chali import affichage_jours,affichage_heure,annuaire_jours

donnees=charger()


data_list=[{'lat':[x[i]['latitudeE7']/1e7 for i in range(len(x))],'long':[x[i]['longitudeE7']/1e7 for i in range(len(x))],'temps':[x[i]['timestampMs'] for i in range(len(x))]} for x in donnees]



def decoupage_heure(l):
    """on découpe sur la journée, les données d'une personne"""
    temps=[(int(t)/1000) for t in l['temps']]
    out=[affichage_heure(h,l['lat'],l['long'],temps) for h in range(24)]
    out_con=[{'lat':[q[0] for q in x], 'long':[q[1] for q in x], 'temps':[q[2] for q in x] } for x in out ]
    return(out_con)

def decoupage_journee(l):
    """On découpe en journées"""
    temps=[int(t)/1000 for t in l['temps']]
    out=annuaire_jours(l['lat'],l['long'],temps)
    return out


def decoupage_tot(l):
    A=decoupage_journee(l)
    out=[decoupage_heure(a) for a in A]
    return(out)

def somme_dict(L):
    """prend en argument une liste de dictionnaires, avec tous les memes clés, et retourne la somme des valeurs associées à chaque clé"""
    S={key:0 for key in L[0].keys()}
    for x in L:
        S={key:S[key]+x[key] for key in S.keys()}
    return S

def sum_dict(dict):
    """fais la somme des valeurs dans un dictionnaire"""
    return(sum(dict.values()))

def dict_zone(l):
    A=decoupage_tot(l)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]=zone.quelle_zone(A[i][j])
    return A

def tot_compte():
    L=[]
    for x in data_list:
        L.append(decoupage_tot(x))
    
    A=[[] for j in range(len(data_list[0]))]
    for i in range(len(L[0])):
        for j in range(len(L[0][0])):
            A[i].append(somme_dict([zone.quelle_zone(L[q][i][j]) for q in range(len(L))]))
    return A






























# 
# #de 8h a 20h
# 
# debut='Wed Mar 7 08:00:00 2018'
# debut=time.strptime(debut)
# debut=time.mktime(debut)
# 
# finabs='Wed Mar 7 20:00:00 2018'
# finabs=time.strptime(finabs)
# finabs=time.mktime(finabs)
# 
# fin='Wed Mar 7 9:00:00 2018'
# fin=time.strptime(fin)
# fin=time.mktime(fin)
# 
# compteur=0
# accu=[]
# 
# for A in donnees:
#     stock=[]
#     l=[]
#     
#     i=9
#     fin='Wed Mar 7 {}:00:00 2018'.format(i)
#     fin=time.strptime(fin)
#     fin=time.mktime(fin)
#     
#     for j in range(len(A)):
#         compteur+=1
#         if int(A[len(A)-1-j]['timestampMs'])/1000>debut :
#             if int(A[len(A)-1-j]['timestampMs'])/1000>fin:
#                 stock.append(l)
#                 l=[]
#                 i+=1
#                 fin='Wed Mar 7 {}:00:00 2018'.format(i)
#                 fin=time.strptime(fin)
#                 fin=time.mktime(fin)
#             if int(A[len(A)-1-j]['timestampMs'])/1000<fin:
#                 l.append(A[len(A)-1-j])
#             if fin>finabs:
#                 break
#     accu.append(stock)
#     
# for i in range(len(accu)):
#     for j in range(len(accu[i])):
#         accu[i][j]=decompte.decompte(accu[i][j])
#         
# for i in range(len(accu)):
#     for j in range(len(accu[i])):
#         accu[i][j]=np.array(accu[i][j])
# 
# 
# f=[]
# 
# for j in range(len(accu[0])):
#     s=0
#     for i in range(len(accu)):
#         s+=accu[i][j]
#     f.append(s)
