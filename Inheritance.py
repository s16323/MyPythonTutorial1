from MyModules.Klasy1 import *

parent = Parent()
parent.parent()
parent.poke()

nowyAkapit("klasa Child dziedzicząca po Parent")
# klasa dziedzicząca po Parent()
class Child(Parent):

    def __init__(self):
        super().__init__()          # wykonaj również jakąś funkcję rodzica - super() - czyli z rzędu wyżej w hierarchii klas - opcjonalnie
        print("Child __init__")

    def __del__(self):
        print("Child __del__")

    def poke(self):
        super().poke()   # to samo znowu - opcjonalnie
        print("Child poked")


child = Child()
child.poke()
child.parent()          # to jest funkcja odziedziczona z klasy nadrzędnej


nowyAkapit("Praktyczne Zastosowanie")
# Schemat firmy - pracownicy

class Person():

    def __init__(self, name):
        self.name = name
        self.surname = "domyślne nazwisko"
        self.wiek = 0

class Employee(Person):

    def __init__(self, position, name):
        super().__init__(name)                                # żeby metoda z rodzica też się wykonała.. pracownik też jest osobą i musi mieć imie i nazwisko itd..
        self.position = position                          # żeby ytrzeba było podawać p;osition podczas tworzenia instancji.. nie może istnieć pracownik który nie jest zatrudniony na jakimś stanowisku ( to nie parlament EU)
        self.specialisation = "domyślna specjalizacja"


class Client(Person):

    def __init__(self, name):
        super().__init__(name)
        self.ordered = "empty order"


employee1 =  Employee("Programmer", "Tomek")         # konstruktor
print(employee1.position, employee1.name)

client1 =  Client("Dupa")
print(client1.name)