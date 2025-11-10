# Python Functions

# A function is a reusable block of code that is defined once and only executes when you 'call' it.
# Functions help organize your code and prevent repetition.
# Often, a function will process data and send a value back to the main program using the return keyword.

def add_numbers(a, b):
    return a + b

sum_value = add_numbers(1, 2)
print(sum_value)

another_sum_value = add_numbers(1, 5)
print(another_sum_value)