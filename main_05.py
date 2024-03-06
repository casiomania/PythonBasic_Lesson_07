# Lesson 07 / Homework 05
# Write a function that takes two lists as a parameter and returns a list containing the elements of both lists.

def merge_lists(first_list, second_list):
    merged_list = first_list + second_list
    return merged_list


try:
    spec_list_1 = [2, 5, 7, 8]
    spec_list_2 = [2, 5, 7, 8]
    result = merge_lists(spec_list_1, spec_list_2)
    print(f"Merged list: {result}")

except Exception as error:
    print(f"Error: {error}")

