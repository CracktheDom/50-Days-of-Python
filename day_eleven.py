#! /usr/bin/env python3

"""Write a function called equal_strings. The function takes two
strings as arguments and compares them. If the strings are equal
(if they have the same characters and have equal length), it
should return True, if they are not, it should return False. For
example, 'love' and 'evol' should return True."""


def equal_strings(str_one: str, str_two: str) -> bool:
    """
    Compare two strings for equality based on their lengths and reverse order.

    This function takes two strings as input and returns True if they have the
    same length and are equal when one of them is reversed. Otherwise, it
    returns False.

    Args:
        str_one (str): The first input string.
        str_two (str): The second input string.

    Returns:
        bool: True if the strings are equal in length and when one is reversed,
        False otherwise.
    """
    return len(str_one) == len(str_two) and str_one == str_two[::-1]


assert equal_strings("baffle", "battle") is False
assert equal_strings("love", "evol") is True
