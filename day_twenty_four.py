#!/usr/bin/env python3

"""Create a function called average_calories that calculates the
average calories intake of a user. The function should ask the user
to input their calories intake for any number of days and once they
hit 'done' it should calculate and return the average intake."""


def average_calories() -> int:
    """
    Calculate the average daily caloric intake based on user input.

    Returns:
        int: The average caloric intake.

    This function prompts the user to input their daily caloric intake until
    they enter 'done'.
    It then calculates the average of the provided values and returns it.
    If no valid numeric values are provided, the function returns 0.
    """

    total: list[float] = []
    print("Input your daily caloric intake.")
    print("When you are finished entering data, input 'done'.")
    calories: str = ""  # Initialize variable as a condition for while loop
    while calories != "done":
        calories = input("What was your caloric intake? ")
        if calories == "done":
            break
        elif calories.isnumeric():
            total.append(float(calories))
        elif not calories.isnumeric():
            print("Please enter numeric values.")

    return sum(total) / len(total) if len(total) > 0 else 0


"""Extra Challenge: Create a Nested List
Write a function called nested_lists that takes any number of
lists and creates a 2-dimensional nested list of lists. For example,
if you pass the following lists as arguments: [1, 2, 3, 5], [1, 2, 3,
4], [1, 3, 4, 5].
Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]"""


def nested_lists(*args: list[int]) -> list[list[int]]:
    return [arg for arg in args]


assert nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]) == [
    [1, 2, 3, 5],
    [1, 2, 3, 4],
    [1, 3, 4, 5],
]

print(average_calories())
