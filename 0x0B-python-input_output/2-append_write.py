#!/usr/bin/python3
"""Documentation for append_write function"""


def append_write(filename="", text=""):

    with open(filename, 'a', encoding='utf-8') as y:
        file_ = y.write(text)
        return file_
