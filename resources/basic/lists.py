# Python List

# A list holds a collection of items under one name.
fruits = ["apple", "banana", "cherry"]
print(fruits)

# A List keeps its items in a specific sequence, can be modified after it's made, and lets you store the same item more than once.
print(fruits[0]) # apple
print(fruits[1]) # banana

fruits[1] = "blueberry"
print(fruits)

fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
print(fruits)

# If you want to know the total count of items in a list, you can use the len() function. It returns the list's length (or size)
print(len(fruits))

# A list is very flexible; it can hold different data types all in the same list. You can mix strings, numbers, and even other lists together
list1 = ["abc", 34, True, 40, "male"]

# With negative indexing, -1 refers to the last item, -2 to the second-to-last, and so on.
print(fruits[-1])
print(fruits[-2])

# Specifying a range of indexes (with a start and end point) returns a new list containing only the items within that specified slice
print(fruits[1:3])

# The append() method is used to add a new item to the very end of a list.
fruits.append("mango")
print(fruits)

# Use the insert() method to add a new item to a list at a specified index.
fruits.insert(1, "papaya")
print(fruits)

# For remove(): "The remove() method deletes an item based on its value.
fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
fruits.remove("banana")
print(fruits)

# For pop(): "The pop() method deletes an item based on its index (position).
fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
fruits.pop(2)
print(fruits)

fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
fruits.pop()
print(fruits)

# The clear() method removes all items from a list, leaving the list itself intact but empty.
fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
fruits.clear()
print(fruits)


