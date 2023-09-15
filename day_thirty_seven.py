#!/usr/bin/env python3

"""Create a function called count_the_vowels. The function
takes one argument, a string, and returns the number of vowels
in the string. For example, ‘hello’ should return 2 vowels. If a
vowel appears in a string more than once it should be counted
as one. For example, ‘saas’ should return 1 vowel. Your code
should count lowercase and uppercase vowels."""


def count_the_vowels(string_of_chars: str) -> str:
    """
    Count the vowels in a given string and return a formatted string with the
    list of vowels and the count.

    Args:
        string_of_chars (str): The input string in which you want to count the
                               vowels.

    Returns:
        str: A formatted string containing the list of vowels found in the
             input string and the total count of vowels.

    Example:
        >>> count_the_vowels("Hello, World!")
        "['o', 'e', 'o'], 3 vowels"
    """
    # Create a list of unique vowels found in the input string
    vowels_present: list[str] = [
        char for char in set(string_of_chars) if char in "aAeEiIoOuU"
    ]

    # Format the result string with the list of vowels and their count
    result_str = f"{vowels_present}, {len(vowels_present)} vowels"

    return result_str


print(count_the_vowels("A, e, I, O, U, u, and sometimes 'Y'"))
