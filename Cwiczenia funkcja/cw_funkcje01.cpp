#include <iostream>
using namespace std;

void awans(int &staz, int &zarobek, int lata){

	for(int i=1; i<lata; i++){
		staz += 1;
		zarobek = zarobek + 0.1*zarobek;
	}
}

void drukuj(int staz, int zarobek){
	cout << "Po " << staz << " latach pracy bedziesz zarabiac: " << zarobek << endl;
}

int main(int argc, char **argv)
{
	int staz = 1;
	int zarobek = 1000;
	int lata = 0;

	cout << "Podaj przewidywane lata pracy: ";
	cin >> lata;

	awans(staz, zarobek, lata);
	drukuj(staz,zarobek);
	return 0;
}
