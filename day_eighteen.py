#!/usr/bin/env python3

from statistics import mean

"""Write a function called any_number that can receive any
number of arguments (integers and floats) and return the
average of those integers. If you pass 12, 90, 12, 34 as
arguments your function should return 37.0 as average. If you
pass 12, 90 your function should return 51.0 as average."""


def any_number(*args) -> float:
    return round(mean(list(args)), 2)


"""Extra Challenge: Add and Reverse
Write a function called add_reverse. This function takes two
lists as argument and adds each corresponding number, and
reverses the outcome. For example, if you pass [10, 12, 34]
and [12, 56, 78]. Your code should return [112, 22, 68]. If the
two lists are not of equal lengths, the code should return a
message that "the lists are not of equal lengths"."""


def add_reverse(list1: list[int], list2: list[int]) -> list[int] | str:
    """
    Add elements from two lists element-wise and return the result in reverse
    order.

    Args:
        list1 (list[int]): The first input list of integers.
        list2 (list[int]): The second input list of integers.

    Returns:
        list[int] | str: A list of integers containing the sum of corresponding
                         elements from list1 and list2, in reverse order, or a
                         string indicating unequal list lengths.

    Raises:
        None

    Example:
        >>> add_reverse([1, 2, 3], [4, 5, 6])
        [9, 7, 5]
        >>> add_reverse([1, 2, 3], [4, 5, 6, 7])
        "the lists are not of equal length"
    """
    if len(list1) != len(list2):
        return "the lists are not of equal length"

    # zip iterates through both lists, then adds the corresponding elements
    # together, the sums are the elements of the new list
    return [sum(i) for i in zip(list1, list2)][::-1]


assert any_number(12, 90) == 51
assert any_number(12, 90, 12, 34) == 37
assert any_number(1, 3, 6, 8, 4, 7, 5, 9, 3, 7) == 5.3
assert any_number(1, 3, 6, 7, 5, 4, 101.7) == 18.24
assert add_reverse([10, 12, 34], [12, 56, 78]) == [112, 68, 22]
assert (
    add_reverse([10, 12, 34], [12, 56, 78, 63]) == "the lists are not of equal length"
)
