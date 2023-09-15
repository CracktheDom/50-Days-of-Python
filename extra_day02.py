#!/usr/bin/env python3

"""Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should return
the duplicates. If there are no duplicates, the function should
return "No duplicates". For example, the list of fruits below
should return apple as a duplicate and list of names should
return "no duplicates"."""


def check_duplicates(str_list: list[str]) -> list[str] | str:
    """
    Check for duplicates in a list of strings.

    This function takes a list of strings as input and checks for duplicate
    strings in the list.

    Args:
        str_list (list[str]): A list of strings to check for duplicates.

    Returns:
        Union[list[str], str]:
            - If duplicates are found, it returns a list of the duplicate
              strings.
            - If no duplicates are found, it returns the string "no duplicates."

    Example:
        >>> check_duplicates(["apple", "banana", "apple", "orange"])
        ['apple']
        >>> check_duplicates(["apple", "banana", "cherry"])
        'no duplicates'
    """

    duplicates = []  # Initialize an empty list

    # Iterate through unique items in the list
    for item in set(str_list):
        # Count the occurrences of the item in the original list
        if str_list.count(item) >= 2:
            # If there are at least two occurrences, it's a duplicate
            duplicates.append(item)

    # Return either the list of duplicates or "no duplicates"
    return list(duplicates) if duplicates else "no duplicates"


print(check_duplicates(["1", "2", "3", "4", "97", "2", "3"]))
print(check_duplicates(["1", "2", "3", "4", "97"]))
print(
    check_duplicates(
        [
            "apples",
            "banana",
            "guava",
            "banana",
            "lemon",
            "lime",
            "kiwi",
            "apples",
            "dragonfruit",
            "mango",
            "kiwi",
            "lime",
            "kiwi",
        ]
    )
)
