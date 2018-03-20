def karatsuba(x,y):
    xlen = len(str(x))
    ylen = len(str(y))

    maxlen = max(xlen,ylen)
    if maxlen < 10:
        return x*y
    N = maxlen/2
    multiplicador = 2**N
    a = x/multiplicador
    b = x%multiplicador
    c = y/multiplicador
    d = y%multiplicador

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    res = karatsuba(a+b,c+d)
    result = ac*(2**N) + bd + res*(2**(N/2))
    return result

print karatsuba(1100,1010)
    
