#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        total = 0
        for k in range(x):
            print(my_list[k], end="")
            total += 1
    except IndexError:
        pass
    finally:
        print()
        return (total)
