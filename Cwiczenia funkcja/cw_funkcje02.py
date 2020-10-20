
import math
import statistics



def srednia(tablica, iloscliczb):
	srednia =sum(tablica)/iloscliczb
	print("Srednia wynosi: ", srednia)


def mediana(tablica):
	print("Mediana wynosi: ", statistics.median(tablica))


def main(args):
	iloscliczb = int(input("Podaj ilosc ocen: "))
	if iloscliczb >20:
		print("Maksymalna ilosc ocen wynosi 20!")
		return(iloscliczb)

	tablica =[]
	for i in range(0,iloscliczb):
		f = int(input("Podaj ocene: "))
		tablica.append(f)

		if f <=0 or f >6:
			print("Wprowadzono niepoprawna ocene")
			return


	srednia(tablica, iloscliczb)
	mediana(tablica)

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
