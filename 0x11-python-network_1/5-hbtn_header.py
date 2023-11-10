#!/usr/bin/python3
"""sends a request to the URL
displays the value of the variable X-Request-Id in the response header
"""


if __name__ == '__main__':
    import requests
    import sys

    url = requests.get(sys.argv[1])
    print(url.headers.get('X-Request-Id'))
