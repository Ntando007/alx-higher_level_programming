#!/usr/bin/python3
"""Documentation for write_file function"""


def write_file(filename="", text=""):

    with open(filename, 'w', encoding='utf-8') as f:
        filex = f.write(text)
        return filex
