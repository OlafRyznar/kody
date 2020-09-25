#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma.parzyste.py
#  iloczyn liczb wprowadzonych przez uzytkownika
#  


def main(args):
    
    iloczyn =  1
    for i in range(10):
        a=int(input("podaj liczbe "))
        iloczyn = iloczyn * a
           
    print(iloczyn)
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
