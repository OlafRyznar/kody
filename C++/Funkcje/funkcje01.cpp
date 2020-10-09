/*
 * funkcje01.cpp
 * 
 * Copyright 2020  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <cmath>
using namespace std;

void sumuj(int a, int b) {
	int suma = a+b;
    cout<< "suma: " <<suma << endl;
	}
	
	
	
int potega(int podstawa, int wykladnik){
	int wynik = pow(podstawa, wykladnik);
	return wynik;
	}

int main(int argc, char **argv)
{
	int liczba1 = 0;
	int liczba2 = 0;
	cout<<"podaj liczby: " <<endl;
	cin>> liczba1;
	cin>> liczba2;
	
	sumuj(liczba1, liczba2);
	cout << potega(liczba1, liczba2) << endl;
	return 0;
}

