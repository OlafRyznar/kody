def wydajReszte1(reszta, listaNm):
    i = 0  # indeks wskazujący nominał
    while reszta > 0:
        if reszta >= listaNm[i]:
            ileNm = int(reszta / listaNm[i])
            reszta -= ileNm * listaNm[i]
            print(f"{ileNm} x {listaNm[i]}")
        i += 1


def wydajReszte2(reszta, listaNm):
    i = 0  # indeks wskazujący nominał
    liczbaNm = len(listaNm)  # liczba nominałów
    while reszta > 0 and i < liczbaNm:
        while i < liczbaNm and reszta < listaNm[i]:
            i += 1
        # print "aktN={}".format(aktualnyNominal)
        if i < liczbaNm and reszta >= listaNm[i]:
            ileNm = int(reszta / listaNm[i])
            reszta -= ileNm * listaNm[i]
            print(f"{ileNm} x {listaNm[i]}")

    if reszta > 0:
        print(f"Brak nominałów do wydania pozostałej kwoty: {reszta} zł")


def wydajReszte3(reszta, listaNm):
    i = 0  # indeks wskazujący nominał
    liczbaNm = len(listaNm)  # liczba nominałów
    while reszta > 0 and i < liczbaNm:
        while i < liczbaNm and reszta < listaNm[i]:
            i += 1
        # print "aktN={}".format(aktualnyNominal)
        if i < liczbaNm and reszta >= listaNm[i]:
            nominal = listaNm[i]
            ileNm = int(reszta / nominal)
            if ileNm > listaNm.count(nominal):  # czy mamy nominaly?
                ileNm = listaNm.count(nominal)
            reszta -= ileNm * nominal
            for i in range(ileNm):
                listaNm.remove(nominal)
                liczbaNm -= 1
            i = 0
            print(f"{ileNm} x {nominal}")

    if reszta > 0:
        print(f"Brak nominałów do wydania pozostałej kwoty: {reszta} zł")

def pobierzNominaly():
    # lista poprawnych nominałów
    nominaly = set([200, 100, 50, 20, 10, 5, 2, 1])
    nominal = int(input("Podaj nominał lub 0, aby zakończyć: "))
    listaNm = []  # lista podanych nominałów
    while nominal > 0:
        if nominal in nominaly:
            listaNm.append(nominal)
        else:
            print("Niepoprawny nominał!")
        nominal = int(input("Podaj nominał: "))
    listaNm.sort(reverse=True)  # sortowanie malejące
    print(listaNm)

    return listaNm


def main(args):
    listaNm = pobierzNominaly() #[200, 100, 50, 20, 10, 5, 2]
    reszta = int(input("Podaj resztę: "))
    #wydajReszte1(reszta, listaNm)
    #wydajReszte2(reszta, listaNm)
    wydajReszte3(reszta, listaNm)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
