#! /usr/bin/env python3

"""Write a function called equal_strings. The function takes two
strings as arguments and compares them. If the strings are equal
(if they have the same characters and have equal length), it
should return True, if they are not, it should return False. For
example, ‘love’ and ‘evol’ should return True."""

# TODO: Finish writing function
 
def equal_strings(str_one:str, str_two:str) -> bool:
	if len(str_one) == len(str_two):
		for char in str_one:
			if char not in str_two:
				# return str_two == str_one
				break
			elif char in str_two:
				pass
	return str_two == str_one