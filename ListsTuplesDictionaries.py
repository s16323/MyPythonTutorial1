# Lists  <class 'list'>

products = []
print(products, type(products))
print("----------------------------------------")

products = ["cocaine", "MDMA", "LSD", "Marihuana"]
print(products, type(products))
print(products[0], type(products))
print(products[0:2], type(products))
print("----------------------------------------")

# Functions of <class 'list'>

products.append("Amphetamine")
print(products[-1], type(products))
print(products.count("Amphetamine")) # count() takes exactly 1 argument!

moreProducts = ["Vodka", "Beer", "Amarena"]
products.extend(moreProducts)
print(products)
print(products.index("Amphetamine"))    # gives items position in the list
products.insert(4, "Shrooms")
print(products)
products.remove("Shrooms")
print(products)
products.pop(5)     # pop takes 1 arg
print(products)
products.clear()
print(products, type(products))
print("----------------------------------------")


# Tuples <class 'tuple'>
# can't be edited --> are faster than lists

products = ("cocaine", "MDMA", "LSD", "Marihuana")
print(products, type(products))
print("----------------------------------------")

# Dictionaries
# custom keys with values

myDictionary = {
    "One": "cocaine",
    "Two": "MDMA",
    "Three": "LSD",
    "Four": "Marihuana",
    "Five": 5,       # this is int
    123: True
}

print(myDictionary, type(myDictionary))
print(myDictionary["One"], type(myDictionary["One"]))
print(myDictionary["Five"], type(myDictionary["Five"]))
print(myDictionary[123], type(myDictionary[123]))

# Functions of <class 'dict'>

print(myDictionary.get("Six", "defaultValue"))               # get by key, if not give default
print(myDictionary.keys(), type(myDictionary.keys()))        # <class 'dict_keys'>
print(myDictionary.values(), type(myDictionary.values()))    # <class 'dict_values'>

print(myDictionary.items(), type(myDictionary.items()))      # <class 'dict_items'>
myDictionary.clear()