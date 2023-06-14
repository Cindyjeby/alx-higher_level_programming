#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    weight = []
    size = 0
    for total, point in my_list:
        weight.append(total * point)
        size += point
        weight_average = sum(weight) / size
        return weight_average
