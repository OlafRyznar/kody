

def euklides2(a, b):
    i = 0
    while a > 0:
        i = i+1
        a = a % b
        b= b - a
        print("Powtórzeń: ", i)
    return b


def euklides1(a,b):

    licznik = 0

    while a != b:
        if a > b:
            a = a - b
            licznik += 1
        else:
            b = b - a
            licznik += 1

    print("Liczba powtórzeń: ", licznik)

    return a

def main(args):
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print(f"NWD({a}, {b} wynosi", euklides1(a,b))
    print (euklides2(a, b))
    return 0
