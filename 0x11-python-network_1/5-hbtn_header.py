#!/usr/bin/python3
"""script that takes in a url sends request to it and displays value of variable X-Request-Id"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get('X-Request-Id'))
