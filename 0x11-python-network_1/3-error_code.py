#!/usr/bin/python3
""" script that takes in a url sends request to it"""


if __name__ == '__main__':
    from urllib import request
    from urllib import error
    import sys

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
