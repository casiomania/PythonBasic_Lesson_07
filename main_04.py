# Lesson 07 / Homework 04
# Write a function that removes a given integer from the list.
# From the function, you need to return the number of deleted items.

def remove_number(specified_list, num):
    qty = specified_list.count(num)
    specified_list[:] = [x for x in specified_list if x != num]
    return qty


try:
    number_to_remove = 2
    my_list = [2, 5, 7, 8, 2, 2]

    print(f"In list: {my_list}")

    removed_qty = remove_number(my_list, number_to_remove)

    print(f"The number {number_to_remove} removed {removed_qty} times.")

except Exception as error:
    print(f"Error: {error}")

