# TP1 Structure interne des donnÃ©es

## Importation

import time

#Fonction qui découpe le 
def read_fichier(fichier) :
    with open(fichier,'r') as fichier : # ouverture du fichier en lecture seule
        L1 = fichier.readlines() # crée une liste constituée des lignes 
        # du fichier en lecture
        L_propre = [i.strip() for i in L1] # supprime les espaces superflus en 
        # début et en fin de chaine si il y en a
    return L_propre

def puget_veronneau_hachage_originel(chaine,M,c1,c2):
    debut = time.time()
    j=0
    nb_collisions=0
    s=read_fichier(chaine) 
    hash_table=[0 for i in range(M)]
    for x in s:
        y=conversion(x,26)
        i = hash_base(y,c1,c2,M)
        if hash_table[i]==0:
            hash_table[i]=x
        else:
            while hash_table[i]!=0 : # on va faire de l'adressage ouvert
                nb_collisions+=1
                i= (i+ c1*j + c2*j**2)%M # sondage quadratique
                j+=1
            hash_table[i]=x
    fin = time.time()
    return hash_table, nb_collisions, fin - debut
        
def hash_base(x,alpha,beta,M):
    return (alpha*x+beta)%M

def conversion(mot, base):
    b=base
    p=1000000007
    h=0
    bl =1
    for c in mot:
        h = (h + (ord(c)*bl))%p
        bl = (bl*b)%p
    return h%base
    




