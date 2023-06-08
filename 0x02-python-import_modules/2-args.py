#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = sys.argv[1:]

    if len(count) == 0:
        print(f"0 arguments.")
    elif len(count) == 1:
        print(f"1arguments:")
    else:
        print(f"{len(count)}arguments:")

        for k, arg in enumerate(count):
            print(f"{k+1}: {arg}")
