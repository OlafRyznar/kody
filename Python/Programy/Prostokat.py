
def main(args):
    bok1 = int(input("Podaj 1 bok: "))
    bok2 = int(input("Podaj 2 bok: "))
    pole = bok1 * bok2
    print("Pole: ", pole)
    obwod = 2 * bok1 + 2 * bok2
    print("Obwod: ", obwod)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
