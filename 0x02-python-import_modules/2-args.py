#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = sys.argv

    if len(count) == 0:
        print("0 arguments.")
    elif len(count) == 2:
        print("1 arguments:")
        print(f"1: {count[1]}")
    else:
        print(f"{len(count)-1} arguments:")

        for k in range(1, len(count)):
            print(f"{k}: {count[k]}")
