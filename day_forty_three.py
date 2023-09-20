#! /usr/bin/env python3


"""Write a function called student_marks that records marks
achieved by students in a test. The function should ask the user
to input the name of the student and then ask the user to input
the marks achieved by the student. The information should be
stored in a dictionary. The name is the key and the marks is the
value. When the user enters done, the function should return a
dictionary of names and values entered."""


def student_marks() -> dict[str, float]:
    is_grading_finished = False
    grade_book = {}
    while not is_grading_finished:
        student_name = input("What is the student's name?  ")
        print()
        marks = input(f"Enter {student_name}'s marks:  ")
        print()
        grade_book[student_name] = marks
        are_you_done = input(
            "Enter 'done' if you are finished entering student marks  "
        )
        if are_you_done == "done":
            is_grading_finished = True

    return grade_book


print(student_marks())
