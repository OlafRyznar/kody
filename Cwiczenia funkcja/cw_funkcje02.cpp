#include <iostream>
using namespace std;

void srednia(float suma, float iloscliczb){
    float srednia = suma / iloscliczb;
    cout <<"Srednia wynosi: "<< srednia <<endl;
}

void mediana(float *tab, int iloscliczb){
    float m;
    if(iloscliczb % 2 ==0){
        m = (tab[iloscliczb/2 - 1]+tab[iloscliczb/2])/2;
    } else {
        m = tab[iloscliczb/2];
    }
    cout <<"Mediana wynosi: " << m << endl;
}

int main(int argc, char **argv)
{

	int t =0;
	int iloscliczb =0;
	int *tab = new int [iloscliczb];
	cout <<"Podaj ilosc ocen: ";
	cin >>iloscliczb;

	if(iloscliczb >20){
		cout <<"Maksymalna ilosc ocen to 20" <<endl;
		return 0;
}

	float tablica[iloscliczb];
	int suma = 0;
	for (int i = 0; i < iloscliczb; ++i)
    {
		cout <<"Podaj ocene "<<(i+1)<<" : ";
		cin >>tablica[i];
		if(tablica[i] <1 || tablica[i] >6){
			cout <<"Wprowadzono zla ocene"<<endl;
			return 0;
        }
		suma += tablica[i];
    }
	int v;
	int x;
	for(v=0;v<iloscliczb;v++)
    	{
			for(x=v+1;x<iloscliczb;x++)
    		{
    			if(tablica[v]>tablica[x])
    			{
    				t  =tablica[v];
    				tablica[v]=tablica[x];
    				tablica[x]=t;
    			}
    		}
    	}
    srednia(suma, iloscliczb);
    mediana(tablica, iloscliczb);


	return 0;
}
