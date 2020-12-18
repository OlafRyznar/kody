#include <iostream>

using namespace std;

void biale(char t[])
{
    int i = 0;
    int x;
    x = 0;

    while(t[i] != '\0')
    {
        switch (t[i])
        { 
            case ' ': x++; break;
            case '\t': x++; break;
        }
        i++;
    }

    cout << "Ilość Znaków białych: " << x << endl;
}

int literki(char t[])
{
    int i = 0;
    int kod = 0;

    while(t[i] != '\0')
    {
        kod = (int)t[i];

        if (kod >= 65 && kod <= 90)
            kod += 32;
        else if (kod >= 97 && kod <= 122)
            kod -= 32;
        i++;
    }
    return char(kod);
}

int main(int argc, char **argv)
{
    int r = 50;
    char zdanie[r];

    cout << "Wpisz maksymalnie 50-znakowe zdanie: ";
    cin.getline(zdanie, r);

    biale(zdanie);
    cout << "Zdanie po zmianie wielkosci liter: " << char(literki(zdanie));


    return 0;
}
