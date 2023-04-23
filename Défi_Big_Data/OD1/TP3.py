#TP3

import importlib
import time

fichier_fct_hach = importlib.import_module("fonctions_hachage_classe")

liste_fun = fichier_fct_hach.liste_fun

M = 833334

def read_fichier(fichier) :
    with open(fichier,'r') as fichier : # ouverture du fichier en lecture seule
        L1 = fichier.readlines() # crée une liste constituée des lignes du fichier en lecture.
        # On supprime les espaces superflus en début et en fin de chaine si il y en a.
        L_propre = [i.strip() for i in L1] 
    return L_propre


def Bloom(fichier1, fichier2, m, k):
    debut = time.time()
    #Phase d'insertion
    T=[0 for i in range(m)]
    L_doublons=[]
    s1=read_fichier(fichier1)
    s2=read_fichier(fichier2)
    for mot in s1:
        for x in liste_fun[0:k]:
            i = x(mot, M)
            T[i]+=1
            
    #Phase de recherche
    for mot in s2:
        test=1
        for x in liste_fun[0:k]:
            i = x(mot, M)
            if T[i]==0:
                test=0
        if test!=0:
            L_doublons.append(mot)
    fin=time.time()
    
    #Suppresion des doublons de la liste L_doublons (le fichier 'word2' en contient beaucoup)
    L_sans_doublons = list(set(L_doublons))
    return T, len(L_doublons), len(L_sans_doublons), fin - debut

            
## Obtenir un tableau de bits (0 ou 1) sans informations sur les collisions avec Bloom2

def Bloom2(fichier1, fichier2, m, k):
    debut = time.time() 
    T=[[0] for i in range(m)] # filtre de Bloom : tableau de taille m
    L_doublons=[] # liste des intersections trouvées dans les deux fichiers
    s1=read_fichier(fichier1)
    s2=read_fichier(fichier2)
    # On commence par hacher chaque mot du premier fichier k fois
    for mot in s1: 
        for x in liste_fun[0:k]:
            i = x(mot, M) # hachage du mot par la fonction x
            if T[i][0]==0:
                T[i][0]=1 # on égalise T[i][0] à 1
            if T[i][0]!=1:
                T[i].append(1) # on ajoute un 1 à la liste T[i]  
                # obtenu pour mot par la fonction x
    # Phase de recherche des doublons
    for mot in s2:
        test=1
        for x in liste_fun[0:k]:
            i = x(mot, M)
            if T[i][0]==0: # on teste si le mot testé a la même valeur de 
            # hachage qu'un mot du fichier précédent
                test=0 # si ce n'est pas le cas, le test est faux et ce n'est
                # pas un mot du fichier 1
        if test!=0: # si le mot testé a les mêmes valeurs de hachage qu'un mot
        # du fichier 1 alors il est dans le fichier 1 et 2 et on l'ajoute à la
        # liste des intersections
            L_doublons.append(mot) 
    fin=time.time()
    
    # Suppression des doublons de l'intersection
    L_sans_doublons = list(set(L_doublons))
    return L_sans_doublons, len(L_sans_doublons),fin - debut # on retourne 
    # l'intersection des fichiers et le temps d'execution du filtre
            
                
        

