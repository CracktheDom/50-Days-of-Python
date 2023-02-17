#!/usr/bin/env python3

"""Create a function called biggest_odd that takes a string of
numbers and returns the biggest odd number in the list. For
example, if you pass ‘23569’ as an argument, your function
should return 9. Use list comprehension."""


def biggest_odd(string: str) -> int:
    num_list = list(map(int, string))
    return max([odd for odd in num_list if odd % 2 == 1])


print(biggest_odd('324856787'))
