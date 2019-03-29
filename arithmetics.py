# arithmetic in Python:
import math
import fractions
print(dir(math))
print(dir(fractions))
from math import *
from fractions import *


a = 13
b = 2

# power:
c = a**b            # leaves int
c = pow(a, b)       # casts to float (!)

# square root:
d = 2**.5

e = sqrt(a)

# n-root:
f = a**(1/b)

# modulus (remainder):
g = a % b

print(c, "\n",
      d, "\n",
      e, "\n",
      f, "\n",
      round(f), "\n",
      g, "\n"
      )

# complex numbers:

ca = 5+5j
cb = 1j
cc = 0
c = complex(c)
print(c)
print(a + b + c)

# trigonometry:
#sin(x) - returns radians
# degrees(x) - radians --> degrees
# radians(x) - degrees --> radians




print("\n----------do some math:-----------\n")
num = 5.645

print(
num, 'number\n',

round(num, 2), '   round({}, 2)  "5" gets rounded down\n'.format(num),
floor(num), '   floor\n',
ceil(num), '   ceil\n',

degrees(pi), '   degrees of pi\n',
radians(180), '   radians of 180 degrees\n',
pi, '   pi\n',

exp(4), '   exponent - returns e**x\n',

factorial(5), '   factorial\n',

sin(pi/2), '\n',
sin(pi), '   sin(pi) =~ 0\n',
sin(2*pi), '   sin(2*pi) =~ 0\n',
sin(radians(0)), '\n',
sin(radians(30)), '   why not 0.5 ???\n',
Fraction(sin(radians(30))).limit_denominator(), '   as fraction\n',
sin(radians(90)), '\n',

log(16, 2), '\n',

)

"""
15%4, 'modulo\n',
5/2, 'division\n',
int(5/2), 'int\n',
bool(5/2), 'bool\n',
round(5/7, 5), 'round\n',
pi*4**2, 'sphere\n',
sin(degrees(180)), 'sin degrees\n',
sin(0), 'sin number\n',
sin(radians(pi)), 'sin radians\n',
"""