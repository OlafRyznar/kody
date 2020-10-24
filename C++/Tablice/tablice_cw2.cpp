#include <iostream>


using namespace std;

void liczby(int t[]) {
    int liczba1 = 0;
    for (int i = 0; i<5; i++){
        cout << "Podaj liczby ";
        cin >> liczba1;
        t[i] = liczba1;
    }
}

int suma(int t[]){
    float suma = 0;
    for (int i = 0; i<5; i++){
        suma+= t[i];
    }
    return suma;
}

int main(int argc, char **argv)
{
	int i = 5;
    int t1[i];
    int t2[i];
    int suma1;
    int suma2;
    liczby(t1);
    cout << "Podaj druga serie liczb" << endl;
    liczby(t2);
    suma1 = suma(t1);
    suma2 = suma(t2);
    cout << "Suma 1 wynosi: " << suma1 << endl;
    cout << "Suma 2 wynosi: " << suma2 << endl;
    for (int i = 0; i<5; i++){
		cout <<  t1[i] << endl;
	}
	for (int i = 0; i<5; i++){
		cout << t2[i] << endl;
	}
	if(suma1>suma2)
		cout << "Suma elementow pierwszej serii jest wieksza od sumy drugiej" << endl;
	else if (suma1<suma2)
		cout << "Suma elementow drugiej serii jest wieksza od sumy pierwszej" << endl;
    else
        cout << "Suma elementow drugiej serii jest rowna sumie pierwszej" << endl;


}

