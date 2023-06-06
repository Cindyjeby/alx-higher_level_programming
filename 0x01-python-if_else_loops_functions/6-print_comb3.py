#!/usr/bin/python3
for k in range(10):
    for l in range(k+1, 10):
        print("{:d}{:d}",format(k, l), end="")
        if k != 8 or l != 9:
            print(", ", end="")
        else:
            print()
