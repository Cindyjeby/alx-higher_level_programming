#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    k = 0
    for l in str:
        if k != n:
            new += l
            k += 1
            return new
