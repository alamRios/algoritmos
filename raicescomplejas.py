# Rios Altamirano Alam Yael
# Medina Juarez Jesus Booz
# raicescomplejas.py

import math

N = 4

def raizparakn(k,n):
    cos = round(math.cos(2*math.pi*k/n),3)
    sen = round(math.sin(2*math.pi*k/n),3)
    return complex(cos,sen)

def raizparan(N):
    raices = []
    for n in range(N):
        raices.append(raizparakn(n,N))
    return raices

print raizparan(N)
