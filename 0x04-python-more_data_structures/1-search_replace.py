#!/usr/bin/python3
def search_replace(my_list, search, replace):
    second_list = []
    for number in my_list:
        if number == search:
            second_list.append(replace)
        else:
            second_list.append(number)
    return second_list
