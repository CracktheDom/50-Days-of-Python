#!/usr/bin/env python3

"""Write a function called prime_numbers. This function asks a
user to enter a number (integer) as an argument and returns a
list of all the prime numbers within its range. For example, if user
enters 10, your code should return [2, 3, 5, 7] as prime numbers."""


def prime_numbers() -> list[int]:
    """
    Calculate prime numbers up to a specified number.

    This function takes user input to determine the upper limit 'numbers,'
    then generates a list of prime numbers up to that limit.

    Returns:
        list: A list of prime numbers up to the specified limit.
    """
    # Prompt the user to enter a number to calculate primes up to that number
    numbers: int = int(input("Enter a number: "))

    # Generate a list of odd numbers up to 'numbers'
    num_list: list[int] = [
        number for number in range(2, numbers + 1) if number % 2 != 0
    ]

    # Insert the first prime number, 2, at the beginning of the list
    num_list.insert(0, 2)

    # Create a copy of the list to store the prime numbers
    primes_list: list[int] = num_list.copy()

    # Iterate through the list of odd numbers
    for number in num_list:
        # Check for divisors up to the square root of the number
        for i in range(2, (round(number**0.5) + 1)):
            # If the number is divisible and still in the prime list, remove it
            if number % i == 0 and number in primes_list:
                primes_list.remove(number)

    # Return the list of prime numbers
    return primes_list


print(prime_numbers())
