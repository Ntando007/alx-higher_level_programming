#!/usr/bin/python3
"""Documentation for Mylist object"""


class MyList(list):

    """Mylist class inherit from the list class"""

    def print_sorted(self):
        """Function that sorts the list"""

        print(sorted(self))
