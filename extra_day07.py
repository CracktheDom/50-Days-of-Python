#!/usr/bin/env python3

"""You are given a list of names, and you are asked to write a code
that returns all the names that start with ‘S’. Your code should
return a dictionary of all the names that start with S and how
many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]

Your code should return: {“Sasha”: 1, “Sera”: 2}"""


def s_names(names: list) -> dict:
    s_dict = {}
    for name in names:
        if name[0] == 'S':
            if name not in s_dict:
                s_dict[name] = 1
            else:
                s_dict[name] += 1
    return s_dict


print(s_names(
    ['Samantha', "Joseph", "Nathan", "Sasha", "Kelly", "Muhammad",
     'Sara', 'Sari', "Jabulani", "Sera", "Patel", "Sera"]
)
)
