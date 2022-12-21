#! /usr/bin/env python3

"""Write a function called index_position. This function takes a
string as a parameter and returns the positions or indexes of all
lower letters in the string. For example, 'LovE' should return
[1,2]."""


def index_postion(string) -> list:
	return [pos for pos in range(len(string)) if string[pos].islower()]



"""Extra Challenge: Largest Number
Write a function called largest_number that takes a list of
integers and re-arrange the individual digits to create the largest
number possible. For example, if you pass the following as an
argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
number in this exact format: 9,877,632 as the largest number."""


def largest_number(int_list:list) -> list:
	str_digits_in_list = [digit for num in int_list for digit in str(num)]
	digit_string = sorted(str_digits_in_list, reverse=True)
	return f"{int(''.join(digit_string)):,}"



print(index_postion("LovE iS bLinD"))
print(largest_number([3, 67, 87, 9, 2, 911, 604385]))
