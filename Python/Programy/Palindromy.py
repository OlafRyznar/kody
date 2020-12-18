#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Palindromy.py
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


def Czypalindrom(str):
 
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
    
    
def main(args):
	
	s = (input("Podaj wyraz: "))
	ans =Czypalindrom(s)
 
	if (ans):
		print("To jest palindrom!")
	else:
		print("To nie jest palindrom!")
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
