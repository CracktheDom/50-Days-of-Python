#!/usr/bin/env python3

from collections import Counter


"""Write a function called count that takes one argument a string,
and returns a dictionary of how many times each element
appears in the string. For example, 'hello' should return:
{'h':1,'e': 1,'l':2, 'o':1}."""


def count(string_of_chars: str) -> dict[str, int]:
    """
    Count the occurrences of each character in a given string.

    Args:
        string_of_chars (str): The input string for character counting.

    Returns:
        dict[str, int]: A dictionary containing characters as keys and their
                        corresponding counts as values.

    Example:
        >>> count("superdupercagliess")
        {'s': 4, 'u': 2, 'p': 2, 'e': 3, 'r': 2, 'd': 1, 'c': 1, 'a': 1, 'g': 1, 'l': 1, 'i': 1}
    """
    return dict(Counter(string_of_chars))


# Example usage of the count function
print(count("superdupercagliess"))
