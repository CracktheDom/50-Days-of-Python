#!/usr/bin/env python3

"""Your new company has a list of figures saved in a list. The issue
is that these numbers have no separator. The numbers are
saved in the following format:
[1000000, 2356989, 2354672, 9878098].
You have been asked to write a code that will convert each of the
numbers in the list into a string. Your code should then add a
comma on each number as a thousand separator for
readability. When you run your code on the above list, your
output should be:
[ '1,000,000', '2,356,989', '2,354,672', '9,878,098']"""


def thousand_separator(num_list: list[int]) -> list[str]:
    """
    Format a list of integers with thousand separators and return a list of
    formatted strings.

    Args:
        num_list (list[int]): A list of integers to be formatted.

    Returns:
        list[str]: A list of strings where each integer from `num_list` is
        formatted with thousand separators.

    Example:
        >>> thousand_separator([1000, 20000, 300000])
        ['1,000', '20,000', '300,000']

    This function takes a list of integers, applies thousand separators to each
    integer, and returns a new list containing the formatted strings.
    """
    return list(map(lambda num: f"{num:,}", num_list))


print(thousand_separator([1000000, 2356989, 2354672, 9878098]))
