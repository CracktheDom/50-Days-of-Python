#!/usr/bin/env python3
# written by CrackTheDom on 11/24/22


"""Write a function called register_check that checks how many
students are in school. The function takes a dictionary as a
parameter. If the student is in school, the dictionary says ‘yes’. If
the student is not in school, the dictionary says ‘no’. Your
function should return the number of students in school. Use the
dictionary below. Your function should return 3."""

register: dict[str, str] = {
    "Michael": "yes",
    "John": "no",
    "Peter": "yes",
    "Mary": "yes",
}


def register_check(attendance_log: dict[str, str]) -> int:
    """
    Counts the number of children present in an attendance log.

    Parameters:
    attendance_log (dict[str, str]): A dictionary containing children's names
        as keys and their attendance status as values. "yes" indicates the
        child is present, and any other value is considered as absent.

    Returns:
    int: The number of children present in the attendance log.
    """
    # Initialize a counter for the number of children present
    number_of_children_present: int = 0

    # Iterate through the keys (names) in the attendance log
    for name in attendance_log.keys():
        # Check if the attendance status is "yes" (indicating the child is present)
        if attendance_log[name] == "yes":
            # Increment the count of present children
            number_of_children_present += 1

    # Return the total number of children present
    return number_of_children_present


print(register_check(register))
