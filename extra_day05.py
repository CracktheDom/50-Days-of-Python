#!/usr/bin/env python3
# written by Dan on 11/25/22

from collections import Counter

"""You work for a school and your boss wants to know how many
female and male students are enrolled in the school. The school
has saved the students in a list. Your task is to write a code that
will count how many males and females are in the list. Here is a
list below:

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female',
 'male', 'Female', 'Male', 'Female', 'Male', 'female']

Your code should return a list of tuples. The list above should
return:

[(‘Male’,7), (‘female’,6)]"""


def gender_count(student_enrollment: list[str]) -> list[tuple[str, int]]:
    """
    Counts the number of students by gender in a list of student enrollments.

    Args:
        student_enrollment (list[str]): A list of student enrollments, where
            each enrollment is represented as a string indicating the student's
            gender.

    Returns:
        list[tuple[str, int]]: A list of tuples containing gender and the count
            of students for each gender. The list is sorted alphabetically by
            gender.
    """
    # Convert each student's gender to title case for consistency
    students_title_list: list[str] = [student.title() for student in student_enrollment]

    # Count the number of students for each gender
    numStudents: Counter = Counter(students_title_list)

    # Sort the gender counts alphabetically by gender
    return sorted(numStudents.items())


print(
    gender_count(
        [
            "MALE",
            "FEMALE",
            "FEMALE",
            "MALE",
            "FEMALE",
            "Male",
            "Female",
            "female",
            "male",
            "male",
            "male",
            "female",
            "male",
            "Female",
            "Male",
            "Female",
            "Male",
            "female",
        ]
    )
)
