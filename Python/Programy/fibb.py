def fib_it(n):
	wynik,a,b=0, 0, 1 #przypisanie wielokrotne
	#[0, 1, 1, 2, 3, 5, 8, 13,21]
#    a, b
	#    a,b
		#a,b
	for i in range(1, n+1):
		wynik = a+b
		a = b
		b = wynik
	return wynik

def main(args):
	n = int(input("Ktory wyraz: "))
	if (n == 0) :
		print(fib_it(n))
	for i in range (1,n+1):
		if i > 1:
			print(f"fib_it({i}) = {fib_it(i)}, {fib_it(i) / fib_it (i-1)}")
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
