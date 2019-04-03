nominaly = [200, 100, 50, 20, 10, 5, 2, 1]

kwota = int(input('podaj kwote: '))


def wydaj(nom):
    global kwota
    ilosc_do_wydania = 0
    while kwota >= nom:
        ilosc_do_wydania += 1
        kwota = kwota - nom
    print('nominał: {}zl, do wydania: {}'.format(nom, ilosc_do_wydania))


for nominal in nominaly:
    wydaj(nominal)



