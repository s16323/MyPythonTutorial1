import sys
sys.path.append('C:/Users/Artur/Desktop/TESTY WYDAJNOSCI/Python Projects')      # to add a custom directory to sys.path when a module is somewhere else
import MyModules
print(sys.path)         # shows where Python looks for modules when 'import' is used - now new directory is visible
'''
1. this location
2. python path env. variable
3. std. lib. directory
4 site-packages - fer 3 party packages
'''
# Also a new environment variable can be adder - variable name: PYTHONPATH with variable value: a directory where custom packages will be
# now this new path will also be checked by sys.path for modules to import
# check   https://www.youtube.com/watch?v=CqvZ3vGoGs0   for advanced importing

# Standard Library:

print("\n----------random:-----------\n")
import random
courses = ['History', 'Math', 'Physics', 'CompScience']

# Grab a random value from a list:
random_course = random.choice(courses)
print(random_course)

print("\n----------math:-----------\n")
import math

rads = math.radians(90)     # to radians
print(rads)
print(math.sin(rads))

print("\n----------time, datetime and calendar:-----------\n")
import datetime
import calendar
import time

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))        # is it a leap year?

print("\n----------os:-----------\n")
# access underlying operating system
import os

# print(dir(os))        # get modules functions
# print(dir(os.path))
print(os.getcwd())      # get current working directory
print(os.__file__)      # print out the lcation of this file
# print(datetime.__file__)
# print(math.__file__)
# os.chdir()             # change current directory
print(os.listdir())      # get files and catalogs - pass a directory or () for current
# os.mkdir()               # make sngle dir here (path)
# os.mkdirs()              # make dir many levels deep (path/path/path)
# os.rmdir()               # will NOT remove intermediate directories
# os.removedirs()          # will remove everything on the path (!)
# os.rename(oldname.txt, newname.txt)              # rename a file
print('\n', os.stat('myFiles/plik.txt'))            # get atributes of a file
print('\n', os.stat('myFiles/plik.txt').st_size)        # get a specific atribute - size
print('\n', os.stat('myFiles/plik.txt').st_mtime)       # get a specific atribute - last modification time
# mod_time = os.stat('myFiles/plik.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))           # fromtimestamp DOS NOT WORK for some reason
'''
# os.walk()                   # .walk - a generator that yields a tuple of 3 values walking through a directory tree: path, directories in path, files in path
for dirpath, dirnames, filenames in os.walk('C:\\Users\Artur\Desktop\TESTY WYDAJNOSCI\Python Projects\MyPythonTutorial1'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    
# This can be used to walk through every file and every directory that starts with the 'path' - can browse and than be checked for whatever file name or other atribute we look for - very powerful!
'''
print('\n', os.environ.get('DriverData'))       # Get environment variable (for ex. DriverData) path:
'''
# os.path.join(path1, path2)                    # join 2 paths. Can be alco concatenated normally, but than it's easy to forget or dpuble a slash
'''

# print('\n', os.path.join('C:\\Users\Artur\Desktop\TESTY WYDAJNOSCI\Python Projects\MyPythonTutorial1', 'dir1\dir2/file.txt'))        # note that slashes are actually not correct
print('\n', os.path.basename('/jakis/path/plik.txt'))       # gets /plik.txt name
print('\n', os.path.dirname('/jakis/path/plik.txt'))       # gets directory name
print('\n', os.path.split('/jakis/path/plik.txt'))       # gets both in a tuple
print('\n', os.path.exists('/jakis/path/plik.txt'))       # Does the path exist?
print('\n', os.path.isdir('/jakis/path/plik.txt'))       # Is this a directory?
print('\n', os.path.isfile('/jakis/path/plik.txt'))       # Is this a file?
print('\n', os.path.splitext('/jakis/path/plik.txt'))       # Split file name and its extension - return a tuple - This is great to change extensions, create new files with new extensions..





print("\n----------webbrowser:-----------\n")
import webbrowser

print("\n----------hashlib:-----------\n")
import hashlib

print("\n----------antigravity:-----------\n")
# ?!
#import antigravity
#print(antigravity.__file__)