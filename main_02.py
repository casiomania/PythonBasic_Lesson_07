# Lesson 07 / Homework 02
# Write a function to find the minimum in a list of integers.
# The list is passed as a parameter. The result is returned from the function.

def min_list(list_of_int_numbers):
    result = list_of_int_numbers[0]
    for num in list_of_int_numbers:
        if num < result:
            result = num
    return result


try:
    spec_list = [2, 5, 7, 8]
    print(f"From the list items {spec_list} min is equal to {min_list(spec_list)}.")
except Exception as error:
    print(f"Error: {error}")
