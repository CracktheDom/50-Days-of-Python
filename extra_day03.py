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


def lowercase_names(names: list[str]) -> tuple[str, ...]:
    """
    Filters a list of names and returns a sorted tuple of lowercase names.

    Args:
        names (list[str]): A list of strings representing names.

    Returns:
        tuple[str, ...]: A tuple containing lowercase names sorted in reverse
                         order.

    This function takes a list of names as input and filters out names that
    start with a lowercase letter. It then sorts the filtered names in reverse
    order and returns them as a tuple.
    """
    # Create a list of lowercase names by filtering names starting with
    # lowercase letters
    names_lower: list[str] = [name for name in names if name.islower()]

    # Sort the list of lowercase names in reverse order
    names_lower.sort(reverse=True)

    # Return the sorted lowercase names as a tuple
    return tuple(names_lower)


print(lowercase_names(["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]))
