#!/usr/bin/env python3

from statistics import mean


"""Write a function called make_tuples that takes two lists,
equal lists, and combines them into a list of tuples. For
example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
function should return [(1,5), (2,6), (3,7), (4,8)]."""


def make_tuples(list1, list2) -> tuple:
    if len(list1) == len(list2):
        return [(i) for i in zip(list1, list2)]


"""Extra Challenge: Even Number or Average
Write a function called even_or_average that ask a user to
input five numbers. Once the user is done, the code should
return the largest even number in the inputted numbers. If
there is no even number in the list, the code should return the
average of all the five numbers."""


def even_or_average():
    NUMBER_OF_INPUTS: int = 5
    i: int = 0
    numbers: list[int] = []
    while i < NUMBER_OF_INPUTS:
        response: str = input("Please input a number: ")
        if not response.isnumeric():
            print(f"Value must be a number")
        else:
            i += 1
            numbers.append(int(response))
    even_nums_list: list[int] = [num for num in numbers if num % 2 == 0]
    return mean(numbers) if even_nums_list == [] else max(even_nums_list)


print(make_tuples([1, 2, 3, 3], [5, 6, 7, 8]))
print(even_or_average())
