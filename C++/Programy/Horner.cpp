#include <iostream>
using namespace std;

void drukujw(int n, float tbwsp[]) {
    int i = 0;
    for (i = 0; i < n; i++) {
        cout << tbwsp[i] << "x^" << n-i << " + ";
    }
    cout << tbwsp[i] << endl;

}

float horner_it(int n, float tbwsp[], float x)
{
    float wynik = tbwsp[0];
    for (int i = 1; i < n + 1; i++)
    { 
        wynik = wynik * x + tbwsp[i];
      
    }
    return wynik;

}
int main(int argc, char **argv)
{
    int n = 0; 
    float x = 0;
    cout << "Stopien: ";
    cin >> n;
    float tbwsp[n + 1];
    for (int i = 0; i <= n; i++) {
        cout << "Wspolczynnik przy potedze " << i+1 << ": ";
        cin >> tbwsp[i];
    }
    cout << "Argument: ";
    cin >> x;

    drukujw(n, tbwsp);
    cout << "Wynosi: " << horner_it(n, tbwsp, x) << endl;
    return 0;
}
