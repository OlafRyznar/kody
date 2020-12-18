
#include <iostream>

using namespace std;

int fib_it(int n)
{
	int wynik, a = 0;
	int b = 1;
	
	for (int i=1; i<n+1;i++)
	{ 
		wynik = a+b;
		a=b;
		b=wynik;
	}
	return wynik;
}

int main(int argc, char **argv)
{
	int n;
	cout << "Ktory wyraz?";
	cin >> n;
	
	for(int i = 0;i<n+1; i++)
	{
		if (i>1)
			cout << "fib_it(" << i << "): " << fib_it(i) << " " << (float)fib_it(i)/fib_it(i-1)<< endl;
		else
			cout << "fib_it(" << i << "): " << fib_it(i) << endl;
	}
	
	return 0;
}

