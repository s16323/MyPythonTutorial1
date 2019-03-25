fruits = ["apple", "orange", "pear", "banana", "apple", "strawberry", "apple", "berry"]

# czy jakiś element jest w liście?
print("\n", "--------czy  element 'apple' jest w liście?---------", "\n")

print("lista:", fruits)
znaleziono = False
for fruit in fruits:
    if fruit == "apple": znaleziono = True
print("odpowiedź:", znaleziono)

# czy jakiś element jest w liście? Lepsza metoda:
print("\n", "------------------Lepsza metoda:--------------------", "\n")

if "orange" in fruits:      # 'in' działa tak samo jak w 'for'
    print("znaleziono 'orange'")
else:
    print("nie znaleziono 'ornange'")

# Jka znaleźć 2 owoce?:
print("\n", "----------2 owoce: 'apple' i 'orange'----------------", "\n")

if "apple" in fruits:
    print("znaleziono 'apple'")
else:
    if "orange" in fruits:
        print("nie znaleziono 'apple', ale za to jest 'orange'")
    else:
        print("nic nie znaleziono")

# Jka znaleźć 2 owoce? Lepszy sposób:
print("\n", "------------------Lepszy sposób:---------------------", "\n")

if "apple" in fruits:
    print("znaleziono 'apple'")
elif "orange" in fruits:                                        # 'elif' - 'else if'
    print("nie znaleziono 'apple', ale za to jest 'orange'")
elif "berry" in fruits:
    print("NIe znaleziono 'apple', ani 'orange', ale za to jest 'berry'")
else:                                                           # 'else' = 'elif True'
    print("nic nie znaleziono")

# Operatory Logiczne: and , or , == , !=
print("\n", "---------------Operatory Logiczne:-------------------", "\n")

print("Podaj liczbę z przedizłu (5,20):")
liczba = int(input())        # czeka aż uzytkownik cos wpisze i wcisnie Enter, int() zmienia wprowadzony string na liczbę naturalna

if liczba < 20 and liczba > 5:
    print("<20 i >5")
else:
    print("liczbs jest poza przedziałem (5,20)")


print("Podaj liczbę : >20 lub <5")
liczba = int(input())

if liczba > 20 or liczba < 5:
    print(">20 lub <5")
else:
    print("liczbs należy do przedziału <5,20>")


# Operatory Logiczne i listy: ('in' i 'not in')
print("\n", "------------Operatory Logiczne i listy:-------------", "\n")

listaLiczb = [4, 7, 1, 9, 5, 3]
print("listaLiczb =", listaLiczb)

print("Wyszulaj liczbę:")
szukana = int(input())
if szukana not in listaLiczb:
    print(szukana, "nie ma w liście")
else:
    print("znaleziono", szukana)

print("Wyszulaj liczbę:")
szukana = int(input())
if not szukana in listaLiczb:       # różne miejsca umieszczeia 'not', można też zaprzeczyć podwójnie "if not szukana not in listaLiczb'...
    print(szukana, "nie ma w liście")
else:
    print("znaleziono", szukana)