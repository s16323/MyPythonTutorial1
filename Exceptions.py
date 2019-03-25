# doprowadzamy do stworzenia wyjątku
# próbujemy otworzyć (bez tworzenia - bo np. mode='r+') plik, którego nie ma

# plik = open("exceptiontest.txt", "r+")
# plik.write("helllo")
# plik.close()

# dostajemy: FileNotFoundError: [Errno 2] No such file or directory: 'exceptiontest.txt'
print("\n-----------1 wyjątek--------------\n")

# teraz spróbujmy przechwycić ten błąd:

try:                                            # spróbuj wykoać...
    plik = open("exceptiontest1.txt", "r+")
    plik.write("hello")
    plik.close()
except FileNotFoundError:                       # jeżeli się nie wykona (a konkretnie - będzie: FileNotFoundError) to zrób coś...
    print("Wystąpił błąd z FileNotFoundError - plik nie istnieje, utwórz go najpierw.")

print("program dalej trwa...")

print("\n----------kilka wyjątków-----------\n")
# Teraz kilka różnych wyjątków:

try:                                            # spróbuj wykoać...
    plik = open("exceptiontest2.txt", "r")      # 'r' nie może zapisywać do pliku
    plik.write("Yello")                         # tu będzie błąd
    plik.close()
except FileNotFoundError as e:                  # jeżeli się nie wykona (a konkretnie - będzie: FileNotFoundError) to zrób coś... / tear przekazujemy ten wyjątek do zmiennej e
    print(e)                                    # Python automatycznie przekonwertuje e na stringa do wyświetlenia
    print("Wystąpił błąd z FileNotFoundError - plik nie istnieje, utwórz go najpierw.")
except:                                         # goły except - wychwyci każdy błąd
    print("Nieznany błąd... przejebane fest.")

print("\n-------kilka wyjątków lepiej:-------\n")

try:                                            # spróbuj wykoać...
    plik = open("exceptiontest2.txt", "r")      # 'r' nie może zapisywać do pliku
    plik.write("Yello")                         # tu będzie błąd
    plik.close()
except FileNotFoundError as e:                  # jeżeli się nie wykona (a konkretnie - będzie: FileNotFoundError) to zrób coś... / tear przekazujemy ten wyjątek do zmiennej e
    print(e)                                    # Python automatycznie przekonwertuje e na stringa do wyświetlenia
    print("Wystąpił błąd z FileNotFoundError - plik nie istnieje, utwórz go najpierw.")
except Exception as e:                          # jeżeli się nie wykona z jakiejkolwiek innej przyczyny (tu - nie można zapisywać) to zrób coś / wyjątek przekazujemy do zmiennej e
    print(e)
    print("Nieznany błąd... przejebane fest.")


try:                                            # spróbuj wykoać...
    plik = open("exceptiontest2.txt", "w")      # 'w' nie może odczytywać do pliku
    plik.read("Yello")                          # tu będą 2 błędy - nie może odzczytywać i .read ma zły arg - powinno być .read(), lub .read(5) (odczytaj np.5 znaków) zamiast .read("cośtam..")
    plik.close()
except FileNotFoundError as e:
    print(e)
    print("Wystąpił błąd z FileNotFoundError - plik nie istnieje, utwórz go najpierw.")
except TypeError as e:                          # jak ktoś poda zły typ argumentu
    print(e)
    print("zły typ")
except PermissionError as e:
    print(e)
    print("brak dostępu")
except Exception as e:                          # jeżeli się nie wykona z jakiejkolwiek innej przyczyny to zrób coś / wyjątek przekazujemy do zmiennej e
    print(e)
    print("Nieznany błąd... przejebane fest.")