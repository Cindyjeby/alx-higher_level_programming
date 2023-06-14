#!/usr/bin/python3
def common_element(set_1, set_2):
    same_element = set()
    for element in set_1:
        if element in set_2:
            same_element.add(element)
    return same_element
