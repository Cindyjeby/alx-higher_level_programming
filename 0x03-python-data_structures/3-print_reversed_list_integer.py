#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        None
    else:
        k = len(my_list) - 1
        while k >= 0:
            print("{:d}".format(my_list[k]))
            k -= 1
