# https://www.youtube.com/watch?v=swU3c34d2NQ
# Closures:
# In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language
# with first-class functions. Operationally, a closure is a record storing a function[a] together with an environment.[1] The environment is a mapping associating
# each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound
# when the closure was created.[b] Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references,
# even when the function is invoked outside their scope.


def outer_funct():              # outer_function takes no parameters
    message = 'Hi'              # holds its own variable with a value

    def inner_function():       # also takes no parameters
        print(message)          # but can access 'message' variable - this is called a 'free variable' because it is accessible by 'inner_function()' though not passed directly to it

    return inner_function()     # here 'inner_function()' is executed and its output is returned by 'outer_function()'


outer_funct()                   # executing 'outer_funct()' means in fact executing its 'nner_function()' - than 'Hi' will be printed when outer_function is called


print("\n-----------------Closure in action-----------------\n")
# Now a different example -  let's not execute 'inner_function()' on return - just drop '()':

def outer_funct():
    message = 'Hi'

    def inner_function():
        print(message)          # access to free variable

    return inner_function       # here 'inner_function()' is NOT executed. A function returns a function. 'First-Class-Function'


my_func = outer_funct()         # we create a new function that behaves like 'inner_function()' and has access to message = 'Hi'

# checking where we are:
print(my_func)                  # to check what it is
print(my_func.__name__)         # to check just the name... indeed it shows 'inner_function'

# using 'my_func()'
my_func()                       # here is a closure in action - 'outer_funct()' is not being called, only the 'inner_function()'... but still 'message' is remembered and gets printed
                                # So.. a closure is an inner function that remembers and has access to variables in the local scope in which it was created, even after the outer function finished executing
                                # A closure 'closes over' free variablef from its environment - in this case the environment is 'outer_funct()' and a closure is 'inner_function()'

print("\n-----------------Closure with parameters-----------------\n")


def outer_funct(msg):           # now the same, but we also pass a parameter
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_funct =  outer_funct('Hi')           # makes a 'inner_function' and remembers 'Hi' - a closure with 'Hi' stored
hello_funct =  outer_funct('Hello')     # makes a 'inner_function' and remembers 'Hello' - a closure with 'Hello' stored

hi_funct()                              # should print 'Hi'
hello_funct()                           # should print 'Hello'


print("\n-----------------Advanced Example-----------------\n")

import logging
logging.basicConfig(filename='myFiles/example.log', level=logging.INFO)         # log into a specified file


def logger(func):                      # outer function

    def log_func(*args):                # *args - can accept any number of args
        logging.info('Running function: {} with arguments: {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)        # here we set what function should be used
sub_logger = logger(sub)

add_logger(3, 4)                # here we give arguments to add and execute
sub_logger(10, 5)

# check myFiles/example.log - all operations should be there

# this can be achieved with DECORATORS...