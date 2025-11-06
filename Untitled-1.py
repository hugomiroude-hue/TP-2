import math
n = 0

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

#exercice 9
def nb_occ(ch, c):
    compteur = 0
    for caractere in ch:
        if caractere == c:
            compteur += 1
    return compteur

#exercice 10
def sous_chaine(ch1, ch2):
    return (ch1 in ch2) or (ch2 in ch1)

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
def indices (ch , c) :
    return  [i for i in range(len(ch)) if ch [i] == c]

#exercice 20
def sous_liste(L1, L2):
    return L2 in L1

#exercice 21
def tous_positifs (L) :
    for e in L:
        if e <0:
            return False
        
#exercice 22
def positifs (L) :
    c = 0
    for e in L :
        if e >= 0:
            c += 1
    return c

def rangs_negatifs (L):
    return [i for i in range(len(L)) if L [i] < 0]

def motif (L) :
    n = len(L)
    for k in range(n -1) :
        if L [k] == 0 and L [k +1] == 0:
            return True
    return False

def dix_vingt (L) :
    for e in L :
        if e <0 or e >20:
            return False
    return True

#exercice 23
def croissante (L) :
    n = len(L)
    for k in range (0 , n -1) :
        if L [ k ] > L[ k +1]:
            return False
    return True

#exercice 24
def monotone (L) :
    M = []
    for e in L :
        M += [e]
    return croissante (L) or croissante (M)

#exercice 25
def suite (n) :
    L =[1]
    for i in range(n) :
        L.append(L[i] ** 2+ i )
    return L

#exercice 26
def valeur_absolue (L) :
    return [abs(L[i]) for i in range(len(L))]

#exercice 27
def E_et_sigma ( valeurs , proba ) :
    l = len( valeurs )
    a = 0
    b = 0
    for i in range(n):
        aE += valeurs[i] * proba[i]
        b += valeurs[i] ** 2 * proba[i]
    b -= a ** 2
    S = math.sqrt(b)
    return a, S

#exercice 28
"""
1) 5 3 3
2) ['a', 2, 3]
[1, 2, 3]
3) [4, 3.14, True]
[4, 3.14, True]
4) 
[0, 0, 0] [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
[1, 0, 0] [[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
[1, 0, 0] [[1,0,0],[1,0,0],[2,3,4],[1,0,0]]
[1, 0, 11] [[1,0,11],[1,0,11],[2,3,4],[1,0,11]]
[1, 0, 11] [[1,0,11],[1,0,11],[2,'n',4],[1,0,11]]
5) 
[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
[[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
[[1,0,0],[1,0,0],[2,3,4],[1,0,0]]
[[1,0,11],[1,0,11],[2,3,4],[1,0,11]]
[[1,0,11],[1,0,11],[2,'n',4],[1,0,11]]
6)
[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
[[0,0,0],[1,0,0],[0,0,0],[0,0,0]]
[[0,0,0],[1,0,0],[2,3,4],[0,0,0]]
[[0,0,0],[1,0,0],[2,3,4],[0,0,11]]
[[0,0,0],[1,0,0],[2,'n',4],[0,0,11]]

# exercice 29
1) pour X = 3 a = 9
2) pour X = 3 a = 9
3) pour X = 3 a = 9

"""
#exercice 30 
M = [0 , 0 , 0]
N = 4*[ M]
print(M , N )
N [1][0] = 1
print(M , N )
N [2] = [2 , 3 , 4]
print(M , N )
N [3][2] = 11
print(M , N )
N [2][1] = 'n'
print(M , N )
