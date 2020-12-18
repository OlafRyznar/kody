def silnia_it(n):
	wynik = 1
	for i in range(n):
		wynik = wynik * (i + 1)
	return wynik
    
def main(args):
	n = int(input("Podaj liczbę: "))
	print("{}! = {}".format(n, silnia_it(n)))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
