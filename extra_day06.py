#!/usr/bin/env python3

"""Write a function called zeroed code that takes a list of numbers
as an argument. The code should zero (0) the first and the last
number in the list. For example, if the input is [2, 5, 7, 8, 9],
your code should return [0, 5, 7, 8, 0]."""


def zeroed(nums_list: list[int]) -> list[int]:
    """
    Zeroes out the first and last elements of a list of integers.

    Args:
        nums_list (list[int]): A list of integers.

    Returns:
        list[int]: The input list with its first and last elements set to 0.
    """
    # Set the first element to 0
    nums_list[0] = 0

    # Set the last element to 0
    nums_list[-1] = 0

    return num


print(zeroed([4, 5, 6, 8, 99, 7, 43, 41]))
