
fruits = ["apple", "orange", "pear", "banana", "apple"]

for i, fruit in enumerate(fruits):
    print(i, fruit)

print("--------------Enumerate---------------")
# Enumerate - adds counter to an iterable and returns it
# reach 3 fruit and omit the rest using 'enumerate' (iterator)

for i, fruit in enumerate(fruits):     # 'For' loop receives 2 args now. For every index 'i' and a given 'fruit' element reported by 'enumerate()' function do:
    if i == 3:
        break
    print(i, fruit)

print("---------------Format-----------------")
# Format

# C = "someOtherString".capitalize()  # Check out other functions
# print(C.lower())        # itd...

print("someString {} {}".format("123", "ABC"))      # format replaces whatever is in {}

x ="Hello {}"
y = x.format("World", "xxx", 777)
print(y)

print("--------------------------------------")

for i, fruit in enumerate(fruits):
    print("I'm checking: {}".format(i))
    if i == 3:
        print("{} is the third fruit!!! No more checking.".format(fruit))
        break
    print(i,"is", fruit)

print("------Skipping some iterations--------")
# Skipping some iterations


fruits = ["apple", "orange", "pear", "banana", "apple"]

print("Start")

for fruit in fruits:
    if fruit == "orange":
        print("wracam do poczatku petli")
        continue            # after 'continue' the next if is skipped ! Code goes back to 'for' loop
    if fruit == "banana": break
    print(fruit)
print("End")









