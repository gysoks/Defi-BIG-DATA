#TP2 OD1

## Importation

import time

def read_fichier(fichier) :
    with open(fichier,'r') as fichier : # ouverture du fichier en lecture seule
        L1 = fichier.readlines() # crée une liste constituée des lignes du fichier en lecture.
        # On supprime les espaces superflus en début et en fin de chaine si il y en a.
        L_propre = [i.strip() for i in L1] 
    return L_propre


def fct_hachage(x,alpha,beta,M):
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

### Recherche dans le cas d'un adressage ferme (liste a l'emplacement specifie)

def puget_veronneau_hachage_ferme(chaine,M,c1,c2):
    debut = time.time()
    nb_collisions=0
    s=read_fichier(chaine) 
    hash_table=[[] for i in range(M)]
    for x in s:
        y=conversion(x,26)
        i = fct_hachage(y,c1,c2,M)
        if len(hash_table[i])==0:
            hash_table[i].append(x)
        else:
            # La case est déjà remplie: on ajoute le mot à la liste correspondante
            hash_table[i].append(x)
            nb_collisions+=1
    fin = time.time()
    return hash_table, nb_collisions, fin - debut

def recherche_ferme(table_hachage, fichier_2, M, c1, c2):
    s2=read_fichier(fichier_2)
    L_doublons=[]
    for x in s2:
        y=conversion(x,26)
        i = fct_hachage(y,c1,c2,M)
        if [x]==table_hachage[i]: 
            # table_hachage[i] contient une liste avec un ou plusieurs mots
            L_doublons.append(x)
    return L_doublons

# Essai avec 'texte_Shakespeare' en texte de référence, et 'corncob_lowercase' pour la recherche de doublons

M = 786307 # M a déjà été déterminé au TP1_OD1
T_hachage = puget_veronneau_hachage_ferme('texte_Shakespeare.txt', M, 3, 5)[0]
L_doublons = recherche_ferme(T_hachage, 'corncob_lowercase.txt', M, 3, 5)

print(T_hachage)
print(L_doublons, len(L_doublons))

### Recherche dans le cas d'un adressage ouvert (si case remplie, on prend la case d'après)


## Sondage linéaire
def puget_veronneau_hachage_ouvert(chaine,M,c1,c2):
    debut = time.time()
    nb_collisions=0
    s=read_fichier(chaine) 
    hash_table=[[] for i in range(M)]
    for x in s:
        y=conversion(x,26)
        i = fct_hachage(y,c1,c2,M)
        if len(hash_table[i])==0:
            hash_table[i]=[x]
        else:
            num_iterations = 0
            while len(hash_table[i])!=0 and num_iterations < M:
                nb_collisions+=1
                i=(i+1) % M  # Utiliser l'opérateur modulo pour retourner à l'indice 0 après avoir atteint la fin de la table
                num_iterations += 1
            if num_iterations >= M:
                # Si nous avons parcouru toute la table de hachage sans trouver de case vide, sortir de la boucle
                break
            hash_table[i]=[x]
    fin = time.time()
    return hash_table, nb_collisions, fin - debut

def recherche_ouvert(table_hachage, fichier_2, M, c1, c2):
    s2=read_fichier(fichier_2)
    L_doublons=[]
    for x in s2:
        y=conversion(x,26)
        i = fct_hachage(y,c1,c2,M)
        if len(table_hachage[i])>0: 
            # table_hachage[i] contient une liste avec un ou plusieurs mots
            while [x]!=table_hachage[i] and i<len(table_hachage):
                # On effectue un sondage linéaire jusqu'à retrouver le bon mot
                i=i+1
            if i<len(table_hachage) and [x]==table_hachage[i]:
                L_doublons.append(x)
    return L_doublons

M = 786307 # M a déjà été déterminé au TP1_OD1
T_hachage2 = puget_veronneau_hachage_ouvert('texte_Shakespeare.txt', M, 3, 5)[0]
L_doublons2 = recherche_ouvert(T_hachage, 'corncob_lowercase.txt', M, 3, 5)

#print(T_hachage2)
#print(L_doublons2, len(L_doublons2))

##Sondage quadratique 

def puget_veronneau_hachage_quadratique(chaine,M,c1,c2):
    debut = time.time()
    j=0
    nb_collisions=0
    s=read_fichier(chaine) 
    hash_table=[[] for i in range(M)]
    for x in s:
        y=conversion(x,26)
        i = fct_hachage(y,c1,c2,M)
        if len(hash_table[i])==0:
            hash_table[i]=[x]
        else:
            while len(hash_table[i])>0 : # on va faire de l'adressage ouvert
                nb_collisions+=1
                i= (i+ c1*j + c2*j**2)%M # sondage quadratique
                j+=1
            hash_table[i]=[x]
    fin = time.time()
    return hash_table, nb_collisions, fin - debut

def recherche_ouvert_quadratique(table_hachage, fichier_2, M, c1, c2):
    s=read_fichier(fichier_2)
    j=0
    L_doublons=[]
    for x in s:
        y=conversion(x,26)
        i = fct_hachage(y,c1,c2,M)
        if len(table_hachage[i])>0: 
            # table_hachage[i] contient une liste avec un ou plusieurs mots
            while [x]!=table_hachage[i]:
                # On effectue un sondage linéaire jusqu'à retrouver le bon mot
                i= (i+ c1*j + c2*j**2)%M # sondage quadratique
                j+=1
            L_doublons.append(x)
    return L_doublons
