#!/usr/bin/env python3

from collections import Counter


"""Write a function called count that takes one argument a string,
and returns a dictionary of how many times each element
appears in the string. For example, 'hello' should return:
{'h':1,'e': 1,'l':2, 'o':1}."""


def count(string_of_chars: str) -> dict:
    return dict(Counter(string_of_chars))


print(count('superdupercagliess'))
