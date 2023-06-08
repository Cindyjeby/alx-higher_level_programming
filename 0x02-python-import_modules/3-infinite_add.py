#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(0)
    else:
        total = sum(int(k) for k in sys.argv[1:])
        print(total)
