#include <iostream>


using namespace std;

void pobierz(int tablica[], int ile) {
	int ocena = 0;
	for (int i = 0; i < ile; i++){
		cout << "Podaj ocene: ";
		cin >> ocena;
		if (ocena > 0 && ocena <7)
			tablica[i] = ocena;
		else {
            cout << "Bledne dane, sproboj ponownie" << endl;
			i--;
		}



	}

}

float Srednia(int t[], int ile){
	float suma = 0;
	for (int i = 0; i< ile; i++){
	suma += t[i];
	}
	return suma/ile;
}


void drukuj(int tablica[], int ile){
	for (int i = 0; i< ile; i++){
		cout << "Indeks: " << i << " Wartosc: " << tablica[i] << endl;
}
}




int main(int argc, char **argv)
{
	int ile = 0;
	cout << "Liczba ocen ktora podasz: ";
	cin >> ile;

	int oceny[ile];

	pobierz(oceny, ile);
	drukuj(oceny, ile);

	cout << "Srednia podanych ocen to " << Srednia(oceny, ile) << endl;

	return 0;
}

