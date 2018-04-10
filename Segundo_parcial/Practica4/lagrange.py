f = open('coeficientes.txt','r')
a = f.readlines()
for i in range(0,len(a)):
    a[i] = a[i].replace('\n','')
    a[i] = tuple(a[i].split(','))
print a
