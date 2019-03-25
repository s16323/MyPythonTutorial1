# moduł os - funkcje związane z systemem

import os

lista = os.listdir("./myFiles")         # lista plików katalogów / można też napisać tylko: lista = os.listdir("myFiles")
print(lista)

lista = os.listdir("./")                # aktualne directory / można też napisać tylko: lista = os.listdir(".")
print(lista)

lista = os.listdir("../")               # directory w górę / można też napisać tylko: lista = os.listdir("..")
print(lista)

lista = os.listdir("../..")             # 2 directory w górę
print(lista)

print("\n------------------------------------------------------------\n")
# Czy 'plik' jest plikiem czy katalogiem?
 #lista = os.listdir("./")

for item in os.listdir("./"):
    print(item, "is a file:", os.path.isfile(item))

print("\n------------------------------------------------------------\n")
# Lub:
for item in os.listdir("./"):
    if os.path.isfile(item):
        print("{} jest plikiem".format(item))
    if os.path.isdir(item):
        print("{} jest folderem".format(item))

print("\n----------------------Moja Funkcja--------------------------\n")

def browseDir(directory = "./"):                # jakiś problem z przekazywaniem ścieżki dostępu innej niż lokalna ?!
    for item in os.listdir(directory):
        if os.path.isfile(item): isafile = "plik"
        elif os.path.isdir(item): isafile = "folder"
        else: isafile = "huj wie co"
        print("{} to {}".format(item, isafile))

browseDir()

print("\n-----------------------make directory------------------------\n")


# UWAGA!!! - SKRYPT TWORZY I NISZCZY PLIKI I FOLDERY W TYM PROJEKCIE - NIE ODPALAC BEZ OBCZAJENIA!!!


os.mkdir("nowy folder")
# os.("./nowy folder/pliktestowy.txt")
os.rename("nowy folder", "nowy folder nowa nazwa")
os.rmdir("nowy folder nowa nazwa")

print("\n-----------------------Ścieżki------------------------\n")

#Utworzenie nowego pliku
# plik = open("testfile1.txt", "w")
# plik.close()
# lub prościej:
open("testfile1.txt", "w").close()      # tworzy plik i go zamyka, żeby zwolnić dostęp
os.remove("testfile1.txt")              # kasuje plik

path = "myFiles/testfolder/testfile2.txt"
print(path)

print(os.path.dirname(path))            # zwraca ścieżkę dostępu (ale bez pliku na końcu)
print(os.path.basename(path))           # zwraca wszystko po ostatnim ukośniku, czyli ostatni folder lub plik
print(os.path.abspath(path))            # zwraca ścieżkę absolutną

os.makedirs(os.path.dirname(path))      # tworzy drzewo folderów

open(path, "w").close()                 # tworzy plik na scieżce 'path'

os.remove(path)                         # kasuje plik na końcu
os.rmdir(os.path.dirname(path))        # kasuje folder (przedostatni obiekt na 'path')