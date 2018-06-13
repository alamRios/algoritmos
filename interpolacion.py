# interpolacion.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Interpolacion
def calcular(x):
    n= len(x)
    q=[0]*(n-1)
    q_aux=[]
    if n == 1:
        return -x[0],1
    x_aux=x[:-1]
    q_aux=calcular(x_aux)
    q[0]=-q_aux[n-1]
    for i in range(1,n-1):
        q[i]=q_aux[i-1]-q_aux[i]*n[x-1]
    return q
