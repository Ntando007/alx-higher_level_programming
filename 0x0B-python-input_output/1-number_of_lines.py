#!/usr/bin/python3
"""Documentation for number_of_lines function"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file
    """
    with open(filename, encoding='utf-8') as x:
        line_num = 0
        for i in x:
            line_num += 1
        return line_num
