# Python 2.7.13
# expmodularrapida.py
# Medina Juarez Jesus Booz
# Rios Altamirano Alam Yael
# Algoritmo de exponenciacion modular a^m mod n

def exponenciacion(a,m,n):
    res = 1
    a = a % n
    while m > 0:
        if m%2 != 0:
            res = res*a % n
        m = m>>1
        a = a*a % n
    return res
a,m,n = 5,2,2
print 'a:',a,'m:',m,'n:',n
print exponenciacion(a,m,n)
            
