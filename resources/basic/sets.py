# Python Set

# A Set is used to store a collection of unique items in a single variable.
# It's one of Python's four built-in collection types, alongside List, Tuple, and Dictionary, each with different uses.
# A set is an unordered and unindexed collection, meaning the items have no specific sequence or position

fruits = {"apple", "orange", "banana", "cherry"}
print(fruits)

fruits = {"apple", "orange", "banana", "cherry", "apple", "apple", "banana", "cherry"}
print(fruits)

fruits = {"apple", "orange", "banana", "cherry", True, 1, 0, False}
print(fruits)

# The add() method is used to insert a single item into a set.
fruits.add("kiwi")
print(fruits)

# The update() method merges all items from another set into the current one.
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print(fruits)

# The remove() method deletes a specific item, but will raise an error if the item isn't found.
fruits.remove("pineapple")
print(fruits)