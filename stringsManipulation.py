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
# x[:6] od początku - do 6  PYTHON LICZY DO PRZEDOSTATNIEGO ZNAKU, czyli wyświetli znaki z pozycji: 0, 1, 2, 3, 4, 5
# x[:] całość
# x[-2] 2 od końca itd...

# konkatenacja:

print(x + " costamcostam", x + x)

# placeholders:
# %s - placeholder dla stringów:
name = "Jake"
sentence = "%s  is 15 yeays old"

print(sentence%name)        # użycie: %s = name będzie wstawione do sentence w miejsce %s
print(sentence%("Paul"))

sentence = "%s %s is the %s president of US"       # multiple substitution as string (%s)
print(sentence%("Donald", "Trump", 45))

# %d - placeholder dla int:
sentence = "%s %s is the %d president of US"       # multiple substitution as string and int (%d)
print(sentence%("Donald", "Trump", 45))