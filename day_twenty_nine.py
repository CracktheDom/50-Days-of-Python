#!/usr/bin/env python3

"""Write a function called middle_figure that takes two
parameters a, and b. The two parameters are strings. The
function joins the two strings and finds the middle element.
If the combined string has a middle element, the function should
return the element, otherwise, return 'no middle figure'. Use
'make love' as an argument for a and 'not wars' as an
argument for b. Your function should return ‘e’ as the middle
element. Whitespaces should be removed."""


def middle_figure(string_a: str, string_b: str) -> str:
    """
    Return the middle character of the combined string of two input strings
    after removing spaces.

    Args:
        string_a (str): The first input string.
        string_b (str): The second input string.

    Returns:
        str: The middle character of the combined string, or "no middle figure"
        if there is no middle character.
    """

    # Combine the input strings 'string_a' and 'string_b', and remove spaces
    # from the combined string.
    combined: str = (string_a + string_b).replace(" ", "")

    # Calculate the length of the combined string.
    length_of_combined: int = len(combined)

    # Check if the length of the combined string is odd.
    if length_of_combined % 2 != 0:
        # If it's odd, return the middle character.
        return combined[length_of_combined // 2]

    # If it's even, there is no middle character.
    return f"no middle figure"


print(middle_figure("make love", "not wars"))
print(middle_figure("make love and tea", "not even one wars  "))
