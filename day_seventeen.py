#!/usr/bin/env python3

import random


"""Write a function called user_name, that creates a username
for the user. The function should ask a user to input their name.
The function should then reverse the name and attach a
randomly issued number between 0 – 9 at the end of the name.
The function should return the username."""

def user_name() -> str:
	name = input("What is your name? ")
	return f"{name[::-1]}{random.randint(10)}"



"""Extra Challenge: Sort by Length
names = [ "Peter", "Jon", "Andrew"]
Write a function called sort_length that takes a list of strings
as an argument, and sorts the strings in ascending order
according to their length. For example, the list above should
return:
['Jon', 'Peter', 'Andrew']
Do not use the built-in sort functions"""

def sort_length(str_list:list) -> list:
	return sorted(str_list, key=len, reverse=True)


# print(user_name())
print(sort_length(['Jon', "Emmanuel", 'Peter', 'Andrew', 'Timothy', "Abraham", "Zach"]))