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
#exercice 14
1)2.3
2)5
3)out of range
4)7
5)not correct
6)not fcorrect
7)2.3, 4.1, 4, 2.55, 5
8)4, 2.55
9)8.1
10)4, 4.1
11)3
12)4, 4, 4
13)false
14)True
15)True
16)True
#exercice 15
1)
2)
3)
4)
5)
6)
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
    a = len(ch)
    b = len(c)
    for i in range(1, a+1):
        if ch[i: i+b] == c:
            return i

print(premiere_occ("bonjour", "n"))

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
print(sous_chaine("bon", "bonjour"))
#exercice 12
def triple_six(ch):
    return nb_occ("666") >= 3

def triple_six__exact(ch):
    return '666'in ch and not ('6666' in ch)


def triple_six_exact2 ( ch ) :
   n = len( ch )
   if ch[0:3] == "666" and (n == 3 or ch[3] != "6"):
      return True
   if ch[n-3:n] == "666" and ch[n-4] != "6":
      return True
   for k in range(1, n-3):
      if ch[k:k+3] == "666" and ch[k-1] != "6" and ch[k+3] != "6":
         return True
   return False

#exercice 13
def mirroir(ch):
    inv = ""
    for e in ch:
        inv = e + inv
    return inv

def palindrome(ch):
    return ch == ch[::-1]

def sans_espace(ch):
    ch_sans_espace = ""
    for e in ch:
        if e != " ":
            ch_sans_espace += e
    return ch_sans_espace
def palindrome2(ch):
    print(palindrome(sans_espace("engage le jeu que je le gagne")))

#exercice 17
"""
L = []
for k in range(1, 101):
    L += [k]
print(L)

L = []
for k in range(1, 101):
    L.append(k)
print(L)

L = 100 * [0]
for k in range(100):
    L[k] = k + 1
print(L)
"""
def mult_2_L(n):
    L = []
    for k in range(n):
        L.append(2 * (k + 1))
    return L
def carres(n):
    L = []
    for k in range(1, n + 1):
        L.append(k * k)
    return L
def carre_comprenant(n):
    return [k * k for k in range(1, n+1)]
print(carre_comprenant(15))
#exercice 18

def liste_impairs(n):
    L = []
    for k in range(n):
        if k % 2 != 0:
            L.append(k)
    return L

def carres(n):
    L = []
    for k in range(1, n + 1):
        L.append(k * k)
    return L
def carre_comprenant():
    return [k * k for k in range(1, 11)]

def puissances_2(n):
    return [2**k for k in range(n)]

def trois_en_trois(n):
    return [k for k in range(n) if k % 3 == 0]

#exercice 19
