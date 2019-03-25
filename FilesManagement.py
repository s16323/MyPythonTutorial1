# otwieramy plik
#zabezpieczamy przed zapisem przez innych podczas kiedy jest wykorzystywany tutaj


f =open("myFiles/plik.txt", "a+") # otworzenie pliku i utworzenie zmiennej, która będzie go reprezentować
                    # tryb otwarcia - domyślnie: mode ='r' (read - tylko odczytywanie)
                    # tryby są WAŻNE! mogą tworzyć plik jeżeli go nie znajdą, usuwać zawartość przed zapisem itp. itd...
                    # tryby są w tabelce w pliku: MyFiles/Python open() file modes.xlsx w tym projekcie
                    # wybieramy akurat a+ bo chcemy zapisywać, ale nie kasować zawartości (też tworzy plik jeżeli go nie było!!!), kursor będzie na końcu pliku (w tym trybie)
                    # Przypomnienie: można sprecyzować argumenty (jak w każdej funkcji) mode=a+ zamiast tylko a+, wtedy kolejność nie ma znaczenia

f.write("123456789 ")     # zapisanie stringa
f.close()           # zamykamy plik (już nic się nie da zrobić z nim (trzeba znowu otworzyć))

#wczytywanie z pliku:

f =open("myFiles/plik.txt", "r")        # 'r' - kursor na początku, tylko czytanie
print(f.read(4))       #wczytaj 5 znaków i wyświetl
f.close()


f =open("myFiles/plik.txt", "a+")
f.write(3*"\n Kakao")
f =open("myFiles/plik.txt", "r")        # zmiana mode na 'r' bo chcemy czytać od pczątu pliku a 'a+' ustawia kursor na końcu
f.seek(1)                               # seek przesuwa kursor do przodu po pliku
print(f.read(8))
print(f.readline())                     # czytaj całą linię, .readline(6) - czytaj 6 znaków z linii
print(f.readlines())                    # czytaj cały plik - konwertuje go do tablicy jego linijek

f.close()

f =open("myFiles/plik.txt", "r")

for line in f.readlines():
    print(line, end="")                 # end="" żeby usunąć załamania linii dodane przez print()

for line in f.readlines():
    print(line.strip(), end="")        # .lstrip() usuwa wszystkie znaki puste z lewej strony stringa
                                        # .rstrip z prawej , .strip() z obu stron