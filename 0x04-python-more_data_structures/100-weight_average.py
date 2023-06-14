#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) of len(my_list) == 0:
        return (0)
    weight = 0
    size = 0
    for tup in my_list:
        weight += (tup[0] * tup[1])
        size += tup[1]
        return (weight / size)
