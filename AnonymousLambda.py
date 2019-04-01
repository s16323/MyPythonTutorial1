# anonymous means the same as lambda

def square(a):
    return a*a

f = lambda a : a*a


print(square(5))
print(f(5))

# other:

ff = lambda a, b: a*b

print(ff(4, 4))