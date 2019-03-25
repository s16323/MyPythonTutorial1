# funkcje:
# def - define
# nazwy funkcji nie mogą zaczynać się od liczby, mogą mieć podkreślnik

# wyświetl wpisaną liczbę:
# def printujTo(liczba):
#     print("Test:", end = "")    # end = "" powoduje, że print() nie łamie linii
#     print(liczba)
#
# printujTo(int(input()))

# pomnóż:
def pomnoz(a, b):
    return a * b
#
def dodaj(a, b):
    return a + b

def podziel(a, b=1):        # b = 1 jest teraz domyślnym argumentem - jeżeli nie ma podanego innego w wywołaniu
    return a/b
#
# wynikMnoz = pomnoz(1, 2)
# wynikDod = dodaj(3, 4)
# wynikDziel = podziel(2, 4)
# print(wynikMnoz, wynikDod, wynikDziel)

# Keywords:
wynik = podziel(b=4, a=2)   # podawanie argsów w innej kolejności
print(wynik)

wynik = podziel(6, 2)
print(wynik)
