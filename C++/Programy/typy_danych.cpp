#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
   int b;
   long int c;
   short unsigned int a;
   cout << a << " " << sizeof(a) << endl;
   cout << b << " " << sizeof(b) << endl;
   cout << c << " " << sizeof(c) << endl;

   char z = 'a';
   cout << z << " " << (int)z << " " << sizeof(z) << endl;

   float d = 0;
   double e = 0;
   cout << d << " " << sizeof(d) << endl;
   cout << e << " " << sizeof(e) << endl;

   cout << "Uzycie tablic";

   int ile = 5;
   int tab[ile];
   for (int i=0; i<ile ; i++) {
        cout << "Podaj" << i+1 << "liczbe";
        cin >> tab [i];
   }

   cout << "Zawartosc tablicy" << endl;
   for (int i=0; i<ile ; i++) {
        cout << "Indeks: " << i << "Wartosc: " << tab [i] <<endl;

   }
   return 0;
}
