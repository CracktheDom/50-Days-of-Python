#! /usr/bin/env python3

"""Write a function called equal_strings. The function takes two
strings as arguments and compares them. If the strings are equal
(if they have the same characters and have equal length), it
should return True, if they are not, it should return False. For
example, 'love' and 'evol' should return True."""


def equal_strings(str_one: str, str_two: str) -> bool:
    isEqual = bool
    if len(str_one) == len(str_two):
        for char in str_one:
            if char not in str_two:
                isEqual = False
                break
            elif char in str_two:
                isEqual = True
    else:  # strings are not the same length
        isEqual = False
    return isEqual


print(equal_strings('baffle', 'battle'))
