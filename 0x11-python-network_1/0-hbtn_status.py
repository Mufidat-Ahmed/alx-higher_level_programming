#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"


with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type: <class 'bytes'>")
    print("\t- content: b'OK'")
    print("\t- utf8 content: OK")
