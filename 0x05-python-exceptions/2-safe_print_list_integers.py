#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for k in range(x):
            if type(my_list[k]) is int:
                print("{:d}".format(my_list[k]), end="")
                total += 1
    except IndexError:
        pass
    finally:
        print()
        return (total)
