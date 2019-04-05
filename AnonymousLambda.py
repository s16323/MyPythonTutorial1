# anonymous function = lambda expression
# function without a name
'''
For one time use, fast and easy.
Sorting and filtering data on the fly.
'''
# normalnie
def square(a):
    return a*a



f = lambda a : a*a
# f - lambda expression that gets 'a' and returns 'a*a'

print(square(5))
print(f(5))


# other:
ff = lambda a, b: a*b

print(ff(4, 4))

print("\n-----------------complex lambda expression:-----------------\n")
# with many inputs:
# first an last name taken from the form and formated to get rid of unwanted spaces and with capitalised letters:

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

full_name(' aRtur  ', 'DEMbicki ')

print(full_name(' aRtur', 'DEMbicki '))

# Use this whenever you gather any data from user input - users do weird shit...

print("\n-----------------Sorting lists with custom sort function:-----------------\n")
# Common use:
# https://www.youtube.com/watch?v=25ovCm9jKfA

sf_authors = ['Isaac Asimov', 'Ray Bradbury', 'Arthur C. Clarke', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells']
print('unsorted:', sf_authors)
# Sort by LAST name:
'''
help(sf_authors.sort)
sort(*, key=None, reverse=False) method of builtins.list instance
key --> function that would be ued for sorting - let's pass it a lambda expression
'''
# To access last name:
# 1. split the string into pieces wherever it has a space using .split(' ')
# 2. access the last index by name.split(' ;)[-1]
# As a precaution convert to lowercase using .lower() - now the sorting will not be case-sensitive

sf_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print('sorted: ', sf_authors)


print("\n-----------------A function that makes functions:-----------------\n")
# quadratic equations
# f(x) = a*x**2 + b*x + c

def build_quadratic_function(a, b, c):
    '''Returns a function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)

print(f(1))
print(f(-8))
print(f(0))

# now let's build and use quadratic function without EVER giving it a name... (!)

print(build_quadratic_function(3, 0, 1)(2))    # this will create 3x^2+1 and than immediately pass x=2 to it  --> should print 13

