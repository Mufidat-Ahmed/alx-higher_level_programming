#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter
displays the body of the response.
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    res = requests.post(url, data=data)
    print(res.text)
