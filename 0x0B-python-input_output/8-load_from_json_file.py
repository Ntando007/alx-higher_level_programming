#!/usr/bin/python3
import json


def load_from_json_file(filename):

    with open(filename) as f:
        json_obj = json.load(f)
    return json_obj
