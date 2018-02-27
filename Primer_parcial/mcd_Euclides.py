# Archivo: mcd_Euclides.py
# Autores:
#       Medina Juarez Jesus Booz
#       Rios Altamirano Alam Yael
# Calcula el minimo comun multiplo de dos numeros
# utilizando el algoritmo de Euclides
# Forma de ejecución:
# Ejecutar el codigo e ingresar un numero,
# dar enter e ingresar el otro antes del siguiente enter

def mcd(a, b):
	if a < b: #Identificar al mayor
		a, b = b, a 
	while b != 0:
		r = a % b
		a, b = b, r
	return a
	
a, b = int(raw_input()), int(raw_input())
print mcd(a, b)
