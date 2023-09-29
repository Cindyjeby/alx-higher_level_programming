#!/usr/bin/python3
"""Script that takes in a url an an email and sends post"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    emails = {'email': sys.argv[2]}
    response = requests.post(url, data=emails)
    print(response.text)
