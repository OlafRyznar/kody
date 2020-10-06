#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje01.py

def sumuj(a, b):
    suma = a+b
    print ("suma: ",suma)


def odejmij(a,b):
    roznica = a-b
    print ("roznica: ", roznica)
    
    
def pomnoz(a,b):
    iloczyn = a*b
    print ("iloczyn: ", iloczyn)


def podziel(a,b):
    iloraz = a/b
    print ("iloraz: ", iloraz)


def poteguj(a,b):
    potega = a**b
    return potega


def main(args):
    liczba1 = int(input("Podaj liczbę:"))
    liczba2 = int(input("Podaj liczbę:"))

    odejmij(liczba1, liczba2)
    sumuj(liczba1,liczba2)
    pomnoz(liczba1, liczba2)
    podziel(liczba1,liczba2)
    print (poteguj(liczba1,liczba2))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
