#!/usr/bin/env python3

"""Write a function called repeated_name that finds the most
repeated name in the following list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]"""


def repeated_name():
	# TODO: display key with highest value
	names = ["John", "John", "John", "Peter", "John", "Peter", "Jones", "Peter"]
	nameDict = {k:names.count(k) for k in names}
	return sorted(nameDict.items())


"""Extra Challenge: Sort by Last Name
You work for a local school in your area. The school has a list of
names of students saved in a list. The school has asked you to write a program 
that takes a list of names and sorts them
alphabetically. The names should be sorted by last names. Here
is a list of names:
['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris
Brown', 'Tom Cruise']
Your code should not just sort them alphabetically, but it should
also switch the names (the last name must be the first). Here is
how your code output should look:
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie',
'Knowles Beyonce']
Write a function called sorted_names"""


def sort_names(names:list):
	return sorted([f'{name[name.index(" ") + 1:]} {name[:name.index(" ")]}' for name in names])


print(repeated_name())
print(sort_names(['Richard Greer','Judy Greer','Pam Grier', 'Janelle Monae', 'Emily Blunt', 'Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown','Tom Cruise']))
