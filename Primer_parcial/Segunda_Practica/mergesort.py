# Python 2.7.13
# selectionSort.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de algoritmo merge sort

def mergesort(A):
    n = len(A)
    if n == 1:
        return A
    Ap = mergesort(A[:n/2])
    if n%2 != 1:
        App = mergesort(A[n/2:])
        return merge(Ap,App)
    else:
        App = mergesort(A[n/2:n-1])
        res = []
        res.append(A[-1])
        return merge(merge(Ap,App),res)

def merge(L,R):
    Re = []
    for i in range(0,len(L)):
        if L[i] < R[i]:
            Re.append(L[i])
            Re.append(R[i])
        else:
            Re.append(R[i])
            Re.append(L[i])
    return Re

A = [13,23,1,232,8]
print A,mergesort(A)
