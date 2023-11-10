#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    import sys

    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data={'q': letter})
    try:
        data = res.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
