#!/usr/bin/python3
"""Documentation for a Student class"""


class Student:

    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function for Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of an object or
           a dictionary representation of all string attributes
        """

        if not isinstance(attrs, list):
            return self.__dict__
        for var in attrs:
            if not isinstance(var, str):
                return self.__dict__
        string_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                string_dict[string] = self.__dict__[string]
        return string_dict
