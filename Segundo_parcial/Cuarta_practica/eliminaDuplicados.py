# Python 2.7.13
# eliminaDuplicados.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de algoritmo fuerza bruta
# para eliminar duplicados

def eliminaDuplicados(A):
    Res = []
    for a in A:
        existe = False
        for r in Res:
            if r == a:
                existe = True
        if not existe:
            Res.append(a)
    return Res
                
            

A = [1,0,-1,20,1,0,-20,-50,1]
print A,eliminaDuplicados(A)
