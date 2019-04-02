import logging
logging.basicConfig(filename='myFiles/example.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


print('\n--------Example--------\n')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created employee: {} - {}'.format(self.fullname, self.email))
        logging.info('Created employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('Dupa', '666')
emp3 = Employee('Kutas', 'Kozla')
