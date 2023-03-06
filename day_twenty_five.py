#!/usr/bin/env python3

"""Create a function called all_the_same that takes one
argument, a string, a list, or a tuple and checks if all the
elements are the same. If the elements are the same, the function
should return True. If not, it should return False. For example,
['Mary', 'Mary', 'Mary'] should return True."""


def all_the_same(str_list_or_tuple) -> bool:
    # TODO: iterate thru list, str, tuple & finish
    pass


"""Extra Challenge: Reverse a String
str1 = "the love is real"
Write a function called read_backwards that takes a string as
an argument and reverses it. For example, the string above
should return: "real is love the"""


def read_backwards(string) -> str:
    return ' '.join(string.split(' ')[::-1])


print(read_backwards("The arc of a life well lived."))
