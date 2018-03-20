# Python 2.7.13
# multipol_1.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Algoritmo por fuerza bruta para multiplicar
# polinomios de igual grado
def multiplicarpolinomios(A, B):
    C = [0] *((len(A)*2)-1)
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            C[i+j]+=(A[i]*B[j])
    return C

A=[1, 3, 2, 2, 4, 1]
B=[3, 2, -1, 3, 8, 9]
print(multiplicarpolinomios(A, B))
