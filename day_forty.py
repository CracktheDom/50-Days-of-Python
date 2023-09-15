#!/usr/bin/env python3

"""Write a function called translate that takes the following
words and translates them into pig Latin.
a = 'i love python'
Here are the rules:
1. If a word starts with a vowel (a,e, i, o, u) add 'yay' at the
end. For example, 'eat' will become 'eatyay'
2. If a word starts with anything other than a vowel, move
the first letter to the end and add 'ay' to the end. For
example, 'day' will become 'ayday'.
Your code should return:
iyay ovelay ythonpa"""


from collections import deque


def translate(stringInEnglish: str) -> str:
    """
    Translates a given English string into Pig Latin.

    Args:
        stringInEnglish (str): The input string in English.

    Returns:
        str: The translated string in Pig Latin.

    Example:
        >>> translate("The arc of a life well-lived")
        "hetay arcyay ofyay ayay ifelay ell-livedway"
    """

    # Split the input English string into words and convert to lowercase.
    wordList = stringInEnglish.lower().split(" ")
    pig_latin_word_list = []

    # Iterate through each word in the input.
    for word in wordList:
        # Check if the word starts with a vowel.
        if word.startswith(("a", "e", "i", "o", "u")):
            # If it starts with a vowel, add "yay" to the end.
            word += "yay"
            pig_latin_word_list.append(word)
        else:
            # If it doesn't start with a vowel, convert to Pig Latin.
            wordDeque = deque(word)
            wordDeque.rotate(-1)  # moves first letter to the end of word
            wordDeque.append("ay")
            pig_latin_word_list.append("".join(wordDeque))

    # Join the Pig Latin words and return the translated string.
    return " ".join(pig_latin_word_list)


# Test cases
assert (
    translate("The arc of a life well-lived")
    == "hetay arcyay ofyay ayay ifelay ell-livedway"
)
assert translate("I love python") == "iyay ovelay ythonpay"
