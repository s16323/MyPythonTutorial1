# deklarowanie zmiennych
# python sam definiuje typy
'''
many lines comment
many lines comment
many lines comment
'''

print("variables in python:")

zmienna1 = "somecharacters"     # <class 'str'>
zmienna2 = 123                  # <class 'int'>
zmienna3 = -0.1                 # <class 'float'>

print(zmienna1, type(zmienna1))
print("    ", zmienna1 + "abc", " --> dodawanie stringów")
print("    ", zmienna1*2, " --> mnożenie stringów")
print(zmienna2, type(zmienna2))
print(zmienna3, type(zmienna3))
print()


# właściwości typu <class 'bool'>
print("bool type properties:")

zmienna4 = False    # false  <class 'bool'>
zmienna5 = -False   # 0      <class 'int'>
print(zmienna4, type(zmienna4))
print(zmienna5, type(zmienna5))
print()

zmienna4 = True     # true   <class 'bool'>
zmienna5 = -True    # -1     <class 'int'>
print(zmienna4, type(zmienna4))
print(zmienna5, type(zmienna5))
print()

zmienna4 = 15
bool(zmienna4)
print(zmienna4, type(zmienna4)) # dlaczego typem jest teraz <class 'int'> ?
zmienna5 = 0
bool(zmienna5)
print(zmienna5, type(zmienna5)) # dlaczego typem jest teraz <class 'int'> ?
print()


# getting user input
print("user input:")

print("type in a variable:")
x = input()
print("type of variable:", x, " is: ", type(x))
print("important: 'input()' does not check for type!!! everything is <class 'str'>")
print()

print("user numbers input:")
print("type in a number:")
x = input()
x = int(x)      # type conversion string --> int
print("variable", x, "has now been converted to", type(x))