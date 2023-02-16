#!/usr/bin/env python3

"""Write a function called count that takes one argument a string,
and returns a dictionary of how many times each element
appears in the string. For example, ‘hello’ should return:
{‘h’:1,’e’: 1,’l’:2, ‘o’:1}."""


def count(string_of_chars:str) -> dict:
	count_dict = {}
	for char in string_of_chars:
		if char in count_dict:
			count_dict[char] += 1
		else:
			count_dict[char] = 1
	return count_dict



print(count('superdupercagliess'))