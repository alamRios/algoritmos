/*
  Multiplicador.cpp
    Medina Juarez Jesus Booz
    Rios Altamirano Alam Yael
  Multiplica dos numeros de la entrada
  Ejecutar el programa e ingresar los dos numeros
*/
#include <iostream>
using namespace std;
 int multiply(int x, int y);
 int main()
 {
 	int x, y;
 	cin >> x >> y;
 	cout << multiply(x, y);
 }

 int multiply(int x, int y){
 	if(y == 0)
 		return 0;
 	int z = multiply(x, y/2);
 	if(y%2 == 0)
 	 return 2*z;
 	return x + 2*z;
 }
