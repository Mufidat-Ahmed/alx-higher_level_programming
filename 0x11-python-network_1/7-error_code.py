#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""


if __name__ == '__main__':
    import requests
    import sys

    url = requests.get(sys.argv[1])
    if url.status_code >= 400:
        print("Error code:", url.status_code)
    else:
        print(url.text)
