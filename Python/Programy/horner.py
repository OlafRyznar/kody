def drukujw(n,tbwsp):
	for i in range(n):
		print(f"{tbwsp[i]}x^{n-i} + ", end="")
	print(tbwsp[n])


def horner_it(n, tbwsp ,x):
	wynik = tbwsp[0];

	for i in range(1, n+1):
		wynik = wynik * x + tbwsp[i];
	return wynik;
	


def main(args):
	
	

	n=int(input("Jaki stopień wielomianu: "))
	tbwsp = []

	for i in range(n+1):
		tbwsp.append(float(input(f"Współczynnik przy potędze {n-i}: ")))
	x=float(input("Jaki argument x: "))

	print("Wartość wielomianu o postaci: ") 
	drukujw(n, tbwsp)
	print(f"wynosi: {horner_it(n,tbwsp,x)}")
    
	return 0
	
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
