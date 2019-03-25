import module1
import MyModules.module2      # Ścieżka dostępu do innego flderu jest potrzebna


module1.test("dupa")        # Jeżeli zaimportowany jest cały module1 to trzeba podawać ścieżkę module1.test
module1.test("huj")

MyModules.module2.test("kakao")       # Wywołanie ze ścieżką dostępu

module1.funkcja1("dupa2")

# importowanie tylko wybranych funkcji z modułu:
from module1 import funkcja1, funkcja2      # jeżeli zaimportowane są konkretne funkcje z modułu, lub wszystkie (*) to nie trzeba pisać ścieżki


funkcja1("dupa3")
funkcja2("dupa4")

# importowanie tylko wybranych funkcji z modułu:

from time import sleep

sleep(1)

# inny zapis importowania wsystkiego z modułu:
from module1 import  *

funkcja1("dupa5")

# importowanie funkcji z modułu z aliasowaniem - jeżeli chcemy użyć swojej własnej funkcji a akurat w module już jest jakas o tej samej nazwie
from module1 import funkcja1 as funkcja1_module1

funkcja1_module1("dupa7")   #funkcja funkcja1 występuje teraz pod aliasem funkcja1_module1

def funkcja1 ():        # moja lokalna funkcja o tej samej nazwie co jakaś funkcja w module1
    print("kutas kozła")

funkcja1()

from MyModules.module2 import *       # Są zaimportowane wszystkie funkcje

test("dupa8")                       # nie trzeba terz podawać ścieżki, momo że moduł jest w innej lokalizacji
test2("dupa9")