# Python 2.7.13
# mergeSort.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de algoritmo merge sort

def mergesort(A):
    n = len(A)
    if n == 1:
        return A
    Ap = mergesort(A[:n/2])
    App = mergesort(A[n/2:])
    return merge(Ap,App)

def merge(L,R):
    Re = []
    LRigualTam = 0
    n = len(L)
    if(len(R) != len(L)):
        if len(R) > len(L):
            LRigualTam = 1
        else:
            LRigualTam = 2
            n = len(R)
    for i in range(0,n):
        if L[i] < R[i]:
            Re.append(L[i])
            Re.append(R[i])
        else:
            Re.append(R[i])
            Re.append(L[i])

    if LRigualTam == 1:
        Re += R[n:]
    elif LRigualTam == 2:
        Re += L[n:]
        
    return Re

A = [13,23,1,232,8]
print A,mergesort(A)
