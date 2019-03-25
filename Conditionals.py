#Conditional instructions

print("Chose your x:")
x = float(input())

# if
#instead of {} ose TAB !!!
if x == 5:  # == compares values. =
    print("x = 5", type(x))
else:
    print(x, "!= 5", type(x))
    if x > 5:
        print(x, "> 5", type(x))
    else:
        print(x, "< 5", type(x))

print()

#Same with booleans:
print("Chose your 0 or 1")
x = bool(int(input()))      # input is a string ---> converrted to int ---> converted to bool !!! EVERY  NOT EMPTY STRING == True !!!
if x:                       #now.. if True, than do sth... 0 == False, any other value == True
    print("True")
else:
    print("False")

#   if x        if x == True    if x == 1   if 1   if not ""
#   if not x    if x == False   if x == 0   if 0   if ""
if not x:
    print("'not x' also works as negation, check line 27") #to x or not to x

print()

#booleans inside variables

x = 5 < 6   #this is bool 1
print(type(x))

x = 1 > 6   #this is bool 0
print(type(x))
