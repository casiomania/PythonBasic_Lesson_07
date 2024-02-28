# Lesson 07 / Homework 01
# Write a function that calculates the product of the elements of a list of integers.
# The list is passed as a parameter. The result is returned from the function.

def product_list(list_of_int_numbers):
    result = 1
    for num in list_of_int_numbers:
        result *= num
    return result


try:
    spec_list = [2, 5, 7, 8]
    print(f"Product of elements in list {spec_list} is equal to {product_list(spec_list)}.")
except Exception as error:
    print(f"Error: {error}")
