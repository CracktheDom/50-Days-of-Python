#!/usr/bin/env python3

"""Write a function called zeros_last. This function takes a list as
argument. If a list has zeros (0), it will move them to the front of
the list and maintain the order of the other numbers in the list.
If there are no Zeros in the list, the function should return the
original list sorted in ascending order. For example, if you pass
[1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
your code should return [1, 2, 4, 6, 7]."""


def zeros_last(num_list: list[int]) -> list[int]:
    """
    Rearranges a list of numbers such that all zeros are moved to the front
    of the list while maintaining the original order of non-zero elements.

    Args:
        num_list (list): A list of numbers.

    Returns:
        list[int]: A new list with zeros moved to the beginning while
        preserving the order of non-zero elements.

    Example:
        >>> zeros_last([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
    """

    # Count the number of zeros in the input list
    num_zeros = num_list.count(0)

    # If there are no zeros, return a sorted copy of the input list
    if 0 not in num_list:
        return sorted(num_list)
    else:
        # Remove each zero from the list num_zeros times
        for count in range(num_zeros):
            num_list.remove(0)

        # Insert each removed zero at the beginning of the list num_zeros times
        num_list = [0] * num_zeros + num_list

    # Return the modified list with zeros moved to the end
    return num_list


print(zeros_last([3, 4, 5, 6, 0, 8, 9, 0, 7, 8, 0, 5, 6, 7]))
print(zeros_last([3, 4, 5, 8, 9, 7, 8, 5, 6, 7]))
