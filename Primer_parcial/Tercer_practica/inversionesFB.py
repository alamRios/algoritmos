# inversionesFB.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Algoritmo por fuerza bruta para encontrar inversiones
# -> i < j -> A[i] > A[j]

def inversiones(A):
    indices = []
    for i in range(0,len(A)-1):
        for j in range(i+1, len(A)):
            if(A[i] > A[j]):
                indices.append((i,j))
    return indices

A = [2,4,1]
print 'A:',A,'inversiones:',inversiones(A)
