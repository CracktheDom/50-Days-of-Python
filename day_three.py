# written by CrackTheDom on 11/24/22
#!/usr/bin/env python3

"""Write a function called register_check that checks how many
students are in school. The function takes a dictionary as a
parameter. If the student is in school, the dictionary says ‘yes’. If
the student is not in school, the dictionary says ‘no’. Your
function should return the number of students in school. Use the
dictionary below. Your function should return 3."""

register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}

def register_check(attendance_log:dict) -> int:
	number_of_children_present = 0
	for name in attendance_log.keys():
		if attendance_log[name] == 'yes':
			number_of_children_present += 1
	return number_of_children_present


print(register_check(register))