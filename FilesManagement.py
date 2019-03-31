# otwieramy plik
#zabezpieczamy przed zapisem przez innych podczas kiedy jest wykorzystywany tutaj


f = open("myFiles/plik.txt", "a+") # otworzenie pliku i utworzenie zmiennej, która będzie go reprezentować
                    # tryb otwarcia - domyślnie: mode ='r' (read - tylko odczytywanie)
                    # tryby są WAŻNE! mogą tworzyć plik jeżeli go nie znajdą, usuwać zawartość przed zapisem itp. itd...
                    # tryby są w tabelce w pliku: MyFiles/Python open() file modes.xlsx w tym projekcie
                    # wybieramy akurat a+ bo chcemy zapisywać, ale nie kasować zawartości (też tworzy plik jeżeli go nie było!!!), kursor będzie na końcu pliku (w tym trybie)
                    # Przypomnienie: można sprecyzować argumenty (jak w każdej funkcji) mode=a+ zamiast tylko a+, wtedy kolejność nie ma znaczenia

f.write("123456789 ")     # zapisanie stringa
print(f.name, f.mode)
f.close()                 # zamykamy plik (już nic się nie da zrobić z nim (trzeba znowu otworzyć))  - Ważne żeby zamknąć !!!

#wczytywanie z pliku:

f = open("myFiles/plik.txt", "r")        # 'r' - kursor na początku, tylko czytanie
print(f.read(4))       #wczytaj 5 znaków i wyświetl
f.close()


f = open("myFiles/plik.txt", "a+")
f.write(3*"\n Kakao")
f = open("myFiles/plik.txt", "r")        # zmiana mode na 'r' bo chcemy czytać od pczątu pliku a 'a+' ustawia kursor na końcu
f.seek(1)                               # seek przesuwa kursor do przodu po pliku
print(f.read(8))
print(f.readline())                     # czytaj całą linię, .readline(6) - czytaj 6 znaków z linii
print(f.readlines())                    # czytaj cały plik - konwertuje go do tablicy jego linijek

f.close()

f = open("myFiles/plik.txt", "r")

for line in f.readlines():
    print(line, end="")                 # end="" żeby usunąć załamania linii dodane przez print()

for line in f.readlines():
    print(line.strip(), end="")         # .lstrip() usuwa wszystkie znaki puste z lewej strony stringa
                                        # .rstrip z prawej , .strip() z obu stron
f.close()
print("\n----------context manager:-----------\n")
# 'with' keyword
# otwieramy kontekst
with open('myFiles/plik.txt', 'r') as f:        # Po zakończeniu pracy i wyjściu z tego bloku kodu plik zostanie automatycznie zamknięty. Nie potrzeba f.close()
    pass                                        # Jeżeli pojawi się wyjątek plik również zostanie zamknięty
# zamykamy kontekst

print(f.closed)                                 # sprawdź czy zamknięty
# print(f.read())                                 # czy da sie teraz odczytać - nie.

# praca z plikiem wewnątrz kontekstu (czyli prawidłowo):
with open('myFiles\plik.txt', 'r') as plik:
    plik_contents = plik.read()                       # zawartość pliku do zmiennej (obciąża pamięć!)
    print('\nread:', plik_contents)                           # wyświetl zawartość

    plik_contents = plik.readlines()                  # lista linii w pliku
    print('\nreadlines:', plik_contents)

    plik_contents = plik.readline()                  # kolejna linia
    print('\nreadline:', plik_contents)

    for line in plik:
        print(line, end='')

print(f.closed)         # i już poza kontekstem - plik jest zamknięty

with open('myFiles\plik.txt', 'r') as plik:

    plik_contents = plik.read(10)                 # przeczytaj pierwsze 10 znaków
    print('\nread:', plik_contents, end='')

    plik_contents = plik.read(8)                 # przeczytaj kolejne 8 znaków (!) w obrębie kontekstu wie gdzie skończył i leci dalej
    print('\nread:', plik_contents, end='')      # jak doleci do końca odda pusty string

    size_to_read = 20                            # żeby kontrolować ilość info jakie ma być czytane

    while len(plik_contents) > 0:
        print(plik_contents, end='')
        plik_contents = plik.read(size_to_read)