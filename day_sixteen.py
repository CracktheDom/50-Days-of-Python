#!/usr/bin/env python3

"""Write a function called sum_list with one parameter that takes
a nested list of integers as an argument and returns the sum of
the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
as an argument your function should return a sum of 33."""


def sum_list(nested: list) -> int:
    return sum(unpack(nested))


"""Extra Challenge: Unpack A Nest
Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from
the nested list above – 34, 67, 78. Your output should be another
list:
[34, 67, 78]. The list output should not have duplicates."""


def unpack(nested: list) -> list:
    flat = []
    for num_list in nested:
        flat += num_list
    return flat


print(sum_list([[1, 2, 5, 9, 4], [8, 6, 7, 4, 9]]))
print(unpack([[1, 2, 5, 9, 4], [8, 6, 7, 4, 9]]))
