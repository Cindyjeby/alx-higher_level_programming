#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
    for key, volume in list(a_dictionary.keys()):
        if volume == value:
            del a_dictionary[key]
            break
    return a_dictionary
