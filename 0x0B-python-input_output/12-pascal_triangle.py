#!/usr/bin/python3

"""defines a function pascal_triangle"""


def pascal_triangle(n):
    """Return alist of lists of int"""

    angle = []
    if n <= 0:
        return angle
    if n == 0:
        return [[1]]

    angle = [[1]]
    for k in range(n-1):
        angle.append([a+b for a, b in zip([0] + angle[-1], angle[-1] + [0])])
    return angle
