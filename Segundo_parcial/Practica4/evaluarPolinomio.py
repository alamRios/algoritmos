# evaluarPolinomio.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Algoritmo para evaluar un polinomio en valores aleatorios dado sus coeficientes

from random import *

def evaluarParaX(A,x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p

def evaluarParaAleatorios(a):
    c = []
    x = 0
    for x_i in range(0,len(a)+1):
        x = randint(1,100)
        c.append((x,evaluarParaX(a,x)))
    return c

a = [1,2,3,4]
f = open('coeficientes.txt','w')
res = evaluarParaAleatorios(a)
for tupla in res:
    reg = str(tupla[0]) + ',' + str(tupla[1])
    print reg
    f.write(reg)
    f.write('\n')
f.close()
