#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Anagramy.py
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

def czyanagram(x,y):
    for i1 in range(0, x):
        for i2 in range(0, x):
            if i1 == i2:
                continue
            for i3 in range(0, x):
                if i3 == i1 or i3 == i2:
                    continue
                i4 = 6 - i1 - i2 - i3
                
            print(y[i1], y[i2], y[i3], y[i4])


def main(args):
	
    y=input("Podaj wyraz: ")
    x=5 
    
    czyanagram(x-1,y)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
