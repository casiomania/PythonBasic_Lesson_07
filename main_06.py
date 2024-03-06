# Lesson 07 / Homework 06
# Write a function that calculates the degree of each element of the list of integers.
# The value for the degree is passed as a parameter, the list is also passed as a parameter.
# The function returns a new list containing the results.

def calculate_power_list(lst, power):
    powered_list = [num ** power for num in lst]
    return powered_list


try:
    spec_list = [2, 5, 7, 8]
    value = 2
    result = calculate_power_list(spec_list, value)
    print(f"List after calculating the degrees: {result}")

except Exception as error:
    print(f"Error: {error}")
