### liste fonctions élèves

import math

liste_fun = []

def boudras_thomas_bon_hachage(X_chaine, M_integer): ## la méthode de cette fonction de hachage consiste à prendre le mot qu'on veut hacher, le répèter jusqu'à avoir un nouveau mot de 100 caractère et enfin appliquer une formule sur ce mot qui va nous donner la clef du mot initial
    clef=0
    if (len(X_chaine)!=0) : ## on vérifie qu'il n'y pas dans la base de donnée de ligne vide
        for i in range(100) :
            if (X_chaine[i%len(X_chaine)]!=X_chaine[i%len(X_chaine)-1]) : ## cette distinction évite de crée des clefs identiques si deux mots sont composés d'une seule lettre mais un nombre différent de fois (Par exemple avec le mot "a" et "aa", avec cette methode on créerait deux mot identique "aaaaa...aaaa" et donc on risquerait d'avoir la même clef)
                clef += ord(X_chaine[i%len(X_chaine)])*101**i ## formule qu'on applique à ce nouveau mot de 100 caractères
            else :
                clef += (ord(X_chaine[i%len(X_chaine)])+len(X_chaine))*101**i
        return clef%M_integer
    else :
        return False

liste_fun.append(boudras_thomas_bon_hachage)

def Kretz_hashage(X_chaine, M_integer):
    hash=0
    for i in range(0, len(X_chaine)):
        hash+= ord(X_chaine[i])*(i+1)**2
        ## la valeur de hashage est la somme des valeurs ASCII des lettres du mot fois leur position au carré
    return (hash)%M_integer
liste_fun.append(Kretz_hashage)

def motio_bon_hachage(X_chaine, M_integer) :
    if str(X_chaine)!=X_chaine or int(M_integer)!=M_integer:
        return False
    lettres = [51,64,35,75,46,44,99,71,69,73,13,8,58,53,61,22,28,95,66,62,80,68,67,90,24,10] # Obtenu à partir de conversion_alphabet()
    ecart = ord('a')
    integer_value = 0
    for i in range(len(X_chaine)):
        n = lettres[ord(X_chaine[i])-ecart]
        integer_value += (ord(X_chaine[i])*n)%M_integer
    return integer_value % M_integer

def hachage_base_motio(X_chaine, M_integer) :
    if str(X_chaine)!=X_chaine or int(M_integer)!=M_integer:
        return False
    a = 29 # 29 est premier et permet de contenir tout le jeu de caractères des clés
    l = len(X_chaine)
    ecart = ord('a')
    integer_value = 0
    for i in range(len(X_chaine)):
        integer_value += (ord(X_chaine[i])-ecart)*a**(l-i-1)%M_integer
    return integer_value %M_integer

liste_fun.append(motio_bon_hachage)
liste_fun.append(hachage_base_motio)

def hash_string_bernstein(input_string, hash_table_size):
    """
    Fonction de hachage basé sur la fonction djb2 de Dan Bernstein, recommandé par ChatGPT :)

    Parameters
    ----------
    input_string: str
        Chaine de caractères
    hash_table_size: int
        Taille de la table de hachage

    Returns
    -------
    integer_value: int
        Valeur de hachage
    """

    # Initialize the hash value to a prime number
    hash_value = 5381

    # Loop through each character in the string
    for char in input_string:
        # Update the hash value using the following formula:
        # hash_value = (hash_value * 33) + ord(char)
        hash_value = ((hash_value << 5) + hash_value) + ord(char)

    # Compute the index in the hash table by taking the absolute value of the hash value modulo the table size

    hash_index = abs(hash_value) % hash_table_size

    # Return the computed hash index
    return hash_index

liste_fun.append(hash_string_bernstein)

def peter_eid_bon_hachage(X_chaine: str, M_integer: int):
    """
    Fonction de hachage basé sur la fonction "Polynomial Rolling Hash"

    Parameters
    ----------
    X_chaine: str
        Chaine de caractères
    M_integer: int
        Taille de la table de hachage

    Returns
    -------
    integer_value: int
        Valeur de hachage
    """
    p=53
    length = len(X_chaine)
    temp_hash=0
    p_pow = 1

    for i in range(length):
        temp_hash = (temp_hash + (1 + ord(X_chaine[i]) - ord('a')) * p_pow) % M_integer
        p_pow = (p_pow * p) % M_integer

    integer_value = temp_hash
    return integer_value

liste_fun.append(peter_eid_bon_hachage)

def fct_hachage_oussamaE(chaine, taille_table) :
    taille=len(chaine)
    ch=[]
    for i in range(taille) :
        lettre=chaine[i]
        chiffre=ord(lettre)%97
        ch.append(chiffre)
    ch_b26=0
    for i in range(len(ch)) :
        ch_b26=ch_b26 + ch[i]*(26**(taille-i-1))
    ch_b26= ch_b26 % taille_table
    return ch_b26

liste_fun.append(fct_hachage_oussamaE)


def fct_hash_jenkins(chaine,Taille):
    def toBinary(chaine):
        l,m=[],[]
        for i in chaine:
            l.append(ord(i))
        for i in l:
            m.append(int(bin(i)[2:]))
        return m
    c=toBinary(chaine)
    hash=0
    for i in range(len(c)):
        hash += c[i]
        hash += (hash << 10)
        hash ^= (hash >> 6)
    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)
    return hash%Taille

liste_fun.append(fct_hash_jenkins)

def Saleh_Yokamamoharan_hachage(string, table_size):
    hash_value = 0

    for i in range(len(string)):
        hash_value += ord(string[i]) * (31**(len(string)-i-1))  # La fonction ord renvoie le code Unicode

    return hash_value % table_size

liste_fun.append(Saleh_Yokamamoharan_hachage)

def hash_Najlaa_Imane_1 (s,M):
    """la fonction prend en pramètre une chaine de caractère et la valeur M et renvoie l'index du mot dans la table hachage """
    g=31
    hash=0
    for i in range(0,len(s)) :
        hash = (hash*g + ord(s[i]))
    hash=hash%M
    return hash

liste_fun.append(hash_Najlaa_Imane_1)

#La deuxième fonction
def ascii_function(mot):
    """fonction prend en argument une chaine de caractère et renvoie la liste du code ASCII du mot """
    ascii= [ord(lettre)%97 for lettre in mot]
    return ascii

def hash_Najlaa_Imane_2(s,M):
    """ fonction de hachage qui se base sur la représentation dans la base 26"""
    ascii=ascii_function(s)
    ascii=ascii +[len(s)]
    hash= 0
    for i in range(len(ascii)):
        hash=hash+((ascii[i])*(26**(len(ascii)-i-1)))
    hash=hash%M
    return hash

liste_fun.append(hash_Najlaa_Imane_2)

# Amèlioration
def hash_Najlaa_Imane_3(s,M):
    """  Amélioration de  la fonction de hachage précédente en faisant une permutation si le code ASCII commence par 0   """
    ascii=ascii_function(s)
    if ascii[0]==0:
        i=0
        while ascii[i]==0 and i+1<len(s):
            i=i+1
        ascii=ascii[i:]+ascii[:i]
    hash=0
    for i in range(len(ascii)):
        hash=hash+((ascii[i])*(26**(len(ascii)-i-1)))
    hash=hash%M
    return hash

liste_fun.append(hash_Najlaa_Imane_3)

#Amélioration 2
def hash_Najlaa_Imane_4(s,M):
    ascii=ascii_function(s)
    g=31
    ascii=ascii +[len(s)]
    hash= 0
    for i in range(0,len(s)) :
        hash = (hash*g + ord(s[i]))
    for i in range(len(ascii)):
        hash=hash+((ascii[i])*(26**(len(ascii)-i-1)))

    hash^= (hash >> 16)
    hash ^= (hash >> 9)
    hash += (hash << 15)
    hash += (hash << 3)
    hash=hash%M
    return hash

liste_fun.append(hash_Najlaa_Imane_4)


def EID_Nabih_bon_hachage(X_chaine, M_integer):

  # Use a larger prime number
    prime = 15485867

    # Add additional bitwise operations
    hash_val = 0
    for c in X_chaine:
        hash_val = (((hash_val << 5) - hash_val) + ord(c)) & 0xFFFFFFFFFFFFFFFF

    # Apply the prime number
    hash_val = (hash_val * prime) & 0xFFFFFFFFFFFFFFFF

    # Apply additional bitwise operations
    hash_val = (hash_val ^ (hash_val >> 30)) * 0xBF58476D1CE4E5B9
    hash_val = (hash_val ^ (hash_val >> 27)) * 0x94D049BB133111EB
    hash_val = hash_val ^ (hash_val >> 31)

    # Reduce the hash value to fit within the hash table size
    hash_val = hash_val % M_integer

    return hash_val

liste_fun.append(EID_Nabih_bon_hachage)

def f_hachage_morganj(cdc,M):
    s=0
    for i in range(len(cdc)):
        s=19*s+ord(cdc[i])
        s=s%M
    return s

liste_fun.append(f_hachage_morganj)

def jactat_maxime_bon_hachage(word,M):#h2
    #collisions 15.304%
    #uniformité 1.0099
    # 2sec pour hacher tout les mots de word2.txt
    number = 0
    n = len(word)
    for i,letter in enumerate(word) :
        number += n*(i+2)*ord(letter)*(53**(n+i-1))
    return number%M

liste_fun.append(jactat_maxime_bon_hachage)

def maxime_jactat_gold_hash_string4(word,M):
    number = 0
    n = len(word)
    gold_number = (np.sqrt(5)-1)*0.5
    for i,letter in enumerate(word) :
        number += (gold_number *(ord(letter)*i*n)**2)
    return round(number)%M

#liste_fun.append(maxime_jactat_gold_hash_string4)

def FRANÇOIS_bon_hachage(X_chaine, M):
    x = 0
    n = len(X_chaine)
    for i in range(n):
        x = x + ord(X_chaine[i])*2**n-i-1
    return x%M

liste_fun.append(FRANÇOIS_bon_hachage)

def Maxime_F_hachage_bis(X_chaine,M):
    x = 0
    n =len(X_chaine)
    for i in range(n):
        x = (x*128 + ord(X_chaine[i]))
    return x%M

liste_fun.append(Maxime_F_hachage_bis)

def BRES_bon_hachage(string, M = 786307):
    h = 0
    for character in string:
        h = (h * 128 + ord(character)) % M
    return h

liste_fun.append(BRES_bon_hachage)

def puget_veronneau_bon_hachage1(X_chaine, M_integer):
    b = 26 # taille de l'alphabet
    h = 0 # valeur de hachage
    b2 = 1
    for c in X_chaine:
        h = (h + (ord(c) * b2))
        b2 = (b2 * b)
    return h % M_integer # on applique un modulo pour obtenir un indice
    # dans la table de hachage

liste_fun.append(puget_veronneau_bon_hachage1)

def puget_veronneau_bon_hachage2(X_chaine, M_integer):
    a = 33 # nombre premier le plus proche de la taille de l'alphabet
    h = 0 # valeur de hachage
    for i in range(len(X_chaine)):
        h += ord(X_chaine[i]) * (a ** (len(X_chaine) - i - 1))
    return h % M_integer # on applique un modulo pour obtenir un indice
    # dans la table de hachage

liste_fun.append(puget_veronneau_bon_hachage2)

def liam_latour_bon_hash(string, M):
    number = 0

    for char in string:
        number += ord(char)
        number <<= 8
        number %= 802589

    return number%M

liste_fun.append(liam_latour_bon_hash)


def hachage_GPT(str,M):
    # Initialisation des variables de hachage
    hash = 2166136261
    prime = 16777619

    # Itération sur chaque caractère de la chaîne
    for char in str:
        # XOR de la valeur ASCII du caractère avec le hash courant
        hash = (hash ^ ord(char)) * prime

    # Retourne le hash modulo 2^32
    return (hash % (2**32))%M

liste_fun.append(hachage_GPT)

dico ={}
nombres_premiers = [1]
c=1
b=True
while (len(nombres_premiers)<26):
    c+=1
    for i in range(2,round(math.sqrt(c))+1):
        if (c%i) == 0:
            b = False
    if b and (c!=2) and (c!=5):
        nombres_premiers.append(c)
    b=True

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range (len(alphabet)):
    dico[alphabet[i]] = nombres_premiers[i]

def hachage_leo(str, M):
    valeur = 0
    for i in range (len(str)):
        valeur += (i+1) * dico[str[i]] ** 3
    return (valeur%M)

#liste_fun.append(hachage_leo)

def lu_hachage1(chaine, taille):
    hash = len(chaine)
    p = 107
    for c in chaine:
        hash = (hash * p + ord(c))
    return hash % taille

liste_fun.append(lu_hachage1)

def lu_hachage2(chaine, taille):
    hash = 0
    for c in chaine:
        hash += ord(c)
        hash += (hash << 12)
        hash ^= (hash >> 6)
    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)
    return hash % taille

liste_fun.append(lu_hachage2)

def de_andrade_bon_hachage(X_chaine, M_integer):
	integer_value = 0
	for x in X_chaine:
		integer_value += ord(x)* 256**(X_chaine.index(x))
	integer_value = integer_value % M_integer
	return integer_value

liste_fun.append(de_andrade_bon_hachage)

def de_andrade_bon_hachage2(X_chaine, M_integer):
	integer_value = 0
	for x in X_chaine:
		integer_value += string.ascii_lowercase.index(x)* 26**(X_chaine.index(x))
	integer_value = integer_value % M_integer
	return integer_value

#liste_fun.append(de_andrade_bon_hachage2)

def isla_gubbay_bon_hachage (chaine, M):
    somme = 0
    nb_lettres=0
    hash=0
    for i in range (0, len(chaine)):
        somme = somme + ord(chaine[i])-65
        somme = somme << 6
        nb_lettres+=1
    hash = somme+nb_lettres
    hash = hash%M
    return hash

liste_fun.append(isla_gubbay_bon_hachage)

def hachage_paul(mot,taille_table_hachage):
    h=[]
    number=0
    position=0
    voyelles=["a","e","i","o","u","y"]
    for lettre in mot:
        if lettre in voyelles:
            h.append(1)
        else: h.append(2)
    for i in range(len(h)):
        number+=h[i]*10**(len(h)-i-1)
    position=number%taille_table_hachage
    return position

liste_fun.append(hachage_paul)

def hachage2_paul(mot,size):
    H = 0
    for lettre in mot:
        H = (H*11 +ord(lettre)) % size
    return H

liste_fun.append(hachage2_paul)

# Hugo et Lucas
def string_to_base26(string):
    '''
    La fonction string_to_base26 convertit une chaîne de caractère donnée en sa représentation numérique en base 26.
    Elle ne peut donc convertir que les chaînes de caractères dont la typograpie est en minuscule.
    L'argument string est une chaîne de caractères.
    '''
    n = len(string)
    b = 26
    x = 0

    for k in range(n):
        x += (ord(string[k]) - ord("a")) * b**(n-(k+1))

    return(x)

def hash_div_hugo_lucas(string, p):
    '''
    hash_div est une fonction de hachage par division. Elle renvoie une valeur de hachage à partir d'un string.
    L'argument string est une chaîne de caractères.
    '''
    key = string
    return(string_to_base26(key) % p)

liste_fun.append(hash_div_hugo_lucas)

def jenkins_hash(string):
    '''
    La fonction jenkins_hash renvoie une valeur de hachage de 32 bits.
    L'argument string est une chaîne de caractères.
    '''
    hash = 0

    for char in string:
        hash += ord(char)
        hash += (hash << 10)
        hash ^= (hash >> 6)

    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)

    return(hash)

def sha256_hash(string):
    """
    sha256_hash renvoie une valeur de hachage de 256 bits que l'on convertit en sa représentation numérique en base 26.
    string est une chaîne de caractères.
    """

    if type(string) != bytes:
        string = string.encode('utf-8')

    hash_object = hashlib.sha256(string)
    hex_dig = hash_object.hexdigest()
    hash_values = string_to_base26(hex_dig)

    return(hash_values)

def YORIATTI_hachage_original(X_chaine, M_integer):
    """
    YORIATTI_hachage_original calcule la valeur de hachage d'une clé par le biais de sinus, cosinus et SHA-256.
    X_chaine est une chaîne de caractères.
    M_integer est un entier qui représente la taille de la table de hachage.
    """
    hash_val = 0
    for i, char in enumerate(X_chaine):
        hash_val += i ** ord(char) * math.sin(i) * math.cos(i) * sha256_hash(char)

    hash_val = int(abs(hash_val) * M_integer) % M_integer
    return (hash_val)

#liste_fun.append(YORIATTI_hachage_original)

def adressage_ouv_div_jenkins_hugo_lucas(string, M):
    k = 5
    return((hash_div_hugo_lucas(string,M) + k * jenkins_hash(string)) % M)

liste_fun.append(adressage_ouv_div_jenkins_hugo_lucas)

## Hamza
def string_to_int_ASCII(s):
    n=len(s)
    r=0
    for k in range(n):
        r+=(ord(s[k])*(127**k))
    return r

def string_to_int_ASCII_mod(s,M):
    n=len(s)
    r=0
    for k in range(n):
        r+=(ord(s[k])*(127**k))%M
    return r%M

def h1_Hamza(s,M):
    return string_to_int_ASCII_mod(s,M)

liste_fun.append(h1_Hamza)


M=833334
p=M
q=400009
a,b=3,7

def h2_int(x,p):
    x0=int(x%q)
    x1=int(x//q)
    return (pow(a,x0,p)*pow(b,x1,p))%p

def h2_Hamza(s,M):
    x=string_to_int_ASCII(s)
    return h2_int(x,M)


liste_fun.append(h2_Hamza)

def jenkins_hash_i_giorgio(string, table_size):
    hash_val = 0
    for char in string:
        hash_val += ord(char)
        hash_val += (hash_val << 10)
        hash_val ^= (hash_val >> 6)
    hash_val += (hash_val << 3)
    hash_val ^= (hash_val >> 11)
    hash_val += (hash_val << 15)
    return hash_val % table_size

liste_fun.append(jenkins_hash_i_giorgio)

def murmur_hash_i_giorgio(string, table_size):
    seed = 0x9747b28c
    m = 0x5bd1e995
    r = 24
    hash_val = seed ^ len(string)
    while len(string) >= 4:
        k = (ord(string[0]) & 0xff) | ((ord(string[1]) & 0xff) << 8) | ((ord(string[2]) & 0xff) << 16) | ((ord(string[3]) & 0xff) << 24)
        k = (k * m) & 0xffffffff
        k ^= k >> r
        k = (k * m) & 0xffffffff
        hash_val = ((hash_val * m) & 0xffffffff) ^ k
        string = string[4:]
    if len(string) == 3:
        hash_val ^= (ord(string[2]) & 0xff) << 16
    if len(string) >= 2:
        hash_val ^= (ord(string[1]) & 0xff) << 8
    if len(string) >= 1:
        hash_val ^= (ord(string[0]) & 0xff)
        hash_val = ((hash_val * m) & 0xffffffff)
    hash_val ^= hash_val >> 13
    hash_val = ((hash_val * m) & 0xffffffff)
    hash_val ^= hash_val >> 15
    return hash_val % table_size

liste_fun.append(murmur_hash_i_giorgio)

def fnv_hash_i_giorgio(string, table_size):
    fnv_prime = 0x811C9DC5
    hash_val = 0
    for char in string:
        hash_val *= fnv_prime
        hash_val ^= ord(char)
    return hash_val % table_size

liste_fun.append(fnv_hash_i_giorgio)

def pire_fonction_hachage_fu(string,MdC):
    hash_value = 0
    for char in string:
        hash_value += ord(char)
    return round((hash_value*(np.sqrt(5)-1)*0.5)%MdC)

#liste_fun.append(pire_fonction_hachage_fu)

def fonction_deuxieme_fu(string,MdC):
  hash_value = 0
  length=len(string)
  for i, char in enumerate(string):
      hash_value += ord(char)*(25**(length-i-1))
  return round((hash_value*(np.sqrt(5)-1)*0.5)%MdC)

#liste_fun.append(fonction_deuxieme_fu)

def hash_function2_Emeric(data, max_value):
    hash_value = 0
    for char in data:
        hash_value = ((hash_value *32) + hash_value) ^ ord(char)
    return hash_value % max_value

liste_fun.append(hash_function2_Emeric)

## Diego et Ignacio

def hash_fonction1(word):
  hash = np.uint32(0)
  for c in word:
    hash += (ord(c) <<  5) | (ord(c) & hash)
    hash ^= (hash >> 6) + hash

  hash ^= (hash >> 8) | ~(hash << 12)
  hash = (hash << 3)

  return abs(hash)

def hash_fonction2(word):
  hash = np.uint32(0)
  for c in word:
    hash += ((ord(c)  << 2) & ~(ord(c) << 3))
    hash = (hash  << 3)
    hash -= (hash >> 5)
    hash ^= (hash >> 7)

  hash ^= (hash << 1) & ~(hash >> 17)
  hash = (hash >> 2) & ~(hash << 13)
  hash -= (hash >> 3)


  return abs(hash)

def nacho_diego_hachageV2(word,M):
  ## pas le bon type
  p = M
  cle1 = hash_fonction1(word)
  cle2 = hash_fonction2(word)

  finalHash = (cle1 % p + cle2 % p) % M

  return finalHash

#liste_fun.append(nacho_diego_hachageV2)

""" pour Daniel

alphab=list(string.ascii_lowercase)
b=len(alphab)

def tibi_daniel_hachage1(x,M):
    #représentation numérique de x en base b=26

    l=len(x)
    integer=0
    for e in x:
        i=alphab.index(e)
        l=l-1
        integer+=i*b**l

    #HACHAGE PAR DIVISION
    integer=integer%M #valeur comprise entre 0 et M-1 (tableau de taille M)

    return integer

#liste_fun.append(tibi_daniel_hachage1)

def tibi_daniel_hachage2(x,M):
    #représentation numérique de x en base b=26

    l=len(x)
    integer=0
    for e in x:
        i=alphab.index(e)
        l=l-1
        integer+=i*b**l

    #HACHAGE PAR MULTIPLICATION
    A=(math.sqrt(5)-1)/2 #D.Knuth
    integer=math.floor(M*((integer*A)%1))

    return integer

#liste_fun.append(tibi_daniel_hachage2)"""

def fhachage_cleo(mot,M):
    x=0
    for i in range(len(mot)):
        x=x+ord(mot[i])
    return x % M

liste_fun.append(fhachage_cleo)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range (len(alphabet)):
    dico[alphabet[i]] = nombres_premiers[i]

def fhachage2_cleo(str, M):
    valeur = 0
    for i in range (len(str)):
        valeur += (i+1) ** 1 * dico[str[i]] ** 3
    return (valeur%M)

liste_fun.append(fhachage2_cleo)

def aknin_bon_hashage(mot,size):
    H = 0
    for lettre in mot:
        H = (H*11 +ord(lettre)) % size
    return H

liste_fun.append(aknin_bon_hashage)

def aknin_hashage_original(mot,size):
    voyelles = ""
    consonnes = ""
    for lettre in mot:
        if lettre.lower() in ['a', 'e', 'i', 'o', 'u']:
            voyelles += lettre
        else:
            consonnes += lettre

    voyelles_hash = sum([ord(lettre) for lettre in voyelles])
    consonnes_hash = sum([ord(lettre) for lettre in consonnes])

    H = (voyelles_hash << 4) | (consonnes_hash >> 4)
    return H%size

liste_fun.append(aknin_hashage_original)

def fonction_hachage1_ayoub(word, taille_table):
    # initialiser une table de hachage vide
    hash_val = 0

    # hacher chaque mot
    for char in word:
        hash_val += ord(char) # La fonction ord() renvoie le point de code Unicode d'un caractère donné
    hash_val *= 17 # nombre premier arbitraire pour une meilleure répartition
    hash_val %= taille_table

    return hash_val

liste_fun.append(fonction_hachage1_ayoub)

def fonction_hachage2_ayoub(word, taille_table):
    # Initialisation de la liste qui contiendra la conversion en base 36 de la chaine de caractères
    codes = []
    for i in range(len(word)):  # On parcourt la chaine par lettres:
        letter = word[i]
        # On convertit les lettres en ascii puis modulo 37 pour avoir la valeur en base 26
        code = ord(letter) % 37
        codes.append(code)

    hash_val = 0
    for i in range(len(codes)):
        # Conversion de toute la chaine en base 26
        hash_val = hash_val + ((codes[i])*(36**(len(codes)-i-1)))

    hash_val = hash_val % taille_table  # Puis modulo la taille de la table

    return hash_val

liste_fun.append(fonction_hachage2_ayoub)

def mussard_arthur_hachage1(x, M):
    val = 0
    for l in x:
        val = (val * 26 + ord(l)) % M
    return val

liste_fun.append(mussard_arthur_hachage1)

"""## pour Angel B
Alphabet = list(string.ascii_lowercase)
Longueur_Alphabet = len(Alphabet)

def BRICQUIR_Hachage_Original(x,M) :
    val = 0
    l = len(x)
    for e in x:
        i = Alphabet.index(e)
        l = l-1
        val += i*Longueur_Alphabet**l
    val = val%M
    return(val)

#liste_fun.append(BRICQUIR_Hachage_Original)

def BRICQUIR_Hachage_2(x, M):
    hash_value = 0
    for e in x:
        hash_value = (hash_value * 31 + Alphabet.index(e)) % M
    return hash_value

#liste_fun.append(BRICQUIR_Hachage_2)

def BRICQUIR_pire_hachage(x, M):
    hash_value = 0
    l = len(x)
    for e in x:
        hash_value = int(np.ceil(hash_value + (Alphabet.index(e)+1)**(np.pi-l)))
    return hash_value % M

#liste_fun.append(BRICQUIR_pire_hachage)"""