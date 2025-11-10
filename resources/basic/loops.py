# Python Loops

""" For Loops """

# A for loop executes a block of code once for every item in a sequence (like a list, tuple, set, or string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Strings are iterable objects as well, meaning you can process them as a sequence, one character at a time.
for x in "banana":
  print(x)

# Use the break statement to exit the loop immediately, even if it hasn't finished iterating through all the items.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Use the continue statement to skip the rest of the code in the current iteration and move directly to the next item in the loop.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() function generates a sequence of numbers, by default starting from 0 and incrementing by 1,
# stopping just before it reaches the specified end number.
for x in range(6):
  print(x)

""" While Loops """
# A while loop repeatedly executes a block of code as long as a specified condition remains true.
i = 1
while i < 6:
  print(i)
  i += 1