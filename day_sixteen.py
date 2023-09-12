#!/usr/bin/env python3

"""Write a function called sum_list with one parameter that takes
a nested list of integers as an argument and returns the sum of
the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
as an argument your function should return a sum of 33."""

from typing import List


def sum_list(nested_list: List[List[int]]) -> int:
    """
    Calculate the sum of all integers in a nested list.

    Args:
        nested_list (List[List[int]]): A nested list containing integer
        elements.

    Returns:
        int: The sum of all integers in the nested list.

    Raises:
        TypeError: If the input is not a list or if any element in the nested
        list is not an integer.

    Example:
        >>> sum_list([[1, 2, 3], [4, 5, 6]])
        21
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")

    total = 0
    for inner_list in nested_list:
        if not isinstance(inner_list, list):
            raise TypeError("Input must be a list of lists")
        for elem in inner_list:
            if not isinstance(elem, int):
                raise TypeError("All elements of the list must be integers")
            else:
                total += elem
    return total


"""Extra Challenge: Unpack A Nest
Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from
the nested list above – 34, 67, 78. Your output should be another
list:
[34, 67, 78]. The list output should not have duplicates."""

# Unclear instructions, not sure how elements from nested lists are selected
# to make subsequent list


def unpack(nested_list: List[List]) -> list:
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    flat = []
    for num_list in nested_list:
        flat += num_list
    return flat


assert sum_list([[1, 2, 5, 9, 4], [8, 6, 7, 4, 9]]) == 55
assert sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]) == 33
print(unpack([[1, 2, 5, 9, 4], [8, 6, 7, 4, 9]]))
