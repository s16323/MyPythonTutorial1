# While

i = 0
while i < 10:
    print(i)
    i += 1

i = 9
while i >= 0:
    print(i)
    i -= 1
print("-----------------------------------------")


#Loopping through lists

someList = ["a", "b", "c", "d", "e", "f", "g", "h"]

#print out whole list using while
i = 0
while i < len(someList):    # len() --> length
    print(someList[i])
    i += 1
print("-----------------------------------------")

# print out whole list using for

for letter in someList:
    print(letter)
print("-----------------------------------------")

for letter in someList:
    print(letter)
    if letter == "e":
        print("This is letter e!")
        break
print("-----------------------------------------")


# Generators

for i in range(10):     # generates a "list" of 10 elements
    print(i)
print("-----------------------------------------")

for i in range(10, 20):  # generates a "list"  of elements between 10 and 50
    print(i)
print("-----------------------------------------")

for i in range(10, 20, 2):  # generates a "list"  of elements between 10 and 50 in steps of 2
    print(i)
print("-----------------------------------------")