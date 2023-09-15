#! /usr/bin/env python3

"""Write a function called index_position. This function takes a
string as a parameter and returns the positions or indexes of all
lower letters in the string. For example, 'LovE' should return
[1,2]."""


def index_postion(string: str) -> list[int]:
    return [index for index in range(len(string)) if string[index].islower()]


"""Extra Challenge: Largest Number
Write a function called largest_number that takes a list of
integers and re-arrange the individual digits to create the largest
number possible. For example, if you pass the following as an
argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
number in this exact format: 9,877,632 as the largest number."""


def largest_number(int_list: list[int]) -> str:
    str_digits_list: list[str] = [digit for num in int_list for digit in str(num)]
    sorted_digit_list: list[str] = sorted(str_digits_list, reverse=True)
    return f"{int(''.join(sorted_digit_list)):,}"


print(index_postion("LovE iS bLinD"))
print(largest_number([3, 67, 87, 9, 2, 911, 604385]))
