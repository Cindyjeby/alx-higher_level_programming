#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord(k) >= 97 and ord(k) <= 122:
            l = chr(ord(k) - 32)
        else:
            l = k
            print("{}".format(l), end="")
            print()
