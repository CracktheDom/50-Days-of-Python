#!/usr/bin/env python3

"""Write a function called word_index that takes one argument,
a list of strings and returns the index of the longest word in the
list. If there is no longest word (if all the strings are of the same
length), the function should return zero (0). For example, the list
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
And this list below, should return zero (0)
words2 = ["Love", "Hate"]"""


def word_index(words: list[str]) -> int:
    """
    Find the index of the longest word in a list of words, but return 0 if
    there are multiple words with the same longest length.

    Args:
        words (list[str]): A list of words to process.

    Returns:
        int: The index of the longest word in the list, or 0 if there are
             multiple words with the same longest length.
    """
    # Find the longest word in the list based on its length
    longest_word_length: str = max(words, key=len)

    # Create a list of word lengths for all words in the input list
    word_length_list: list[int] = [len(word) for word in words]

    # Check if there are multiple words with the same longest length
    if word_length_list.count(len(longest_word_length)) >= 2:
        return 0

    # Return the index of the longest word in the original list
    return words.index(longest_word_length)


print(word_index(["Hate", "remorse", "venegenace", "perpendicular"]))
print(word_index(["Love", "Hate"]))
