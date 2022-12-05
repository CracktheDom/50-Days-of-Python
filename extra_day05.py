# written by Dan on 11/25/22
#!/usr/bin/env python3


"""You work for a school and your boss wants to know how many
female and male students are enrolled in the school. The school
has saved the students in a list. Your task is to write a code that
will count how many males and females are in the list. Here is a
list below:

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

Your code should return a list of tuples. The list above should
return:

[(‘Male’,7), (‘female’,6)]"""

def gender_count(student_enrollment:list) -> list:
	students_lower = [student.lower() for student in student_enrollment]
	return[("Males", students_lower.count('male')), ("Females", students_lower.count('female'))]

print(gender_count(["MALE", 'FEMALE', 'FEMALE', 'MALE', 'FEMALE', 'Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
))
