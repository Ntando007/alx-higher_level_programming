#!/usr/bin/python3
"""Documentation for append_write function"""


def append_write(filename="", text=""):

    with open(filename, 'a', encoding='utf-8') as f:
        filex = f.write(text)
        return filex
