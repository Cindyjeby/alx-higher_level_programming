#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, volume in list(a_dictionary.keys()):
        if volume == value:
            del a_dictionary[key]
    return a_dictionary
