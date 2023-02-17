#!/usr/bin/env python3

"""Write two functions. The first function is called count_words
which takes a string of words and counts how many words are in
the string."""


def count_words(string_of_words: str) -> int:
    return len(string_of_words.split(" "))


"""The second function called count_elements takes a string of
words and counts how many elements are in the string. Do not
count the whitespaces. The first function will return the number
of words in a string and the second one will return the number
of elements (less whitespace). If you pass ‘I love learning’,
the count_words function should return 3 words and
count_elements should return 13 elements."""


def count_elements(stringOfWords: str) -> int:
    elements = 0
    for word in stringOfWords.split(" "):
        elements += len(word)
    return elements


print(count_words("the arc of a life well lived"))
print(count_elements("the arc of a life well lived"))
