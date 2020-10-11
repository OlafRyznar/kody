#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje02.py

a= int(input("Podaj liczbę1 :")) #zmienna globalna
b= int(input("Podaj liczbę2 :"))








def sumuj(a,b):   #defincja funkcji z parametrami
    suma = a+b
    print ("suma: ",suma)
    
    
def sumuj2(): 
    suma = a+b
    print ("suma: ",suma)


def main(args):
    a = int(input("Podaj liczbę3:")) #zmienna lokalna
    b = int(input("Podaj liczbę4:"))

    sumuj(a,b) #wywolanie funkcji
    sumuj2()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
