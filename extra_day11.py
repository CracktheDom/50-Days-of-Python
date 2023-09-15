#!/usr/bin/env python3

"""Write a function called swap_values. This function takes a list
of numbers and swaps the first element with the last element.
For example, if you pass [2, 4,67, 7] as a parameter, your
function should return
[7, 4, 67, 2]."""


def swap_values(num_list: list[int]) -> list[int]:
    """
    Swaps the first and last elements of a list of integers.

    Args:
        num_list (list[int]): A list of integers.

    Returns:
        list[int]: A list with the first and last elements swapped.

    Example:
        >>> swap_values([1, 2, 3, 4, 5])
        [5, 2, 3, 4, 1]
    """
    # Swap the first and last elements using tuple unpacking
    num_list[0], num_list[-1] = num_list[-1], num_list[0]
    return num_list


assert swap_values([2, 4, 67, 7]) == [7, 4, 67, 2]
