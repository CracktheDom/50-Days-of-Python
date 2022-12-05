#!/usr/bin/env python3

"""Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example ['1', '3', '5'] should be converted to [1, 3, 5] and
summed to 9."""

def convert_add(list_str:list) -> int:
	list_num = [int(s) for s in list_str]
	total = 0
	for num in list_num:
		total += num 
	return total

print(convert_add(['2','5','7','1','8']))
