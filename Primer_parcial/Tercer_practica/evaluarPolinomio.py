# evaluarPolinomio.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Algoritmo para evaluar un polinomio dado sus coeficientes

def evaluarPolinomio(A, x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p

A = [2,5,2]
x0 = 4

print 'a:',A,'x_0:',x0,"p(x_0):",evaluarPolinomio(A,x0)
