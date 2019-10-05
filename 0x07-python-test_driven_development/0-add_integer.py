#!/usr/bin/python3
"""
Function that returns the add two integers
"""


def add_integer(a, b=98):
    """ Adds two integers
    a and b must be integers if they are floats
    it casts them, it returns the sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
