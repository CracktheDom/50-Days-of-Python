#!/usr/bin/env python3

"""Write a function called word_index that takes one argument,
a list of strings and returns the index of the longest word in the
list. If there is no longest word (if all the strings are of the same
length), the function should return zero (0). For example, the list
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
And this list below, should return zero (0)
words2 = ["Love", "Hate"]"""

def word_index(words:list) -> int:
	words_length:list = [len(word) for word in words]
	max_word_length:int = max(words_length)
	if words_length.count(max_word_length) >= 2:
		return 0
	elif words_length.count(max_word_length) == 1:
		return words_length.index(max_word_length)

print(word_index(['Hate', 'remorse', 'venegenace', 'perpendicular']))