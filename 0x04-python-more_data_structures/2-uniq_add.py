#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_add = set()
    for value in my_list:
        new_add.add(value)
        total = sum(new_add)
        return total
