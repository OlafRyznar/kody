#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazwy.py
#  
#  Copyright 2020 olaf5 <olaf5@DESKTOP-HMNH6DK>
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

def euklides2(a, b):
    i = 0
    while a > 0:
        i = i+1
        a = a % b
        b= b - a
        print("Powtórzeń: ", i)
    return b


def euklides1(a,b):

    licznik = 0

    while a != b:
        if a > b:
            a = a - b
            licznik += 1
        else:
            b = b - a
            licznik += 1

    print("Liczba powtórzeń: ", licznik)

    return a

def main(args):
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print(f"NWD({a}, {b} wynosi", euklides1(a,b))
    print (euklides2(a, b))
    return 0
