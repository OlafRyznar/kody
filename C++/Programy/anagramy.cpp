/*
 * anagramy.cpp
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


void anagramy(char w[], int r) {
		int i1,i2,i3,i4;
		for (i1 = 0; i1 <r; i1++) {
			for (i2 = 0; i2 <r; i2++) {
				if (i1 == i2) continue;
				for (i3 = 0; i3 <r; i3++) {
					if (i1 == i3 or i2 == i3) continue;
					// i4= 6- i1 + i2 +i3;
						for (i4 = 0; i4 <r; i4++) {
							if (i1 == i4 or i2 == i4 or i3 == i4) continue;
				cout <<w[i1] <<w[i2] << w[i3] << w[i4] <<endl;
					}
				}
			}
	}
}

				
				
				
int main(int argc, char **argv)
{
	int r = 5;
	char wyraz[r];
	cin.getline(wyraz, r);
	cout<<wyraz<<endl;
	anagramy(wyraz, r-1);
	
	return 0;
}

