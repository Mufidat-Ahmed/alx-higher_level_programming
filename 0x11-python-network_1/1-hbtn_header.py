#!/usr/bin/python3
"""sends a request to the URL
    -displays the value of the X-Request-Id
    -variable found in the header of the response.
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_Id = response.headers.get('X-Request-Id')
        print(x_request_Id)
