#!/usr/bin/env python3

"""Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the
difference between the largest even number in the list and the
smallest odd number in the list. For example, if you pass
[1,2,4,6] as an argument the function should return 6 -1= 5."""


def odd_even(numbers: list[int]) -> int:
    """
    Calculate the difference between the maximum even number
    and the minimum odd number in a given list of numbers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The difference between the maximum even number and
             the minimum odd number. If there are no odd or even
             numbers in the list, return 0. If there are only even
             numbers, return the maximum even number. If there are
             only odd numbers, return the negative of the minimum odd
             number.

    Example:
        >>> odd_even([1, 2, 3, 4, 5])
        3
        >>> odd_even([2, 4, 6, 8])
        8
        >>> odd_even([1, 3, 5, 7])
        -1
        >>> odd_even([])
        0
    """
    odds = []
    evens = []

    # Separate the input numbers into odd and even lists
    for elem in numbers:
        if elem % 2 == 0:
            evens.append(elem)
        else:
            odds.append(elem)

    # Calculate the result based on the odd and even lists
    if len(odds) == 0 and len(evens) == 0:
        return 0
    elif len(odds) == 0:
        return max(evens)
    elif len(evens) == 0:
        return -(min(odds))

    # Calculate the difference between the max even and min odd
    return max(evens) - min(odds)


# Test cases
assert odd_even([num for num in range(5, 26, 5)]) == 15
assert odd_even([1, 2, 4, 6]) == 5
assert odd_even([1, 3, 5, 7]) == -1
assert odd_even([2, 4, 6, 8]) == 8
assert odd_even([]) == 0
assert odd_even([num for num in range(5, 25, 2)]) == -5
