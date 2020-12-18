#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax2.py
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

from random import randint

def minmax2(lista):

    min = lista[0]
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < min:
            min=lista[i]
        if lista[i] > max:
            max=lista[i]
    return min, max

def minmax1(tab,n):
    tbmin=[]
    tbmax=[]

    for i in range(0,n,2):
        if tab[i] > tab[i+1]:
            tbmax.append(tab[i])
            tbmin.append(tab[i+1])
        else:
            tbmax.append(tab[i+1])
            tbmin.append(tab[i])
    return tbmin,tbmax


def losuj(ile, zakres, lista):
    for i in range(ile):
        lista.append(randint(0, zakres))

def main(args):
    ile=21
    zakres=50
    lista = []
    losuj(ile-1, zakres, lista)
    lista.append(-1)
    print("Wylosowane liczby:\n",lista)
    print(f"minimum: {min(lista,ile)}. Maksimum: {max(lista,ile)}.")

    if ile%2:
        tbmin, tbmax = minmax1(lista, ile-1)
    else:
        tbmin, tbmax = minmax1(lista, ile)

    print(tbmin)
    print(tbmax)
    min_el=min(tbmin, len(tbmin))
    max_el=max(tbmax, len(tbmax))

    if ile % 2:
        ost_el = lista[ile-1]
        if ost_el > max_el:
            max_el = ost_el
        elif ost_el < min_el:
            min_el = ost_el


    print(f"Minimum: {min_el}. Maksimum: {max_el}.")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
