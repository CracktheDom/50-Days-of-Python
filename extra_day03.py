#!/usr/bin/env python3

# written by CrackThaDom 11/24/22


"""names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

You are given a list of names above. This list is made up of names
of lowercase and uppercase letters. Your task is to write a code
that will return a tuple of all the names in the list that have only
lowercase letters. Your tuple should have names sorted
alphabetically in descending order. Using the list above, your
code should return:

('kerry', 'dickson', 'carol', 'adam')"""


def lowercase_names(names: list) -> tuple:
    names_lower = [name for name in names if name[0].islower()]
    names_lower.sort(reverse=True)
    return tuple(names_lower)


print(lowercase_names(
    ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]))
