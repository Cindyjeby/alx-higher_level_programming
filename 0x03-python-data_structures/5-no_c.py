#!/usr/bin/python3
def no_c(my_string):
    second_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            second_string += char
            return second_string
