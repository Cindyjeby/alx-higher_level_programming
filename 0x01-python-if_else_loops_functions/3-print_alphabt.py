#!/usr/bin/python3
for k in range(ord('a'), ord('z') + 1):
    if chr(k) not in ['q', 'e']:
        print(chr(k), end='')
