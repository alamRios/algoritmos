# Python 2.7.13
# selectionSort.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Implementacion de algoritmo selection sort

A = [50,34,2,0,-5]
print A
for i in range(0,len(A)):
    min = i
    for j in range(i+1,len(A)):
        if A[j] < A[i]:
            min = j 
    A[i],A[min] = A[min],A[i]
print A
