#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tablice_cw1.py
#  
#  Copyright 2020 olaf5 <olaf5@DESKTOP-T1JQ8NP>
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


def pobierz(lista, ile):
	while ile > 0:
		ocena = int(input("Podaj ocenę: "))
		if ocena > 0 and ocena <7:
			lista.append(ocena)
			ile -= 1
		else:
			print("Błędne dane")	
		

def Srednia(lista):
	suma = 0
	for ocena in lista:
		suma+= ocena
	return suma/ len(lista)


def main(args):
	ile = int(input("Podaj ilosc ocen: "))
	lista = [] 
	pobierz(lista , ile)
	
	print(lista)
	print("Średnia wynosi: ",Srednia(lista))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
