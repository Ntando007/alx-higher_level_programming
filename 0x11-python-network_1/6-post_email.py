#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST
 request to the passed URL with the email as a parameter, and
finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]
    my_mail = sys.argv[2]
    request = requests.get(my_url, data={'email': my_mail})
    posted = request.text
    print(posted)
