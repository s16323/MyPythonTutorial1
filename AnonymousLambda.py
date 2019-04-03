# anonymous function = lambda expression
# function without a name

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

# with many inputs:
# first an last name taken from the form and formated to get rid of unanted spaces and with capitalised letters:

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

full_name(' aRtur', 'DEMbicki ')

print(full_name(' aRtur', 'DEMbicki '))

# Common use:
# https://www.youtube.com/watch?v=25ovCm9jKfA