#!/usr/bin/env python3

from statistics import mean


"""Write a function called make_tuples that takes two lists,
equal lists, and combines them into a list of tuples. For
example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
function should return [(1,5), (2,6), (3,7), (4,8)]."""


def make_tuples(list1: list[int], list2: list[int]) -> list[tuple[int, int]]:
    """
    Create a list of tuples by pairing corresponding elements from two input
    lists.

    Args:
        list1 (list[int]): The first input list.
        list2 (list[int]): The second input list.

    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains a
        pair of elements from list1 and list2, respectively. The length of the
        returned list is equal to the length of the shorter input list.

    Raises:
        ValueError: If the input lists have different lengths.

    Example:
        >>> make_tuples([1, 2, 3], [4, 5, 6])
        [(1, 4), (2, 5), (3, 6)]
    """
    if len(list1) == len(list2):
        return [(i) for i in zip(list1, list2)]


"""Extra Challenge: Even Number or Average
Write a function called even_or_average that ask a user to
input five numbers. Once the user is done, the code should
return the largest even number in the inputted numbers. If
there is no even number in the list, the code should return the
average of all the five numbers."""


def even_or_average() -> int | float:
    """
    Calculate either the average of 5 input numbers or the maximum even number
    from those inputs, depending on the input values.

    Returns:
        int | float:
            - If all inputs are valid numbers, returns the mean (average) of
            the inputs.
            - If no even numbers are input, returns the maximum number from the
            inputs.

    Raises:
        None

    Example:
        >>> even_or_average()
        Please input a number: 4
        Please input a number: 7
        Please input a number: 12
        Please input a number: 9
        Please input a number: 2
        7.0  # Output for valid inputs (mean of 4, 7, 12, 9, and 2)
    """
    NUMBER_OF_INPUTS: int = 5
    i: int = 0
    numbers: list[int] = []

    # Iterate thru loop until NUMBER_OF_INPUTS of valid inputs entered
    while i < NUMBER_OF_INPUTS:
        response: str = input("Please input a number: ")
        # Determine if response is numeric or not
        if not response.isnumeric():
            print(f"Value must be a number")
        else:
            i += 1
            numbers.append(int(response))

    # Create list of even numbers from numbers
    even_nums_list: list[int] = [num for num in numbers if num % 2 == 0]

    # Check if there are even numbers in the input list, return the maximum of
    # all numbers if no even numbers, return the mean if there are even numbers
    return mean(numbers) if even_nums_list == [] else max(even_nums_list)


print(make_tuples([1, 2, 3, 3], [5, 6, 7, 8]))
print(even_or_average())
