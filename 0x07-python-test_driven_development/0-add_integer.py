#!/usr/bin/python3
"""
Function that returns the add two integers
"""


def add_integer(a, b=98):
    """ Adds two integers
    a and b must be integers if they are floats
    it casts them, it returns the sum of a and b.
    """

    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError('a must be an integer')
        elif isinstance(b, (int, float)) is False:
            raise TypeError('b must be an integer')
        return(int(a) + int(b))
    except:
        raise
