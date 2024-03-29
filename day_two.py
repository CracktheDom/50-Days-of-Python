#!/usr/bin/env python3

"""Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example ['1', '3', '5'] should be converted to [1, 3, 5] and
summed to 9."""


# For collections on Python 3.9+,
# the type of the collection item is in brackets
def convert_add(list_str: list[str]) -> int:
    return sum(map(int, list_str))


print(convert_add(["2", "5", "7", "1", "8"]))
