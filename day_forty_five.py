#! /usr/bin/python3

import string


"""Write a function called analyse_string that returns the number of
special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
and, total characters (all letters and special characters minus
whitespaces) in a string. Return everything in a dictionary format:
{"special character": "number", "words": "number", "total
characters": "number"}
Use the string below as an argument:"""

string_to_be_analyzed = """Python has a string format operator %. This functions
analogously to printf format strings in C, e.g. "spam=%s
eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2"."""


def analyse_string(string_to_be_analyzed: str) -> dict:
    """
    Analyzes a given input string and returns a dictionary containing
    information about it.

    Args:
        string_to_be_analyzed (str): The input string to be analyzed.

    Returns:
        dict: A dictionary containing the following information:
            - "special character": The count of special characters in the input
             string.
            - "words": The number of words in the input string.
            - "total characters": The total number of characters in the input
            string (excluding whitespace).
    """
    word_list = string_to_be_analyzed.split()
    num_of_words = len(word_list)
    num_special_chars = 0
    SPECIAL_CHARS = set("#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    total_chars = 0

    for char in string_to_be_analyzed:
        if char in SPECIAL_CHARS:
            num_special_chars += 1
        if char not in string.whitespace:
            total_chars += 1

    return {
        "special character": num_special_chars,
        "words": num_of_words,
        "total characters": total_chars,
    }


print(analyse_string(string_to_be_analyzed))
