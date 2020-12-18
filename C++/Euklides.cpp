#include <iostream>

using namespace std;

int euklides(int a, int b)
{   
    int licznik=0;
    
    do
     {
        a = a % b;
        b = b - a;
        licznik++;
    }
    while (a > 0);
    
    
    cout << "Powtorzen: " << licznik << endl;
    return b;
}
int euklides2(int a, int b)
{
    int licznik=0;
    
    do
    {
		if (a > b)
        {
			a = a - b;
            licznik++;
		}
        else
        {
			b = b - a;
            licznik++;
        }
    }
    while(a!=b);
    
     
    cout << "Powtorzen: " << licznik << endl;
    return a;
}

int main(int argc, char **argv)
{
	int a=0, b=0;
   
    
    cout << "Podaj liczbe: ";
    cin >> a;
            
    cout << "Podaj kolejna liczbe: ";
    cin >> b;

    cout  <<  euklides(a, b)<< endl;
    cout  << euklides2(a, b)<< endl;
    

	return 0;
}
