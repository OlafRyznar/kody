#include <iostream>
using namespace std;
void liczenieznakow(char tab[])
{
    int i = 0;
    int biale;
    biale =0;

    while(tab[i] != '\0')
    {
         switch (tab[i])
        { 
            case ' ': biale++; break;
            case '\t': biale++; break;
        }
        i++;
    }
    cout << "Liczba znakow bialych: " << biale << endl;
}
void zmienianieliter(char tab[])
{
    int i = 0;
    int znak = 0;

    while(tab[i] != '\0')
    {
        znak = (int)tab[i];

        if (znak >= 65 && znak<= 90)
            znak += 32;
        else if (znak >= 97 && znak <= 122)
            znak -= 32;
        cout << (char)znak;
        i++;
    }
}
int main(int argc, char **argv)
{
    int r = 50;
    char znaki[r];
    cout << "Wprowadz znaki(max 50): ";
    cin.getline(znaki, r);
    
    liczenieznakow(znaki);
    cout << "Zmienione znaki: ";
    zmienianieliter(znaki);
    return 0;
}
