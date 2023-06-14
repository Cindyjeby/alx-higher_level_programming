#!/usr/bin/python3
def only_diff_element(set_1, set_2):
    diff_element = set_1 ^ set_2
    return sorted(list(diff_element))
