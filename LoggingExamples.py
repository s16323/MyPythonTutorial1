import logging

# to make a custom logger:
logger = logging.getLogger(__name__)            # __name__ = module name when imported, __name__ = __main__ when ran directly
                                                # we are now getting a new logger
                                                # log now is: "2019-04-02 14:53:55,804:INFO:__main__:Created employee: John Smith - John.Smith@email.com"
                                                # 'root' changed to '__main__' when ran locally
                                                # log is now also:"2019-04-02 14:55:21,797:INFO:LoggingExamples:Created employee: John Smith - John.Smith@email.com"
                                                # 'root' changed to 'LoggingExamples' when ran from an import
                                                # this new logger should be used for logging in this module, so let's change 'logging.info' to 'logger.info':

# first make a file handler to specify the .log file
file_handler = logging.FileHandler('myFiles/Employee.log')

#now add this new handler to the custom logger
logger.addHandler(file_handler)

# now add custom formating to the file handler (not the logger)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# adn add it to the file handler
file_handler.setFormatter(formatter)

# set the log level on this 'LoggingExamples' logger
logger.setLevel(logging.INFO)
# and now delete basic configuration.. custom one is in place

# logging.basicConfig(filename='myFiles/example.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


print('\n--------Example--------\n')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created employee: {} - {}'.format(self.fullname, self.email))
        # logging.info('Created employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('AAA', 'BBB')
emp3 = Employee('CCC', 'DDD')

'''
log:
2019-04-02 14:17:38,643:INFO:root:Created employee: John Smith - John.Smith@email.com

INFO:   level=logging.INFO 
root:   logger - default logger if no other specified
'''
