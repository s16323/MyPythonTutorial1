# First-Class functions:
# A programming language is said to have First-class functions when functions in that language are treated like any other variable
# First-Class Citizen - n programming language design, a first-class citizen (also type, object, entity, or value) in a given programming language
# is an entity which supports all the operations generally available to other entities.
# These operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable
# Higher Order Function - a function that accepts other functions as arguments
# https://www.youtube.com/watch?v=kr0mpwqttM0
def square(x):
    return x * x

f = square(5)           # a value that is return by the function is assigned to a variable

print(square(5))        # a value that is return by the function is passed as an argument
print(square)           # a function itself is passed as an argument (!)

f = square              # a function itself is assigned to a variable (!) which now represents this function (!)
print(f)                # a function itself is passed as an argument (!)
print(f(5))             # (!)

print("\n----------passing a function to other function-----------\n")
# passing a function that accepts other functions as argument example:
# map() - accepts a function and an array of arguments, returna an array of results of given function with given arguments

def my_map(funct, arg_list):        # my own map() function equivalent
    result = []
    for i in arg_list:
        result.append(funct(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])       # NOT 'square()' - bacause we don't want to execute square function (!) just pass it as an argument
print(squares)


def cube(x):
    return x * x * x


cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)

cubedsquares = my_map(cube, squares)
print(cubedsquares)

print("\n----------returning a function by another function-----------\n")
# returning a function by another function as a result:

def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message          # a function is not executed, only returned

log_hi = logger('Hi!')          # log_hi is now a function --> exactly it is 'log_message()'
log_hi()                        # called with no args (cause it accepts no args) BUT THE msg IS REMEMBERED

print("\n----------practical example:-----------\n")

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')        # remember what tag. print_h1 is now wrap_text()
print_h1('My Text')              # the same as wrap_text('My Text')
print_h1('Another Text')         # and so on... 'tag' is still remembered (!)

print_p1 = html_tag('p1')        # a net 'tag' is introduced
print_p1('A Paragraph')          # ...and used fro now on


# JAVASCRIPT DOES THE SAME !



# Closures




# Decorators:
