import json
import os


def charger():
    os.chdir('C:/Users/theot/Desktop/Historique des Positions/histo_sliced')
    
    #loading files
    L=[]
    for file in os.listdir(os.getcwd()):
        df=open(file).read()
        df=json.loads(df)
        L.append(df['locations'])
    return(L)
    