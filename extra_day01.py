#!/usr/bin/env python3

"""Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value."""


def longest_value(dictLen: dict) -> str:
    max_value = max(dictLen.values(), key=len)
    return max_value


fruits = {'fruit': 'durian', 'colors': 'aquamarine',
          'flowers': 'chrysanthemums'}

print(longest_value(fruits))
