# zmienne i funkcje z małych liter, klasy z dużych

# zmienne:
abc = 100
bcd = 0

# funkcje:
def mojaFunkcja():
    print("moja funkcja działa")

def nowyAkapit(tekst = ""):
    print("\n-----------", tekst, "------------\n")

# klasy:

class Calculator():

    #metody specjalne
    def __init__(self):                     # wykonuje się gdy tworzymy instancję naszej klasy
        print("wykonuje się __init__")
        # zmienne można utworzyć też w klasie, używając 'self', np w __init__()
        # self - tutorial: https://www.youtube.com/watch?v=0EN-5H9RTEs&list=PLdBHMlEKo8UcOaykMssI1_X6ui0tzTNoH&index=20
        self.liczba = 10                    # czyli od teraz za każdym razem jak się pojawi instancja tej klasy to będzie miała w sobie zmienną .liczba z przypisaną początkową wartością 10
        self.ostatni_wynik = 0              # jak będziemy chcieli przechowywać ostatni wynik...

    def __del__(self):                      # wykonuje się podczas usuwania obiektu tej klasy (np koniec programu, lub garbage collector)
        print("wykonuje się __del__")

    def __str__(self):                      # wykonuje się gdy chcemy przekonwertować reprezentację klasy na ciąg znaków (czyli co klasa zwróci jak będzie konwertowana na stringa)
        return "To jest reprezentacja klasy Calculator() jako string"

    def __int__(self):                      # wykonuje się gdy chcemy przekonwertować reprezentację klasy na liczbę (czyli co klasa zwróci jak będzie konwertowana na int)
        return 10

    def __float__(self):                    #analogicznie
        return 10.00

    def __len__(self):                      #długość
        return 5

    def __bool__(self):                     # ... tych funkcji jest od chuja.. obczaić...
        return True

    # metody:
    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik          #przechowaj ten wynik - dla każdej instancji tej klasy przechowuj wyniki jakie do niej przynależą
        print(wynik)
    def odejmij(self, a, b):
        wynik = a - b
        self.ostatni_wynik = wynik
        print(wynik)


class Parent():             # Przykładowa klasa po której będa dziedziczyć inne

    def __init__(self):
        print("Parrent __init__")

    def __del__(self):
        print("Parent __del__")

    def parent(self):
        print("Parent parent")

    def poke(self):
        print("Parrent was poked")
