#!/usr/bin/python3
def magic_calculation(a, b):
    total = 0
    for k in range(1, 4):
        try:
            if k > a:
                raise Exception('Too far')
            else:
                total += (a ** b) / k
        except Exception:
            total = a + b
            break
    return (total)
