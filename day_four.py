#!/usr/bin/env python3

"""Write a function called only_floats, which takes two
parameters a and b, and returns 2 if both arguments are floats,
returns 1 if only one argument is a float, and returns 0 if neither
argument is a float. If you pass (12.1, 23) as an argument, your
function should return a 1."""

def only_floats(a, b) -> int:
	if type(a) is float and type(b) is float:
		return 2
	elif type(a) is float or type(b) is float:
		return 1
	elif type(a) is not float and type(b) is not float:
		return 0

print(only_floats(3.4, 1))
print(only_floats(3, 0.0))
print(only_floats(3, 6))
print(only_floats(3.4, 6.1))