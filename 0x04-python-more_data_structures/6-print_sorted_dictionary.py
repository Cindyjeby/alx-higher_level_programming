#!/sur/bin/python3
def print_sorted_dictionary(a_dictionary):
    for number, value in sorted(a_dictionary.items()):
        print("{}: {}".format(number, value))
