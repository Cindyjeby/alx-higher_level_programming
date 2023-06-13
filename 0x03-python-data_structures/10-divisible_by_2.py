#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    second_list = []
    for value in my_list:
        if value % 2 == 0:
            second_list.append(True)
        else:
            second_list.append(False)
    return second_list
