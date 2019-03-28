# Decorators

# First check:
# - First-Class-Functions - treat functions as any other object
# - Closures              - return inner function that remembers and has access to free variables - variables local to the scope (environment/outer function) of inner function

# Quick closures and First_Class_functions recap example:

def outer_function(msg):
    def inner_function():
        print(msg)          # inner has access to free variable 'message'
    return inner_function       # return a First-Class-Function

hi_func = outer_function("Hi")            # assigns inner (by calling outer first) to 'hi_func' variable
bye_func = outer_function("Bye")

hi_func()                       # calls inner
bye_func()

# Decoator - a function that takes another function as an argument adds some kind of functionality and thar returns another function
# without altering the source code of original function

print("\n----------Example simple decorator:-----------\n")
# this decorator actually doesn't change anything in 'original_function' - this is very simple and not very useful...

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def my_display():
    print('my_display function ran')

decorated_my_display = decorator_function(my_display)
decorated_my_display()                                      # now actually 'wrapper_function' is executed, and it's executing the 'original_function'


print("\n----------Example decorator that does something to original function:-----------\n")
# decorating a function lets us easily add functionality to our original_function

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper_function() executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


def my_display():                               # original function
    print('my_display function ran')


decorated_my_display = decorator_function(my_display)
decorated_my_display()                          # wrapper executed - original function wrapped in a wrapper - so changed by the wrapper


print("\n----------The same but using correct syntax with '@':-----------\n")


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper_function() executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function                             # this means - every time you call 'my_display():' - actually call a decorator_function with 'my_display()' passet to it as an argument
def my_display():                               # original function
    print('my_display function ran')

# In use:
my_display()                                    # now, even though only 'my_display()' os called it still is being decorated on the way, so actually 'wrapper_function()' is in work here

#What happens actually is:
# my_display = decorator_function(my_display)     # first decorate
# my_display()                                    # than execute


print("\n----------When original function takes arguments:-----------\n")
# What happens when original function takes some arguments?

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):                                                           #take any number of args and keywords
        print('wrapper_function() executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)                                                    # execute original with any number of args and keywords
    return wrapper_function



@decorator_function
def display_info(name, age):
    print('display_info ran with args: ({}, {})'.format(name, age))


display_info('John', 25)


print("\n----------using classes as decorators:-----------\n")
# this is just an option, does the same.

class DecoratorClass:

    def __init__(self, original_function):
        self.original_function = original_function                                                      # this will tye our function with an instance of this class

    def __call__(self, *args, **kwargs):                                                                # this will behave just like wrapper behaved
        print('__call__() method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_info(name, age):
    print('display_info ran with args: ({}, {})'.format(name, age))


display_info('John', 25)


print("\n----------practical example of decorator - loging and a timer:-----------\n")
# typical example of decorator use is logging - how to keep track of how many times a function was run and with what arguments...

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format('MyFiles/' + original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Wrapper ran with args: {}, kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):                                                # a decorator that will measure how long 'original_function' will take to execute
    import time
    def wrapper(*args, **kwargs):                                               # wrapper must obviously take (*args, **kwargs) for the function inside that it will be executing
        t1 = time.time()                                                        # measure current time
        result = original_function(*args, **kwargs)                             # execute original_function with its *args and **kwargs (in other words - do whatever you need to do now)
        t2 = time.time() - t1                                                   # measure time passed
        print('{} ran for {} seconds'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_timer
def display_info(name, age):
    import time
    time.sleep(1)       # this is to better see how time passes for this function to execute
    print('display_info ran with args: ({}, {})'.format(name, age))


display_info('John', 25)


print("\n----------decorators chained together:-----------\n")

# order is important. This will measure time of wrapper instead of display_info:
# @my_timer
# @my_logger

# order is important. This will log wrapper instead of display_info:
# @my_logger
# @my_timer

# Why? Because:
# @my_logger
# @my_timer
# =
# display_info = my_logger(my_timer(display_info))

# To fix this:
# To preserve the information of 'original_function' use:
from functools import wraps


def my_logger2(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format('MyFiles/' + original_function.__name__), level=logging.INFO)

    @wraps(original_function)                                                                                   # preserve original_function using functools.wraps
    def wrapper(*args, **kwargs):
        logging.info('{} ran with args: {}, kwargs: {}'.format(original_function.__name__, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer2(original_function):
    import time

    @wraps(original_function)                                                                                    # preserve original_function using functools.wraps
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran for {} seconds'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_logger2                                                  # now 'original_function' - display_info(name, age) should be preserved
@my_timer2
def display_info(name, age):
    import time
    time.sleep(1)       # this is to better see how time passes for this function to execute
    print('display_info ran with args: ({}, {})'.format(name, age))


display_info('John', 25)
