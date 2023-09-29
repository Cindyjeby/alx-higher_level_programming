#!/usr/bin/python3
"""
script that takes in a url,
sends a request to the url and 
displays the value of the X-Request-Id variable found in the header of the response"""


if __name__ == '__main__':
    import sys
    from urllib import request

    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
