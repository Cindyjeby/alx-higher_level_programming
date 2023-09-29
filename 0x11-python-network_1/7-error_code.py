#!/usr/bin/python3
"""script that takes in a url and sends s request to it"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    if (response.status_code >= 400):
        print(f"Errorcode: {response.status_code}")
    else:
        print(response.text)
