/*
 * BMI.cpp
 *
 * Copyright 2020 olaf5 <olaf5@DESKTOP-T1JQ8NP>
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

int main(int argc, char **argv)
{
	float waga;
	float wzrost;
	float bmi;

	wzrost = 0;
	waga = 0;
	bmi =  0;

	cout <<"Podaj swoja wage [kg]: ";

	cin>>waga;

	cout<<"Podaj swoj wzrost[cm]: ";

	cin>>wzrost;


	wzrost = wzrost/100;

	bmi = waga/(wzrost*wzrost);


	cout<<bmi<<endl;
	if (bmi < 0) {
		cout<<"Bledne dane";

	return 0;
}
{	if (bmi <18.5)
		cout<<"Niedowaga";
    else if (bmi < 25)
		cout<<"BMI w normie";
    else if (bmi < 30)
		cout<<"Nadwaga";
    else
		cout<<"Otylosc";


	return 0;
}
}



