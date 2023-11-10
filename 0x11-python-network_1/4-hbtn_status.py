#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
You must use the package requests
"""


if __name__ == '__main__':
    import requests

    url = requests.get('https://alx-intranet.hbtn.io/status')
    content = url.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
