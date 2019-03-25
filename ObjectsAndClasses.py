# import MyModules.Klasy1               # zwykły import
# MyModules.Klasy1.mojaFunkcja()        # zwykłe użycie - tak jest nie raz lepiej, bo widać skąd co jest
from MyModules.Klasy1 import *          # importujemy w ten sposób, żeby nie musieć potem pisać ścieżek za każdym razem.. MyModules.Klasy1.costam6 itd..

mojaFunkcja()                           # użycie bez ścieżki (proste, ale nie widzć od razu skąd jest funkcja)
print(abc)                                # użycie zmiennej z zaimportowanego modułu
print(abc.bit_length())

nowyAkapit("Klasy")

calc = Calculator()          # stworzenie obiektu klasy Calculator
calc.dodaj(1, 2)             # wykorzystanie metod obiektu
calc.odejmij(5, 3)

calc_2 = Calculator()        # stworzenie kolejnego obiektu klasy Calculator
calc_2.dodaj(20, 20)         # wykorzystanie metd kolejnego obiektu

nowyAkapit("Metody Specjalne")
# metody specjalne zaczynają się od 2 podkreślników "__costam"

#przykład użycia w jakiejś funkcji:
def main():
    print("zaczynam main")
    calc_3 = Calculator()
    calc_3.dodaj(10, 10)
    print("kończę main")
main()
print("Garbage Collector usunął instancję z maina")


# można ręcznie usuwać instancje:
# calc = Calculator()
# del calc
# print(calc)         # nie ma już nic do wyświetlenia - NameError: name 'calc' is not defined


calc_4 = Calculator()
print(calc_4)         # zadziała __str__() / lub print(str(calc_4)) jeżeli jest wybór, jak nie podane to po kolei bierze dlatego pod spodem trzeba było dopisać konkretnie print(int(calc_4)) żeby dostać liczbę
print(int(calc_4))    # zadziała __int__()

#przykład użycia:

wynik = int(calc_4) + 50      # int(calc) = 10 bo __int__(): return 10 w metodach specjalnych klasy Calculator()
print(wynik)

# wykorzystanie __bool__()
if calc_4:
    print("True")
else:
    print("False")


nowyAkapit("Tworzenie zmiennych w klasach")

#można stworzyć sobie dowolną zmienną w klasie po utworzeniu instancji:
# szkodzi wydajności, ale nie mocno
calc_5 = Calculator()
calc_5.liczba10 = 20
calc_5.liczba10 += 50
print(calc_5.liczba10)
# taka zmienna jest lokalna tylko dla tej instancjiw którym jest utworzona
# czyli nowy obiekt klasy Calculator(), np. jakiś calc_125 już nie ma do niej dostępu

# zmienne można utworzyć też w klasie, używając 'self', np w __init__()
# self - tutorial: https://www.youtube.com/watch?v=0EN-5H9RTEs&list=PLdBHMlEKo8UcOaykMssI1_X6ui0tzTNoH&index=20
# odwołanie się do tej zmiennej, która powstała w __init__(self):
print(calc_5.liczba)

#wykorzystanie self.ostatni_wynik w __init__():
print("działa calc_4")
calc_4.dodaj(4,44)
calc_4.odejmij(15,17)
print("działa calc_5")
calc_5.dodaj(10, 20)
calc_5.odejmij(55, 7)

print("Ostatnie wynik calc_4: {}".format(calc_4.ostatni_wynik))
print("Ostatnie wynik calc_5: {}".format(calc_5.ostatni_wynik))