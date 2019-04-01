import math
import time
# 1 1 2 3 5 8 13 21


# My Decorator:
def logger_timer(original_function):
    import logging
    import time
    from functools import wraps
    logging.basicConfig(filename='{}.log'.format('myFiles/' + original_function.__name__), level=logging.INFO)
    # total1 = time.time()

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        elapsed = time.time() - t1
        logging.info('{0} ran with args: {1}, kwargs: {2}, time elapsed: {3}'.format(original_function.__name__, args, kwargs, elapsed))
        return result
    # total_elapsed = time.time() - total1
    # logging.info('Tototal time elapsed: {}'.format(total_elapsed))
    return wrapper


# function returning n-th Fibonacci number
# @logger_timer
def fibonacci_recursive(n):
    time.sleep(0.05)
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@logger_timer
def measure_fibonacci_recursive(n):
    return fibonacci_recursive(n)

# for n in range(0, 100):
#     print(n, ':', fibonacci_recursive(n))       # VERY SLOW!



# Memoization - store the values of recent function calls so future calls don't have to repeat calculations
# method 1 - memoization implemented explicitly:
fibonacci_cache = {}        # create a dictionary

# @logger_timer
def fibonacci_memoization(n):

    # if the value is cached - return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # if not cached:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        value = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    # store and return:
    fibonacci_cache[n] = value
    return value

# for n in range(0, 11):
#     print(n, ':', fibonacci_memoization(n))     # VERY FAST


@logger_timer
def measure_fibonacci_memoization(number_range):
    for n in number_range:
        print(n, ':', fibonacci_memoization(n))     # VERY FAST

# measure_fibonacci_memoization(range(0, 100))


# method 2 - with built-in tools:
from functools import lru_cache     # least recently used cache


# @logger_timer
@lru_cache(maxsize=3)        # maxsize specifies how many LAST used values should be stored
def fibonacci_recursive_lru(n):
    time.sleep(0.05)
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci_recursive_lru(n - 1) + fibonacci_recursive_lru(n - 2)

@logger_timer
def measure_fibonacci_recursive_lru(number_range):
    for n in number_range:
        print(n, ':', fibonacci_recursive_lru(n))     # FAST


# measure_fibonacci_recursive_lru(range(0,100))       # time: 6.015887260437012
# measure_fibonacci_memoization(range(0, 100))        # time 0.0
# measure_fibonacci_memoization(range(0, 1000))        # time 0.0312
# measure_fibonacci_memoization(range(0, 10000))        # time 16.782



# Golden Ratio:
for n in range(1,1001):
    print(n, ':', fibonacci_memoization(n + 1) / fibonacci_memoization(n))
