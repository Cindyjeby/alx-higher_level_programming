#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for value in range(idx + 1, len(my_list)):
        my_list[value - 1] = my_list[i]
        del mylist[-1]
    return my_list
