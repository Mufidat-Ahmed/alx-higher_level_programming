#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter
    -displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
