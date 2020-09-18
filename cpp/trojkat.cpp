


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	float a;
	float b;
	float c;
	a = 0;
	b = 0;
	c = 0;
	cout << "Podaj pierwszy bok ";
	cin >> a;
	cout << "Podaj drugi bok ";
	cin >> b;
	cout << "Podaj trzeci bok ";
	cin >> c;
	
/*
 * 
	 if (a + b > c) {
		if(a + c > b){
			if (b + c > a){
				cout << "Z tych bokow mozna zbudowac trojkat";
			}
		}
	} else {
	
	cout << "Z tych bokow nie mozna zbudowac trojkata";
	}*/
	 if (a+b>c && a+c>b && b+c>a) {
	cout << "Można zbudować trojkat ";
	 } else {
		cout << "Nie da się";
	}
	
	
	return 0;
}
	
	

