#python 2.7.6

def mcd(a, b):
	if a < b:
		a, b = b, a
	while b != 0:
		r = a % b
		a, b = b, r
	return a
	
a, b = input(), input()
print mcd(a, b)