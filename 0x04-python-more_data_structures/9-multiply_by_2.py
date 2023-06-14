#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_tionary = {}
    for key, value in a_dictionary.items():
        mul_value = value * 2
        new_tionary[key] = mul_value
        return new_tionary
