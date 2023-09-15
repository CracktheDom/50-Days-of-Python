#!/usr/bin/env python3

import timeit


"""
Day 33: List Intersection
Write a function called inter_section that takes two lists and
finds the intersection (the elements that are present in both
lists). The function should return a tuple of intersections. Use
list comprehension in your solution. Use the lists below. Your
function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]"""


def inter_section(first_list: list[int], second_list: list[int]) -> tuple[int, ...]:
    """
    Compute the intersection of two lists and return it as a tuple.

    This function takes two lists of integers, calculates their intersection,
    and returns the result as a tuple. The intersection contains elements that
    are present in both input lists.

    Args:
        first_list (list[int]): The first list of integers.
        second_list (list[int]): The second list of integers.

    Returns:
        tuple[int, ...]: A tuple containing the elements present in both
        input lists.

    Example:
        >>> first_list = [1, 2, 3, 4]
        >>> second_list = [3, 4, 5, 6]
        >>> inter_section(first_list, second_list)
        (3, 4)
    """
    return tuple(set(first_list) & set(second_list))


"""
Extra Challenge: Set or list
You want to implement a code that will search for a number in
a range. You have a decision to make as to whether to store the
number in a set or a list. Your decision will be based on time.
You have to pick a data type that executes faster.
You have a range and you can either store it in a set or a list
depending on which one executes faster when you are searching
for a number in the range. See below:
a = range(10000000)
x = set(a)
y = list(a)
Let's say you are looking for a number 9999999 in the range
above. Search for this number in the list and the set. Your
challenge is to find which code executes faster. You will pick the
one that executes quicker, lists, or sets. Run the two searches
and time them.
"""


def set_or_list(range_input: int, num_to_find: int):
    """
    Compare the performance of sets and lists for checking if a number is in a
    range.

    Args:
        range_input (int): The upper limit of the range to be tested.
        num_to_find (int): The number to search for in the range.

    Returns:
        str: A message indicating which data structure performed faster.
    """
    # Create a range of numbers from 0 to range_input
    range_test = range(range_input)

    # Create a set and a list from the range of numbers
    range_of_nums_in_set = set(range_test)
    range_of_nums_in_list = list(range_test)

    # Measure the time it takes to check if num_to_find is in the set
    time_of_set = timeit.timeit(
        lambda: num_to_find in range_of_nums_in_set, number=100000
    )

    # Measure the time it takes to check if num_to_find is in the list
    time_of_list = timeit.timeit(
        lambda: num_to_find in range_of_nums_in_list, number=100000
    )

    # Compare execution times and return a message indicating the faster data
    structure
    return (
        f"Sets execute faster: sets completed in {time_of_set} seconds versus lists in {time_of_list} seconds"
        if time_of_set < time_of_list
        else f"Lists execute faster: lists completed in {time_of_list} seconds versus sets in {time_of_set} seconds."
    )


print(inter_section([20, 30, 60, 65, 75, 80, 85], [42, 30, 80, 65, 68, 88, 95]))
print(set_or_list(10_000_000, 9_999_999))
