#!/usr/bin/env python3

"""Write a function called repeated_name that finds the most
repeated name in the following list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]"""

from collections import Counter


def repeated_name():
    names = ["John", "John", "John", "Peter", "John", "Peter", "Jones", "Peter"]
    nameDict = Counter(names)
    return nameDict.most_common(1)[0][0]


"""Extra Challenge: Sort by Last Name
You work for a local school in your area. The school has a list of
names of students saved in a list. The school has asked you to write a program
that takes a list of names and sorts them
alphabetically. The names should be sorted by last names. Here
is a list of names:
['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris
Brown', 'Tom Cruise']
Your code should not just sort them alphabetically, but it should
also switch the names (the last name must be the first). Here is
how your code output should look:
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie',
'Knowles Beyonce']
Write a function called sorted_names"""

from typing import List


def sort_names(fullnames: List[str]) -> List[str]:
    """
    Sorts a list of full names based on the first letter of the second word and
    returns a new list with the first and second words of each name switched.

    Args:
        fullnames (List[str]): A list of full names (each name as a string).

    Returns:
        List[str]: A new list of full names with the first and second words
        switched, sorted based on the first letter of the second word.
    """

    # Sort list by the first letter of the second word
    sorted_list = sorted(fullnames, key=lambda x: x.split()[1][0])

    # Switch the first word and second word of each element
    switched_list = [" ".join(name.split()[::-1]) for name in sorted_list]

    return switched_list

    # return sorted(
    #     [f'{name[name.index(" ") + 1:]} {name[:name.index(" ")]}' for name in fullnames]
    # )


print(repeated_name())
print(
    sort_names(
        [
            "Richard Greer",
            "Judy Greer",
            "Pam Grier",
            "Janelle Monae",
            "Emily Blunt",
            "Beyonce Knowles",
            "Alicia Keys",
            "Katie Perry",
            "Chris Brown",
            "Tom Cruise",
        ]
    )
)
