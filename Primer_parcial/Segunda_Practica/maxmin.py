# Python 2.7.13
# maxmin.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Busqueda de el maximo y el minimo en un arreglo

A = [-1,0,0,0,1]
print 'lista',A
maxmin = {'max':A[0],'min':A[0]}
for i in range(0,len(A)):
    if A[i] < maxmin['min']:
        maxmin['min'] = A[i]
    if A[i] > maxmin['max']:
        maxmin['max'] = A[i]
print maxmin
