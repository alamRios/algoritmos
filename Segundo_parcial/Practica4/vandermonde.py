# vandermonde.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de matriz de vandermonde

import math

def raizparakn(k,n):
    cos = round(math.cos(2*math.pi*k/n),3)
    sen = round(math.sin(2*math.pi*k/n),3)
    return complex(cos,sen)

def raizparan(N):
    raices = []
    for n in range(0,N):
        raices.append(raizparakn(n,N))
    return raices

def vandermonde(X,raicesDeLaUnidad,N):
    V = []
    for n in range(0,N):
        Vn = []
        Vn.append(1)
        for i in range(1,N):
            Vn.append(raicesDeLaUnidad[n] ** i)
        V.append(Vn)
    return V
    

n = 4
raicesDeLaUnidad = raizparan(n)
X = [1,2,3]

vander = vandermonde(X,raicesDeLaUnidad,n)
for lista in vander:
    print lista
