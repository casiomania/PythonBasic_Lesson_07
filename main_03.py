# Lesson 07 / Homework 03
# Write a function that determines the number of primes in a list of integers.
# The list is passed as a parameter. The result is returned from the function.

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_count(list_of_int_numbers):
    return sum(1 for num in list_of_int_numbers if prime(num))


try:
    spec_list = [2, 5, 7, 8]
    print(f"Qty of primes in the list {spec_list} is equal to {primes_count(spec_list)}" )

except Exception as error:
    print(f"Error: {error}")
