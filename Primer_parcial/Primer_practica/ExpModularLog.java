/*
  ExponenciacionModularM.cpp
    Medina Juarez Jesus Booz
    Rios Altamirano Alam Yael
	Algoritmo de exponenciacion modular O(log m)
*/
package expmodular;

public class ExpModularLog {
    static int expmod(int a, int m, int n){
        int res = 1;
        a = a % n;
        while (m > 0){
            if((m & 1)==1)
                res = (res * a) % n;
            m = m >> 1; // m = m / 2
            a = (a * a) % n;
        }
        return res;
    }

    public static void main(String args[])
    {
        int a = 78;
        int m = 2;
        int n = 5;
        System.out.println(expmod(a, m, n));
    }
}
