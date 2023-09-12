#!/usr/bin/env python3

"""Write a function called divide_or_square that takes one
argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by
5. For example, if you pass 10 as an argument, then your function
should return 3.16 as the square root."""


def divide_or_square(num: int) -> float:
    """
    This function takes an integer 'num' as input and performs one of two
    operations
    based on whether 'num' is divisible by 5 or not. It returns a float as a
    result.

    Args:
        num (int): An integer input.

    Returns:
        float: The result of the operation. If 'num' is divisible by 5, it
        calculates the square root of 'num' rounded to 2 decimal places.
        Otherwise, it calculates the remainder of 'num' when divided by 5.
    """
    if num % 5 == 0:
        return round(num**0.5, 2)
    return num % 5


assert divide_or_square(25) == 5
assert divide_or_square(36) == 1
assert divide_or_square(10) == 3.16
