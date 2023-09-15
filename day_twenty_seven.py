#!/usr/bin/env python3

"""Write a function called unique_numbers that takes a list of
numbers as an argument. Your function is going to find all the
unique numbers in the list. It will then sum up the unique
numbers. You will calculate the difference between the sum of
all the numbers in the original list and the sum of unique
numbers in the list. If the difference is an even number, your
function should return the original list. If the difference is an
odd number, your function should return a list with unique
numbers only. For example [1, 2, 4, 5, 6, 7, 8, 8] should
return [1, 2, 4, 5, 6, 7, 8, 8]."""


def unique_numbers(numList: list[int]) -> list[int]:
    """
    Returns a list of unique numbers from the input list and checks if their sum
    is even. If the sum is even, it returns the original list; otherwise, it
    returns the list of unique numbers.

    Args:
        numList (list[int]): A list of integers.

    Returns:
        list[int]: Either the original list or a list of unique numbers,
        depending on whether the sum of unique numbers is even or not.
    """
    # Create a list of unique numbers by converting the input list to a set
    unique_num_list: list[int] = list(set(numList))

    # Calculate the sum of unique numbers
    sum_of_unique_nums: list[int] = sum(unique_num_list)

    # Calculate the sum of the original numbers
    sum_of_original_nums: list[int] = sum(numList)

    # Check if the difference between the sum of original and unique numbers is
    # even
    # If it's even, return the original list; otherwise, return the list of
    # unique numbers
    return (
        numList
        if (sum_of_original_nums - sum_of_unique_nums) % 2 == 0
        else unique_num_list
    )


"""Extra Challenge: Difference of two Lists
Write a function called difference that takes two lists as
arguments. This function should return all the elements that are
in list a but not in list b and all the elements in list b not in list
a. For example:
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
should return:
[4, 6, 7, 9]
Use list comprehension in your function."""


def difference(list_a: list[int], list_b: list[int]) -> list[int]:
    return list(set(list_a) ^ set(list_b))


print(unique_numbers([1, 2, 4, 5, 6, 7, 8, 8]))
print(difference([1, 2, 4, 5, 6], [1, 2, 5, 7, 9]))
