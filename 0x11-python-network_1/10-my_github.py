#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    user = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=user)
    print(res.json().get("id"))
