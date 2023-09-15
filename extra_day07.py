#!/usr/bin/env python3

"""You are given a list of names, and you are asked to write a code
that returns all the names that start with ‘S’. Your code should
return a dictionary of all the names that start with S and how
many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]

Your code should return: {“Sasha”: 1, “Sera”: 2}"""


def s_names(names: list[str]) -> dict[str, int]:
    """
    Count names that start with 'S' in a list of names.

    This function takes a list of names as input and returns a dictionary
    where the keys are names that start with 'S', and the values are the
    count of occurrences of each name in the input list.

    Args:
        names (list[str]): A list of strings representing names.

    Returns:
        dict[str, int]: A dictionary containing names that start with 'S'
        as keys and their corresponding counts as values.
    """

    # Create a dictionary comprehension to count names starting with 'S'
    s_dict = {name: names.count(name) for name in names if name.startswith("S")}

    return s_dict


print(
    s_names(
        [
            "Samantha",
            "Joseph",
            "Nathan",
            "Sasha",
            "Kelly",
            "Muhammad",
            "Sara",
            "Sari",
            "Jabulani",
            "Sera",
            "Patel",
            "Sera",
        ]
    )
)
