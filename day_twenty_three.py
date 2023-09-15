#!/usr/bin/env python3

"""Create a simple calculator. The calculator should be able to perform
basic math operations, add, subtract, divide and multiply. The
calculator should take input from users. The calculator should be
able to handle ZeroDivisionError, NameError, and
ValueError."""


def calculator():
    # TODO:  all of it
    pass


"""Extra Challenge: Multiply Words

Write a function called multiply_words that takes a string as an
argument and multiplies the length of each word in the string by
the length of other words in the string. For example, the string
above should return 240 - love (4) live (4) and (3) laugh (5).
However, your function should only multiply words will all
lowercase letters. If a word has one upper case letter, it should be
ignored. For example, the following string:
s = "Hate war love Peace" should return 12 – war (3) love (4).
Hate and Peace will be ignored because they have at least one
uppercase letter."""


def multiply_words(string: str) -> int:
    total: int = 1
    lowercase_words: list[str] = [
        word
        for word in string.split(" ")
        if not any(letter.isupper() for letter in word)
    ]
    for lower in lowercase_words:
        total *= len(lower)
    return total


s = "love live and laugh"
t = "Hate war love Peace"

assert multiply_words(s) == 240
assert multiply_words(t) == 12
