#!/usr/bin/python3

"""define a function sav_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""

    with open(filename, 'w', encoding='UTF -8') as myFile:
        myJsonObj = json.dumps(my_obj)
        myFile.write(myJsonObj)
