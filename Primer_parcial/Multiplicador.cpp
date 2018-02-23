#include <iostream>
using namespace std;
 //Compiler version g++ 6.3.0

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