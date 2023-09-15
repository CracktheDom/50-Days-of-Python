#!/usr/bin/env python3

"""Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value."""


def longest_value(dictLen: dict[str, str]) -> str:
    """
    Find and return the longest value in a dictionary of strings.

    Args:
        dictLen (dict[str, str]): A dictionary containing string values.

    Returns:
        str: The longest string value from the dictionary.

    Raises:
        ValueError: If the input dictionary is empty.

    Example:
        >>> dictionary = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
        >>> longest_value(dictionary)
        'banana'
    """
    # Find the maximum value in the dictionary based on string length
    max_value: str = max(dictLen.values(), key=len)
    return max_value


fruits = {"fruit": "durian", "colors": "aquamarine", "flowers": "chrysanthemums"}

print(longest_value(fruits))
