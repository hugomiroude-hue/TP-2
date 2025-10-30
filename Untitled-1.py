"""
#exercice 1

1) correct donne "4a"
2) faux
3) correct donne "2-a"
4) faux
5) correct donne "aaaa"
6) faux
7) correct donne "abbc"
8) faux

#exercice 2

1) correcte dit "B"
2) dis J
3) 7
4) pas corrrecte
5) Br
6) Brrrr
7) True
8) False
9) True
10) pas correcte
11) Bonjoura
12) BonjourBoujour

#exercice 3

1) '21b'
2) 'aab'
3) 'ab'
4) 'bba'

#exercice 11
1) 'ababa'
2) 'babab'
"""
#exercice 4

def calcul(c, n):
    return c*n

#exercice 5

def calcul1(c, d, n, m):
    return c*n+ d*m

#exercice 6_1

def calcul2(ch, n):
    for i in range (1, n):
        print(calcul(ch, n))

#exercice 6_2

def calcul3(ch, n):
    for i in range (1, n):
        print(i, calcul( ch, n))

#exercice 7
def calcul4(c, n):
    for i in range (1, n+1):
        print(calcul(c, i))

#exercice 8
def premiere_occ(ch , c):
    return c in ch

#exercice 9
def nb_occ(ch, c):
    compteur = 0
    for caractere in ch:
        if caractere == c:
            compteur += 1
    return compteur
print(nb_occ("bonjour", "o"))

#exercice 10
def sous_chaine(ch1, ch2):
    return (ch1 in ch2) or (ch2 in ch1)

#exercice 12
def triple_six(ch):
    return nb_occ("666") >= 3

def triple_six__exact(ch):
    return '666'in ch and not ('6666' in ch)

#exercice 13
def mirroir(ch):
    inv = ""
    for e in ch:
        inv = e + inv
    return inv
print(mirroir("bonjour"))