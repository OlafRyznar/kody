#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alg_warunkowy.py
#  
#  Copyright 2020  <>
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


def main(args):
	
	a = int(input("Podaj wynik: "))
	if (a>60 or a<0):
			print ("Bledne dane")
	elif (a<20):
			print ("Podstawowy")
	elif (a <= 20 or a<=40):
			print ("Sredniozaawansowany")
	elif (a >=60):
			print ("Zaawansowany")
	
	
		

	
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
