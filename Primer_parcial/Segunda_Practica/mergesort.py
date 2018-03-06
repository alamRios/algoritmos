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
    nL = len(L)
    nR = len(R)
    while nL > 0 and nR > 0:
        if L[len(L) - nL] < R[len(R) - nR]:
            Re.append(L[len(L) - nL])
            nL -= 1
        else:
            Re.append(R[len(R) - nR])
            nR -= 1
    if nL > 0:
        Re += L[-nL:]
    elif nR > 0:
        Re += R[-nR:]
    return Re

A = [13,23,1,232,8,0,2,134]
print A,mergesort(A)
