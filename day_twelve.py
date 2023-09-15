#!/usr/bin/env python3

"""Write a function called count_dots. This function takes a
string separated by dots as a parameter and counts how many
dots are in the string. For example, ‘h.e.l.p.’ should return 4
dots, and ‘he.lp.’ should return 2 dots."""


def count_dots(string: str) -> int:
    return (
        f"{string.count('.')} dots"
        if string.count(".") >= 2 or string.count(".") == 0
        else f"{string.count('.')} dot"
    )


print(count_dots("h.e.l.p."))
print(count_dots("he.lp."))
print(count_dots("h.e.l.p.i.n.g.h.a.n.d.s."))
print(count_dots("help"))
