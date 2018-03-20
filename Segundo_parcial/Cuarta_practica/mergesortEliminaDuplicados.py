# Python 2.7.13
# mergeSortEliminaDuplicados.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de algoritmo merge sort
# que a su vez elimina duplicados

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
        if L[0] == R[0]:
            Re.append(L.pop(0))
            R.pop(0)
        elif L[0] < R[0]:
            Re.append(L.pop(0))
        else:
            Re.append(R.pop(0))
    if len(L) > 0:
        Re += L
    elif len(R) > 0:
        Re += R
    return Re

A = [1,0,-1,20,1,0,-20,-50]
print A,mergesort(A)
