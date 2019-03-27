# iterator - an object with a state so that it remembers where it is during iteration and knows how to get its next value with a __next__() method

# iterable - Something that can be looped over, for ex. a list, tuple, dictionary, strings, files, generators...
iterableList = [1, 2, 3]

# looping over this list:
# for number in iterableList:
#     print(number)

# Is something iterable???
# --> It needs to have a special method: __iter__()
# use built-in dir() function to print out methods and atributes of an object
print(dir(iterableList))        # is there a __iter__() method? --> YES --> the list is iterable
                                # is there a __next__() method? --> NO --> the list is NOT an iterator, so:
try:
    print(next(iterableList))
except TypeError:
    print("no such method as __next__() - list is NOT an iterator!")

print("\n-----------------creating iterator:-----------------\n")

i_iterableList = iterableList.__iter__()        # an iterator made for this list, let's check what it has:

print(i_iterableList)
print(dir(iterableList))

print("\n-----------------nice way to do this:-----------------\n")

i_iterableList = iter(iterableList)             # does the same, but this is how it's supposed to be run

print(i_iterableList)
print(dir(iterableList))

print("\n-----------------now check if next() works with an iterator of the list:-----------------\n")

print(next(i_iterableList))     # gives first value
print(next(i_iterableList))     # gives next value - it remembers where it was before, and so on...
print(next(i_iterableList))
# print(next(i_iterableList))     # too much - will throw 'StopIteration' exception (so commenting out, because it breakes herre)

# impotrant!
# This is what a 'for' loop does in fact in the background - it creates an iterator of our object that we want to loop over, than iterates it until the las one. Handles 'StopIteration' in the background

print("\n-----------------The same as above, but now steps are visible in the code:-----------------\n")

iterableList2 = [4, 5, 6]
i_iterableList2 = iter(iterableList2)

while True:
    try:
        item = next(i_iterableList2)
        print(item)
    except StopIteration:
        break

# iterators can only go forward - no reseting or copying, to start from scrach create a new iterator object

print("\n-----------------Example1 - My Own Iterable Class:-----------------\n")

