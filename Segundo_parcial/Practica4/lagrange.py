#Medina Juarez Jesus Booz
#Rios Altamirano Alam Yael
#Interpolacion de Lagrange

from itertools import *
from numpy import convolve
import numpy as np
f = open('puntos.txt','r')
a = f.readlines()
for i in range(0,len(a)):
    a[i] = a[i].replace('\n','')
    a[i] = tuple(map(int,a[i].split(',')))
print a
x = [x[0] for x in a]
y = [y[1] for y in a]
print x
print y

def multiplicarpolinomios(A, B):
    len_a = len(A)
    len_b = len(B)
    producto_len = len_a + len_b
    producto = [0]*(producto_len-1)
    for i in range(len_a):
        for j in range(len_b):
            producto[i+j] += A[i] * B[j]
    return producto

def lagrange(x,y):
    interpolacion = []
    numerador = []
    n = len(x)
    print n
    denominador = [1.0] * (n)
    for i in range(0, n):
        numerador_aux = []
        for j in range(0, n):
            if i != j:
                denominador[i] *= x[i]-x[j]
                numerador_aux.append([-x[j],1])
        denominador[i] /= y[i]
        numerador.append(numerador_aux)
    multiplicacion = []
    multiplicaciones =[]
    print numerador
    for l in range(0,n):
        multiplicacion=multiplicarpolinomios(numerador[l][0], numerador[l][1])
        for m in range(2,n-1):
            multiplicacion=multiplicarpolinomios(multiplicacion, numerador[l][m])
        multiplicaciones.append(multiplicacion)
    print multiplicaciones
    print denominador
    for i in range(0, n):
        for j in range(0, n):
            multiplicaciones[i][j] = multiplicaciones[i][j]/denominador[i]
    interpolacion=np.sum(multiplicaciones, axis=0)  
    return interpolacion

print lagrange(x,y)
