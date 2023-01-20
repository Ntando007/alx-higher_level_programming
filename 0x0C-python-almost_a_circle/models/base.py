#!/usr/bin/python3
"""Documentation for base class"""
import json
import csv
import os.path


class Base:

    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of arguments
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string
        representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set
        """

        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            new_base = cls(1, 1)
        if cls == Square:
            new_base = cls(1)
        new_base.update(**dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instance_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename) as f:
                instance_object = cls.from_json_string(f.read())
                for instance_dict in instance_object:
                    instance_list.append(cls.create(**instance_dict))
                return instance_list
        else:
            return []
