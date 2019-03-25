#String manipulations

x = "Tanie wino jest dobre"
print("To jest string:", x,)

#Extracting one sign
print("wybierz numer znaku do wyświetlenia:")
i = int(input())
a = x[i]
print("Wybrany znak ze stringa:", a)
print()

#Extracting many signs (substring)
print("wybierz początek substringa:")
i = int(input())
print("wybierz koniec substring:")
j = int(input())

a = x[i:j]
print("Wybrany znak ze stringa:", a)
print()

# x[1:] 1 - do końca
# x[:6] od początku - do 6
# x[:] całość
# x[-2] 2 od końca itd...
