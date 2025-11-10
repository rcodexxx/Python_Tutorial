# Python Dictionary

# A dictionary is an ordered, changeable collection that stores data values in key:value pairs and does not allow duplicate keys.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

# A dictionary is an ordered and changeable collection of key:value pairs;
# it does not allow duplicate keys, and you use the key to access its corresponding value.

# To access a value in a dictionary, use its corresponding key name inside square brackets [].
print(car["brand"])
print(car.get("brand"))

# The keys() method provides a list of all the keys currently in the dictionary.
print(car.keys())

# The values() method provides a list of all the values currently in the dictionary.
print(car.values())

# The items() method provides a list of all the (key, value) pairs from the dictionary, with each pair structured as a tuple.
print(car.items())

# You can update the value of a specific item by assigning a new value to its key.
car["year"] = 2020
print(car)

# Use the update() method to add all the items from a given argument into the current dictionary.
car.update({"year": 2020})
print(car)

# You can either assign a value directly to a key using [], or merge another dictionary using the update() method.
car["color"] = "white"
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "white"})
print(car)

# The pop() method removes a specific item from the dictionary using its key name.
car.pop("color")
print(car)

# The popitem() method removes the last item that was inserted into the dictionary.
# (Note: In Python versions older than 3.7, this method removed a random item.)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "white"
}
car.popitem()
print(car)