/*
 * cwiczenie2.cpp
 *
 *
 *
 */


#include <iostream>

using namespace std;


void srednia_art(float suma, int iloscliczb){
    float srednia = suma / iloscliczb;
    cout <<"Srednia wynosi: "<< srednia <<endl;
}

void mediana(float *u, int iloscliczb){
    float mediana;
    if(iloscliczb % 2 ==0){
        mediana = (u[iloscliczb/2 - 1]+u[iloscliczb/2])/2;
    } else {
        mediana = u[iloscliczb/2];
    }
    cout <<"Mediana wynosi: " << mediana << endl;
}


int main(int argc, char **argv)
{

    int z =0;
    int iloscliczb =0;
    int *u = new int [iloscliczb];
    cout <<"Podaj ilosc ocen: ";
    cin >>iloscliczb;

    if(iloscliczb >20){
        cout <<"Wpisales wiecej niz 20 ocen!" <<endl;
        return 0;
}

    float tablica[iloscliczb];
    int suma = 0;
    for (int i = 0; i < iloscliczb; ++i)
    {
        cout <<"Podaj ocene "<<(i+1)<<" : ";
        cin >>tablica[i];
        if(tablica[i] <1 || tablica[i] >6){
            cout <<"Wprowadzono niepoprawna ocene"<<endl;
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
    				z  =tablica[v];
    				tablica[v]=tablica[x];
    				tablica[x]=z;
    			}
    		}
    	}
    srednia_art(suma, iloscliczb);
    mediana(tablica, iloscliczb);


	return 0;
}

