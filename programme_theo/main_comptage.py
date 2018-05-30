import os
import time

os.chdir('C:/Users/theot/Desktop/srcipt_pe')

import decompte
from loading_files import charger
import zone

from graphviz import Digraph
import matplotlib.pyplot as plt
import numpy as np
from chali import affichage_jours,affichage_heure,annuaire_jours

donnees=charger()


data_list=[{'lat':[x[i]['latitudeE7']/1e7 for i in range(len(x))],'long':[x[i]['longitudeE7']/1e7 for i in range(len(x))],'temps':[int(x[i]['timestampMs'])/1000 for i in range(len(x))]} for x in donnees]


##Fonctions qui permettent de mettre en forme le jeu de données, séparant heure par heure 
def decoupage_heure(l):
    """on découpe sur la journée, les données d'une personne"""
    out=[affichage_heure(h,l['lat'],l['long'],l['temps']) for h in range(24)]
    out_con=[{'lat':[q[0] for q in x], 'long':[q[1] for q in x], 'temps':[q[2] for q in x] } for x in out ]
    return(out_con)

def decoupage_journee(l):
    """On découpe en journées"""
    out=annuaire_jours(l['lat'],l['long'],l['temps'])
    return out


def decoupage_tot(l):
    A=decoupage_journee(l)
    out=[decoupage_heure(a) for a in A]
    return(out)

## Deux fonction utiles pour manier les dictionnaires
def somme_dict(L):
    """prend en argument une liste de dictionnaires, avec tous les memes clés, et retourne la somme des valeurs associées à chaque clé"""
    S={key:0 for key in L[0].keys()}
    for x in L:
        S={key:S[key]+x[key] for key in S.keys()}
    return S

def sum_dict(dict):
    """fais la somme des valeurs dans un dictionnaire"""
    s=sum(dict.values())
    if s==0:
        return 1
    else:
        return s

def dict_zone(l):
    A=decoupage_tot(l)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]=zone.quelle_zone(A[i][j])
    return A
# 
# def tot_compte():
#     L=[]
#     for x in data_list:
#         L.append(decoupage_tot(x))
#     
#     A=[[] for j in range(len(data_list[0]))]
#     for i in range(len(L[0])):
#         for j in range(len(L[0][0])):
#             A[i].append(somme_dict([zone.quelle_zone(L[q][i][j]) for q in range(len(L))]))
#     return A
# 

def localisation_tot(jour,n):
    L=[dict_zone(x) for x in data_list]
    out=somme_dict([ x[jour][n] for x in L])
    s=sum_dict(out)
    if s!=0:
        out={key:out[key]/s for key in out.keys()}    #renormalisation
    return out
    

# pour afficher:
# plt.bar(range(len(D)), list(D.values()), align='center')
# plt.xticks(range(len(D)), list(D.keys()))


def afficher_12h(jour):
    Z=[localisation_tot(jour,8+h) for h in range(12)]
    fig1, axes1 = plt.subplots(ncols=6, nrows=1, figsize=(13.42, 12))
    for h in range(12):
        axes1[h].bar(range(len(Z[h])), list(Z[h].values()), align='center')
        axes1[h].set_xticklabels(list(Z[h].keys()), rotation='vertical')
        
    fig1, axes1 = plt.subplots(ncols=6, nrows=1, figsize=(13.42, 12))
    for h in range(6):
        axes[h].bar(range(len(Z[h])), list(Z[h].values()), align='center')
        axes[h].set_xticklabels(list(Z[h].keys()), rotation='vertical')
        
    plt.show()
    return None

##Construction d'un graphe de changement d'état

def decision_location(l):
    """ l est le dictionnaire relatif à une heure en nombre de points par zone """
    if sum_dict(l)==0:
        return 'autre'
    else:
        return max(l, key=lambda k: l[k])

def decision_journee(l):
    out=[decision_location(x) for x in l]
    return out

def construction_matrice(l):
    debaze={'zone_labo':0,'zone_W1':0,'zone_M':0,'zone_entree':0,'zone_residence':0,'entree_chemin_mouilles':0,'entree_charriere_blanche':0,'autre':0}
    dict_trans={key:debaze.copy() for key in debaze.keys()}
    
    A=dict_zone(l)
    
    L=[decision_journee(x) for x in A]
    
    for x in L:
        for i in range(23):
            dict_trans[x[i]][x[i+1]]+=1
    
    return dict_trans

def somme_dict_matrice(L):
    """L une liste de matrices-dictionnaires de mêmes clés..."""
    S={}
    for key in L[0].keys():
        S[key]=somme_dict([x[key] for x in L])
    return S
    
def passage_tot():
    M=somme_dict_matrice([construction_matrice(x) for x in data_list])
    M={key1: {key2:M[key1][key2]/sum_dict(M[key1]) for key2 in M[key1].keys()} for key1 in M.keys()}
    return M



def graphe():
    M=passage_tot()
    
    os.chdir('C:/Users/theot/Desktop/srcipt_pe/graff')
    
    G=Digraph(name='chgtdetat', engine='dot')
    for x in M.keys():
        G.node(x)
    for x in M.keys():
        for y in M.keys():
            s=int(M[x][y]*100)/100
            if s>0:
                G.edge(x,y,str(s))
                
    G.view()
    
    # pour aller ouvrir un .gv déjà defini : graphviz.render('circo','png',os.getcwd() + '\\chgtdetat.gv')
    
    return None
    













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