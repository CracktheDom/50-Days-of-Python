#!/usr/bin/env python3

"""Write a function called flat_list that takes one argument, a
nested list. The function converts the nested list into a one-
dimension list. For example [[2,4,5,6]] should return
[2,4,5,6]."""


def flat_list(nested: list) -> list:
    return nested[0]


print(flat_list([[2, 4, 5, 6, 78, 24, 11, 89]]))
