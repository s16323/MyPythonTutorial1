# pass - w Pythonie, żeby utworzyć klasę trzeba napisać min 1 linię z TABem pod spodem, w tym wypadku nie chcemy nic pisać więc jest neutralne słowo 'pass', które nic nie robi

#własna klasa wyjątku:

class TooColdException(Exception):        # (Exception) - bo chcemy dziedziczyć po domyślnym wyjątku

      def __init__(self, temp):
          super().__init__("Temperature {} below absolute 0!".format(temp))     # uruchamiamy __init__() należący do rodzica - podajemy "nasz tekst" i zmierząną 'temp' jako argumenty



def celcius_to_kelvin(temp):

    if temp < -273.15:
        raise TooColdException(temp)           # raise powoduje wywołanie wuyjątku / też przekazujemy temperaturę 'temp' do __init__() klasy wyjątku
    return temp + 273.15                       # raise działa jak return - przerywa kod, tylko, ze dla wyjątków

print(celcius_to_kelvin(-300))

