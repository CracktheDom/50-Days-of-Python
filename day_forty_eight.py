#!/usr/bin/env python3

"""
Write a function called search_binary that searches for the
number 22 in the following list and returns its index. The
function should take two parameters, the list and the item that
is being searched for. Use binary search (iterative Method).
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
"""


def search_binary(binary_search_list: list[int], num_to_search: int) -> int | str:
    """
    Perform a binary search to find the index of a specified number in a sorted
    list.

    Args:
        binary_search_list[int] (list): A list of integers.
        num_to_search (int): The integer to search for in the list.

    Returns:
        int: The index of the 'num_to_search' in the 'binary_search_list' if
        found, or a message indicating that the number is not in the list.

    Example:
        >>> search_binary([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
        5
        >>> search_binary([10, 20, 30, 40, 50], 35)
        '35 is not in provided list of numbers'
    """
    # Check if the number to search is in the list
    if num_to_search in binary_search_list:
        # Sort the list (in case it's not already sorted)
        sorted_list: list[int] = sorted(binary_search_list)

        # Calculate the middle element's index
        middle_index: int = len(sorted_list) // 2
        middle_element: int = sorted_list[middle_index]

        # Check if the number to search is in the first half of the sorted list
        if num_to_search < middle_element:
            # Iterate through the first half of the sorted list
            for index in range(middle_index):
                if num_to_search == sorted_list[index]:
                    return binary_search_list.index(num_to_search)

        # Check if the number to search is in the second half of the sorted list
        elif num_to_search >= middle_element:
            # Iterate through the second half of the sorted list
            for element in sorted_list[middle_index:]:
                if num_to_search == element:
                    return binary_search_list.index(num_to_search)

    # Return message if the number is not found in the list
    return f"{num_to_search} is not in the provided list of numbers"


LIST1 = [12, 34, 56, 63, 89, 73, 78, 98, 22, 45, 13]
NUM = 22

if __name__ == "__main__":
    print(search_binary(LIST1, NUM))

# assert search_binary(LIST1, NUM) == 5
