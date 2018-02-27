/*
  ExponenciacionModularM.cpp
    Medina Juarez Jesus Booz
    Rios Altamirano Alam Yael
	Algoritmo de exponenciacion modular O(m)
*/
#include<iostream>
#include <stdlib.h>


using namespace std;

int obt();
int expo(int a, int m, int n);

int main(){
	obt();
	return 0;
}

int obt(){
	int a=0, m=0, n =0, r;
	cin>>a;
	cin>> m;
	cin>> n;
	cout<<expo(a,m,n);
return 0;
}

int expo(int a, int m, int n){
	if(n==1)
	return 0;
	int aux=1;
	for(int i = 0; i<m ; i++){
		aux=(aux*a)%n;
	}

	return aux;
}
