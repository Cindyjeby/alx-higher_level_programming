#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        total = add(a, b)
        for k in range(4, 7):
            total = add(total, k)
        return (total)
    else:
        return (sub(a, b))
