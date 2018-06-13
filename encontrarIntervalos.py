# 30 de mayo del 2018
# Rios Altamirano Alam Yael
# Medina Juarez Jesus Booz
# Escoger el conjunto de intervalos que generan la mayor suma de pesos
import copy

global intervalos
intervalos = [{'nom':'c','ti':7,'tf':11,'w':2},
              {'nom':'b','ti':6,'tf':9,'w':3},
              {'nom':'a','ti':4,'tf':7,'w':2}]

#intervalos = [{'nom':'1','ti':0,'tf':3,'w':2},
#              {'nom':'2','ti':1,'tf':5,'w':4},
#              {'nom':'3','ti':3,'tf':6,'w':4},
#              {'nom':'4','ti':2,'tf':7,'w':7},
#              {'nom':'5','ti':6,'tf':8,'w':2},
#              {'nom':'6','ti':7,'tf':9,'w':1}]

global M
M = {}

def mergesort(A):
    n = len(A)
    if n == 1:
        return A
    Ap = mergesort(A[:n/2])
    App = mergesort(A[n/2:])
    return merge(Ap,App)

def merge(L,R):
    Re = []
    while len(L) > 0 and len(R) > 0:
        if L[0]['tf'] < R[0]['tf']:
            Re.append(L.pop(0))
        else:
            Re.append(R.pop(0))
    if len(L) > 0:
        Re += L
    elif len(R) > 0:
        Re += R
    return Re

def ordenarPorTiempoFin():
    return mergesort(intervalos)

def calcularP():
    Pp = {}
    intervalos_ = copy.copy(intervalos)
    while(len(intervalos_)>0):
        j = intervalos_.pop()
        encontrado = False
        for intervalo in intervalos_[::-1]:#lista de fin a inicio
            if intervalo['tf'] <= j['ti']:
                Pp[j['nom']] = intervalo['nom']
                encontrado = True
                break
        if not encontrado:
            Pp[j['nom']] = 0
    return Pp

def opt(intervalo):
    print intervalo
    if not intervalo or intervalo == 0 or not intervalos:
        return 0
    else:
        return max(opt(intervalos[-1]['nom']),intervalos[-1]['w'] + opt(P[intervalos]))

ordenarPorTiempoFin()
global P
P = calcularP()
print P
optima = opt(intervalos.pop()['nom'])
print optima
