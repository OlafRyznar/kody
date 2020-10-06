
#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int bok1;
	int bok2;
	int pole;
	int obwod;
	bok1 = 0;
	bok2 = 0;
	pole = 0;
	cout << "Podaj pierwszy bok prostokąta: ";
	cin >> bok1;
	cout << "Podaj drugi bok prostokąta: ";
	cin >> bok2;
	pole = bok1 * bok2;
	cout << "Pole prostokąta: " << pole << endl;
	obwod = bok1 * 2 + bok2 * 2;
	cout << "Obwód: " << obwod;
	
	return 0;
}

