/*
 * funkcje02.cpp
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

using namespace std;


int a = 0;  //zmienna globalna
int b = 0;

void sumuj(int a, int b){
	a = 20;
	cout << &a << endl;
	int suma = a + b;
	cout << "suma " << suma << endl;
	
	
	}
	
void sumuj2(int &a, int b){
	a = 20;
	int suma = a + b;
	cout << "suma " << suma << endl;
}




int main(int argc, char **argv)
{
	int a = 0;
	int b = 0;
	cout<< "Podaj liczby "<< endl;
	cin>> a;
	cin>> b;
	
	sumuj(a, b); //wywolanie funkcji
	
	cout << &a << endl;
	cout << "a = " << a << endl;
	
	return 0;
}

