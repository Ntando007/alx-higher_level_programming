#!/usr/bin/python3
import json


def load_from_json_file(filename):

    with open(filename) as x:
        json_obj = json.load(x)
    return json_obj
