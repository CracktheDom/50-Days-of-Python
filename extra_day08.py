#!/usr/bin/env python3

"""Write a function called prime_numbers. This function asks a
user to enter a number (integer) as an argument and returns a
list of all the prime numbers within its range. For example, if user
enters 10, your code should return [2, 3, 5, 7] as prime numbers."""


def prime_numbers() -> list:
    numbers = int(input("Enter a number: "))
    num_list = [number for number in range(2, numbers + 1) if number % 2 != 0]
    num_list.insert(0, 2)
    primes_list = num_list.copy()

    for number in num_list:
        for i in range(2, (round(number ** 0.5) + 1)):
            if number % i == 0 and number in primes_list:
                primes_list.remove(number)

    return primes_list


print(prime_numbers())
