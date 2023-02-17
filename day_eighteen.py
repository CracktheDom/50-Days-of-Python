#!/usr/bin/env python3

from statistics import mean

"""Write a function called any_number that can receive any
number of arguments (integers and floats) and return the
average of those integers. If you pass 12, 90, 12, 34 as
arguments your function should return 37.0 as average. If you
pass 12, 90 your function should return 51.0 as average."""


def any_number(*args) -> float:
    return f"{mean(list(args)):.1f}"


"""Extra Challenge: Add and Reverse
Write a function called add_reverse. This function takes two
lists as argument and adds each corresponding number, and
reverses the outcome. For example, if you pass [10, 12, 34]
and [12, 56, 78]. Your code should return [112, 22, 68]. If the
two lists are not of equal lengths, the code should return a
message that "the lists are not of equal lengths"."""


def add_reverse(list1: list, list2: list) -> list:
    if len(list1) != len(list2):
        return f"the lists are not of equal length"
    else:
        # zip iterates thru both lists & adds the corresponding elements
        # together, the totals are the elements of new list
        return [sum(i) for i in zip(list1, list2)][::-1]


print(any_number(12, 90))
print(any_number(1, 3, 6, 8, 4, 7, 5, 9, 3, 7))
print(any_number(1, 3, 6, 7, 5, 4, 101.7))
print(add_reverse([10, 12, 34], [12, 56, 78]))
