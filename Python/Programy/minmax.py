
from random import randint
 
 
def losuj(tab,ile,maks):
	for i in range (ile):
		tab.append(randint(0,maks))
	
	
def min(tab, n):
	min=tab[0];
	for i in range(1, n):
		if tab[i] < min:
			min = tab[i]
	return min;
	
def max(tab, n):
	min = tab[0];
	max = tab[0];
	for i in range(1,n):
		if tab[i] < min:
			min = tab[i]
		if tab[i] > max:
			max = tab[i]
	return max
	
def minmax1(tab, n):
	tbmin = []
	tbmax = []
	for i in range(0,n,2):
		if tab[i] > tab[i+1]:
			tbmax.append(tab[i])
			tbmin.append(tab[i])
	return tbmin,tbmax
	
 
 
 
def main(args):

	tab = [] #int lista[ile];
	n = 20
	MAKS = 50
	losuj(tab,n,MAKS)
	print("Wylosowane liczby:\n", tab)
	print(f"minimum: {min(tab,n)}. Maksimum: {max(tab,n)}.")
	
	if n % 2:
		ost_el = lista[n-1]
		n=n-1
	
	tbmin, tbmax = minmax1(tab, n)
	print(tbmin)
	print(tbmax)
	min_el = min(tbmin, len(tbmin))
	max_el = max(tbmax, len(tbmax))
	
	if n % 2
		tbmin, tbmax = minmax
		elif: ost_el < min_el:
			min_el = ost_el
	print(f"minimum: {min_el}. Maksimum: {max_el}.")
	pass:
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
