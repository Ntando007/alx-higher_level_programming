#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
