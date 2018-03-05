# Python 2.7.13
# selectionSort.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de algoritmo merge sort

def mergesort(A):
    print A
    n = len(A)
    if n = 1:
        return A
    Ap = mergesort(A[:n/2])
    App = mergesort(A[n/2:])
    return merge(Ap,App)

def merge(L,R):
    R = []
    

A = [13,23,1,232]
print A,mergesort(A)

