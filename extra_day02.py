#!/usr/bin/env python3

"""Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should return
the duplicates. If there are no duplicates, the function should
return "No duplicates". For example, the list of fruits below
should return apple as a duplicate and list of names should
return "no duplicates"."""


def check_duplicates(str_list: list):
    duplicates = []
    for elem in str_list:
        if str_list.count(elem) >= 2 and elem not in duplicates:
            duplicates.append(elem)

    return f"no duplicates" if len(duplicates) == 0 else duplicates


print(check_duplicates(['1', '2', '3', '4', '97']))
print(check_duplicates(['apples', 'banana', 'guava', 'banana',
      'lemon', 'lime', 'kiwi', 'dragonfruit', 'mango', 'lime']))
