#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            deleted.append(key)
    for key in deleted:
        del a_dictionary[key]
    return a_dictionary
