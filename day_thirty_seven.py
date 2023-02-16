#!/usr/bin/env python3

"""Create a function called count_the_vowels. The function
takes one argument, a string, and returns the number of vowels
in the string. For example, ‘hello’ should return 2 vowels. If a
vowel appears in a string more than once it should be counted
as one. For example, ‘saas’ should return 1 vowel. Your code
should count lowercase and uppercase vowels."""


def count_the_vowels(string_of_chars: str) -> str:
    vowels_present = [
        char for char in set(string_of_chars) if char in 'aAeEiIoOuU'
    ]
    return f"{vowels_present}, {len(vowels_present)} vowels"


print(count_the_vowels("A, e, I, O, U, u, and sometimes 'Y'"))
