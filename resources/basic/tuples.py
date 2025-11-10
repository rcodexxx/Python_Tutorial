# Python Tuple

# A tuple allows you to store a group of items in one variable
# A Tuple is one of Python's four built-in data structures for storing collections.
# The other three—List, Set, and Dictionary—each have unique characteristics and applications.
# A tuple is a collection that maintains the order of its items and cannot be modified after it is created.
# Tuples are defined using round brackets ().

weekdays = ("Monday", "Tuesday", "Wednesday")
print(weekdays)

# A tuple's items stay in a fixed sequence, cannot be altered after creation, and allow for the same item to appear multiple times.
print(weekdays[0])
print(weekdays[1])

scores = (100, 80, 95, 80, 100, 80)
print(scores)

# You can access items in a tuple using the same indexing method as a list.
print(weekdays[-1])
print(weekdays[1:2])

# The count() method returns the number of times a specific value appears in the list or tuple.
data = ("a", "b", "c", 'a', 'b', 'c')
print(data.count("a"))

# The index() method searches for a value and returns the index (position) of its first occurrence.
print(data.index("b"))