#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  listy_cw2.py
#  
#  Copyright 2020 Karol <Karol@DESKTOP-EDM589B>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def liczby(lista):
	for i in range(5):
		liczba1 = int(input("Podaj liczbe: "))
		lista.append(liczba1)
						
def suma(lista1, lista2):
	suma1 = 0
	suma2 = 0
	for liczba1 in lista1:
		suma1+= liczba1
	for liczba1 in lista2:
		suma2+= liczba1

	
		
	return suma1,suma2
			

def main(args):
	lista1 = [] 
	lista2 = []
	liczby(lista1)
	print("Podaj druga serie")
	liczby(lista2)
	print(lista1)
	print(lista2)
	suma1, suma2 =suma(lista1, lista2)
	print("Suma w tablicy pierwszej: ", suma1)
	print("Suma w tablicy drugiej: ", suma2)
	if suma1>suma2:
		print("Lista pierwsza jest większa od listy drugiej")
	elif suma1<suma2:
		print("Lista druga jest większa od listy pierwszej")
	else:
		print("Lista druga jest rowna liscie pierwszej")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
