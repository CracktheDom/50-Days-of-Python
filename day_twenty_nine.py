#!/usr/bin/env python3

"""Write a function called middle_figure that takes two
parameters a, and b. The two parameters are strings. The
function joins the two strings and finds the middle element.
If the combined string has a middle element, the function should
return the element, otherwise, return 'no middle figure'. Use
'make love' as an argument for a and 'not wars' as an
argument for b. Your function should return āeā as the middle
element. Whitespaces should be removed."""


def middle_figure(a: str, b: str) -> str:
    combined = (a + b).replace(' ', '')
    length_of_combined = len(combined)
    if length_of_combined % 2 != 0:
        return combined[length_of_combined // 2]
    else:
        return f"no middle figure"


print(middle_figure('make love', 'not wars'))
print(middle_figure('make love and tea', 'not even one wars  '))
