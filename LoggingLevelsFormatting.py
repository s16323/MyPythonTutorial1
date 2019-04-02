import logging
logging.basicConfig(filename='myFiles/example.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
'''
https://www.youtube.com/watch?v=-ARI4Cz-awo
logging levels:
1.DEBUG - Detailed info for diagnostics
2.INFO - Confirmation that things are working
3.WARNING - Software is still working but something bad may happen in the future for ex. 'disk space low'
4.ERROR - Software was unable to perform some function
5.CRITICAL  - Serious error, the program may crash

Default level = WARNING --> will catch anything that is a warning or above (ignore DEBUG and INFO)
'''


def add(x, y):
    '''add function'''
    return x + y


def sub(x, y):
    '''subtraction function'''
    return x - y


def mul(x, y):
    '''multiplication function'''
    return x * y


def div(x, y):
    '''division function'''
    return x / y


print('\n--------Logging--------\n')


num_1 = 10
num_2 = 5


add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))             # let's change this to logging:
# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))     # by default ogs into the console, but default logging level=WARNING, so it will not show, so lets change the level:
# logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))   # but this are not actually 'warnings' so this is wrong usage of logging, these lines would rather fit DEBUG or INFO

# So to change the way logging behaves the basic configuration for logging should be changed:
# logging.basicConfig(level=logging.DEBUG)        # logging.DEBUG is just a constant, differrent than logging.debug (a function), so we can just set it and go back to normal usage of logging.debug
# now:
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))      # is actually visible in the console

# let's now create a .log file:
# logging.basicConfig(filename='myFiles/example.log', level=logging.DEBUG)        # now everything goes to the file - this goes to the top, under imports


sub_result = sub(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = mul(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = div(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


print('\n--------Change the format--------\n')
'''
To change the format in the log some special values should be added to basicConfig.
Check Python documentation (log level atributes) for availble formats:   https://docs.python.org/3/library/logging.html#logrecord-attributes

Lets use: time, level name, message
% (asctime)s
%(levelname)s
%(message)s

log:
2019-04-02 14:14:06,533:DEBUG:Add: 10 + 5 = 15

'''
