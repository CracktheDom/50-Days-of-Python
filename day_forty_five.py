#! /usr/bin/python3

import string


"""Write a function called analyse_string that returns the number of
special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
and, total characters (all letters and special characters minus
whitespaces) in a string. Return everything in a dictionary format:
{"special character": "number", "words": "number", "total
characters": "number"}
Use the string below as an argument:"""


def analyse_string(string_to_be_analyzed: str) -> dict[str, str]:
    """
    Analyze a given string and return a dictionary containing information about
    it.

    Args:
        string_to_be_analyzed (str): The input string to be analyzed.

    Returns:
        dict[str, str]: A dictionary containing the following information:
            - 'words': The number of words in the input string.
            - 'special character': The number of special characters in the
            input string.
            - 'total characters': The total number of characters in the input
            string.
    """
    # Split the input string into a list of words
    word_list: list[str] = string_to_be_analyzed.split()

    # Calculate the number of words in the string
    num_of_words: int = len(word_list)

    # Initialize variables for counting special characters and total characters
    num_special_chars = 0
    SPECIAL_CHARS = set("#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    total_chars = 0

    # Iterate through each character in the input string
    for char in string_to_be_analyzed:
        # Check if the character is a special character
        if char in SPECIAL_CHARS:
            num_special_chars += 1

        # Check if the character is not a whitespace character
        if char not in string.whitespace:
            total_chars += 1

    # Return the analysis results as a dictionary
    return {
        "special character": str(num_special_chars),
        "words": str(num_of_words),
        "total characters": str(total_chars),
    }


string_to_be_analyzed = """Python has a string format operator %. This functions
analogously to printf format strings in C, e.g. "spam=%s
eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2"."""

print(analyse_string(string_to_be_analyzed))
