import logging
import LoggingExamples          # imports Employee class - CAUTION - There is a logging.basicConfig already in there witl 'root' logger, it will OVERRIDE local (also 'root')!!!
                                # LoggingExamples module has logging level=logging.INFO, so local logging with level=logging.DEBUG doesn't reach that.
                                # It would actually log if the level was also level=logging.INFO, but this is not the point...
                                # to get rid of that and get two separate logs, 'logger' should be custom configured for each module
                                # lets configure loggers...



# After seting custom logger in 'LogggingExamples' module this local logging.basicConfig works as intended
# 'LoggingExamples' is ran from import and also logs, but to its custom directory with custom settings

# Lets setup this local logger also.. make it custom:
logger = logging.getLogger(__name__)                                                # name the new logger (create if doesn't exist)
logger.setLevel(logging.DEBUG)                                                      # set level

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')                 # create a formater with a custom format configuration

file_handler = logging.FileHandler('myFiles/simpleFunctions.log')                   # createa a file handler with a custom path
file_handler.setLevel(logging.ERROR)                                                # OPTIONAL - level can be changed per handler.. so now nothing except ERRORs will be logged, this overrides loggers own level
file_handler.setFormatter(formatter)                                                # assign formatter to file handler

#more options.. for example to log into the console also, let's make another handler:
stream_handler = logging.StreamHandler()            # no need to set level.. logger already has its level
stream_handler.setFormatter(formatter)              # to decide how console output should look like.. in this case the old 'formatter' is left.. but you could make a custom one as well

logger.addHandler(file_handler)                                                     # add file handler to new logger
logger.addHandler(stream_handler)                                                   # add also stream handler.. can be many handlers
# now delete basicConfig - for more explanation check LoggingExamples module
# logging.basicConfig(filename='myFiles/example.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

# Remember to change 'logging.debug(...)' in functions below to new 'logger.debug(...)' (!)


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
    try:
        result =  x / y
    except ZeroDivisionError:
        # logger.error('No division by zero')
        logger.exception('No division by zero')         # change to exception to also get traceback in the log - nice way for errors
    else:
        return result


num_1 = 10
num_2 = 0

results = []

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
results.append(add_result)

sub_result = sub(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
results.append(sub_result)

mul_result = mul(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
results.append(mul_result)

div_result = div(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
results.append(div_result)


print(results)
print(type(results))
