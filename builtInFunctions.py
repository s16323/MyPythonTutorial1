print("\n-----------------abs()-----------------\n")
# abs()         returns absolute value of a number --> int, float complex
print(abs(-11.1114))
a = -2**(1/2)
print(a)
a = a.__abs__()
print(a)
# for complex numbers it returns magnitude:
complex = (3 - 4j)
print(abs(complex)) # should be 5.0

print("\n-----------------all()-----------------\n")
# all() returns True when all elements in iterable are true
# any iterable (list, tuple, dictionary, etc.) which contains elements
iterable = {"first": True, "second": 1, "third": "three"}
print(all(iterable))
iterable = {"first": True, "second": False, "third": "three"}
print(all(iterable))

print("\n-----------------any()-----------------\n")
# any() Checks if any Element of an Iterable is True:
listWithTrue = [1, "two", True]
listWithOneFalse = [2, "two", 0]
listWithAllFalse = [0, False]
# returns:
# True if at least one element is true
# False if all are false or an iterator is empty
print("any()", any(listWithTrue))
print("any()", any(listWithOneFalse))
print("any()", any(listWithAllFalse))

print("\n-----------------ascii()-----------------\n")
# ascii() Returns String Containing Printable Representation
wierdText = "aącćzżźoólłeę"
wierdList = ["aącćzżźoólłeę", "AĄ", "ZŻŹ"]
print(ascii(wierdText))
print(ascii(wierdList))

print("\n-----------------bin()-----------------\n")
# bin() converts integer to binary string
num = 5
notNum = "not a number"
print("binary representation of", num, "is", bin(num))
try:
    print("binary representation of", notNum, "is", bin(notNum))
except TypeError:
    print(notNum, "- this is NaN - Type Error!!!")

# Convert an object to binary implementing __index__() method:
class Quantity:
    apple = 2
    orange = 3

    def __index__(self):
        return self.apple + self.orange

    def __bool__(self):
        return 0

print("bin(Quantity()) now returns: ",bin(Quantity()), "bacause __index__() method was defined")

print("\n-----------------bool()-----------------\n")
# bool() Converts a Value to Boolean
# False if the value is omitted or false
# True if the value is true
# False on Python: False, None, 0, 0.0, 0j, [], (), '', {}, objects of Classes which has __bool__() or __len()__ method which returns 0 or False
listEmpty = []
listFalse = [False, None, 0, 0.0, 0j, [],  (), '', {}, Quantity()]
print(bool(listEmpty))

print("\n-----------------bytearray()-----------------\n")
# bytearray() returns array of given byte size

print("\n-----------------bytes()-----------------\n")
# bytes() returns immutable bytes object

print("\n-----------------callable()-----------------\n")
# callable() Checks if the Object is Callable
# The callable() method takes a single argument object.
# True - if the object appears callable
# False - if the object is not callable.
x = 5
string = "sadfasd"
def callableFunction():
    print("test")

y = callableFunction
print(callable(x))
print(callable(string))
print(callable(callableFunction))
print(callable(y))

print("\n-----------------chr()-----------------\n")
# chr() Returns a Character (a string) from an Integer
# returns a character (a string) whose Unicode code point is the given integer
print(chr(1))
print(chr(55))
print(chr(1200))
try:
    print(chr(-1))
except ValueError:
    print(" -1 is not in range (0x110000)")

print("\n-----------------classmethod()-----------------\n")
# classmethod() returns class method for given function CHECK: https://www.programiz.com/python-programming/methods/built-in/classmethod
# classmethod() is considered un-Pythonic so in newer Python versions, you can use the @classmethod decorator for classmethod definition.
# The classmethod() method takes a single parameter: function - Function that needs to be converted into a class method
# The classmethod() method returns a class method for the given function.
# A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.
# The difference between a static method and a class method is:
#
#     Static method knows nothing about the class and just deals with the parameters
#     Class method works with the class since its parameter is always the class itself.
#
# The class method can be called both by the class and its object:
#     Class.classmethod()
#     Or even
#     Class().classmethod()
# But no matter what, the class method is always attached to a class with first argument as the class itself 'cls'.
# def classMethod(cls, args...)

print("\n-----------------compile()-----------------\n")
# compile() Returns a Python code object
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString ,"sumstring", "exec")
print(codeObejct)
exec(codeObejct)

print("\n-----------------complex()-----------------\n")
# complex() Creates a Complex Number
# In general, the complex() method takes two parameters:
#
#     real - real part. If real is omitted, it defaults to 0.
#     imag - imaginary part. If imag is omitted, it default to 0.
#
# If the first parameter passed to this method is a string, it will be interpreted as a complex number. In this case, second parameter shouldn't be passed.

# If the string passed to this method is not a valid complex number, ValueError exception is raised.

# z = complex(2, -3)
# print(type(z))
#
# z = complex(1)
# print(z)
#
# z = complex()
# print(z)
#
# z = complex('5-9j')
# print(z)

a, b, c, d = 2+3j, 3j, 0j, 0-0j
print(a, type(a), b, type(b), c, type(c), d, type(d))


print("\n-----------------delattr()-----------------\n")
# delattr() Deletes Attribute From the Object
# The delattr() takes two parameters:
#     object - the object from which name attribute is to be removed
#     name -  a string which must be the name of the attribute to be removed from the object
# The delattr() doesn't return any value (returns None). It only removes an attribute (if object allows it).

class Coordinates:
    x = 1
    y = 5
    z = 10

point1 = Coordinates()

print(point1.x, point1.y, point1.z)

delattr(Coordinates, "z")
try:
    print(point1.z)
except AttributeError:
    print("no 'z' coordinate in Coordinates()")

print("\n-----------------dict()-----------------\n")
# dict() Creates a dictionary
numbers = dict(x=1, y=2)
empty = dict()
print("numbers:",numbers, type(numbers))
print("empty:",empty, type(empty))

print("\n-----------------dir()-----------------\n")
# dir() Tries to Return Attributes of Object
number = [1, 2, 3]
print(dir(number))
print(dir())

class Person:
    def __dir__(self):
        return ['age', 'name', 'salary']

teacher = Person()
print(dir(teacher))

print("\n-----------------divmod()-----------------\n")
# divmod() Returns a Tuple of Quotient and Remainder
# divmod() takes two parameters:
#
#     x - a non-complex number (numerator)
#     y - a non-complex number (denominator)
# divmod() returns:
#
#     (q, r) - a pair of numbers (a tuple) consisting of quotient q and remainder r

print(divmod(4, 2))
print(divmod(6, 5))
print(divmod(1, 10))


print("\n-----------------enumerate()-----------------\n")
# enumerate() Returns an Enumerate Object
# The enumerate() method adds counter to an iterable and returns it (the enumerate object).
# You can convert enumerate objects to list and tuple using list() and tuple() method respectively.
# enumerate() method takes two parameters:
#
#     iterable - a sequence, an iterator, or objects that supports iteration
#     start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.
groceries = ["Beer", "Amarena", "2kC"]
enumerateGroceries = enumerate(groceries)
print(enumerateGroceries)
print(list(enumerateGroceries))
print(type(enumerateGroceries))
enumerateGroceries = enumerate(groceries, 11)
print(tuple(enumerateGroceries))

print("\n-----------------eval()-----------------\n")
# eval() Runs Python Code Within Program
# The eval() method parses the expression passed to this method and runs python expression (code) within the program.
# The eval() takes three parameters:
#
#     expression - this string as parsed and evaluated as a Python expression
#     globals (optional) - a dictionary
#     locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.
# The eval() method returns the result evaluated from the expression.
x = 1
print(eval("x + 1"))

print("\n-----------------exec()-----------------\n")
# exec() Executes Dynamically Created Program which is either a string or a code object.
# exec() takes three parameters:
#
#     object - Either a string or a code object
#     globals (optional) - a dictionary
#     locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.
# The exec() doesn't return any value, it returns None

program = "a = 5\nb=10\nprint('Sum =', a+b)"
exec(program)

