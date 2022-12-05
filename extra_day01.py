#!/usr/bin/env python3

"""Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value."""

# TODO: Need to finish returning longest value, not length of value

def longest_value(dictLen:dict) -> str:
	max_value_length_list = [len(value) for value in dictLen.values()]
	max_value = max(max_value_length_list)
	max_value_index = max_value_length_list.index(max_value)
	return max_value


fruits = {'fruit': 'durian', 'colors':'aquamarine', 'flowers': 'chrysanthemums'}

print(longest_value(fruits))