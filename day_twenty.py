#!/usr/bin/env python3

"""Write a function called capitalize. This function takes a string
as an argument and capitalizes the first letter of each word. For
example, ‘i like learning’ becomes ‘I Like Learning’."""


def capitalize_each_word(string: str) -> str:
    return string.title()


"""Extra Challenge: Reversed List
str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'
You are given a string of words. Some of the words in the string
contain uppercase letters. Write a code that will return all the
words that have an uppercase letter. Your code should return a
list of the words. Each word in the list should be reversed. Here
is how your output should look:
['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']"""


def reverse_lowercase(string: str) -> list[str]:
    """
    Reverse words in a string if they are all in lowercase.

    Args:
        string (str): The input string containing words.

    Returns:
        list[str]: A list of reversed words that are all in lowercase.
    """
    # Split the input string into words using space as a delimiter,
    # and reverse each word if it contains a uppercase letter.
    reversed_words = [
        word[::-1] for word in string.split(" ") if any(ch.isupper() for ch in word)
    ]

    return reversed_words


str1 = "leArning is hard, bUt if You appLy youRself you can achieVe success"

assert reverse_lowercase(str1) == [
    "gninrAel",
    "tUb",
    "uoY",
    "yLppa",
    "flesRuoy",
    "eVeihca",
]
print(capitalize_each_word(str1))
