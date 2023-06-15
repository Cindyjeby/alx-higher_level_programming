#!/sur/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_list = list(a_dictionary.keys())
    order_list.sort()
    for k in order_list:
        print("{}: {}".format(k, a_dictionary.get(k)))
