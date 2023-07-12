#!/usr/bin/python3

"""defines a function load_from_json_file"""

import json


def load_from_json_file(filename):
    """create an object from a JSON file"""

    with open(filename, 'r', encoding='UTF -8') as myFile:
        json_object = json.load(myfile)
        return json_object
