# get factorial of a number

# My Decorator:
def logger_timer(original_function):
    import logging
    import time
    from functools import wraps
    logging.basicConfig(filename='{}.log'.format('myFiles/' + original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        elapsed = time.time() - t1
        logging.info('{0} ran with args: {1}, kwargs: {2}, time elapsed: {3}'.format(original_function.__name__, args, kwargs, elapsed))
        return result
    return wrapper



@logger_timer
def factorial(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    return f

@logger_timer
def factorial_recursive(x):
    if x == 0:
        return 1
    return x * factorial_recursive(x - 1)


print(factorial(10))
print(factorial_recursive(10))

