#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    # Get the info requesting the api
    user = sys.argv[1]
    passw = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(user)

    response = requests.get(url, auth=(user, passw))

    try:
        print(response.json()['id'])
    except KeyError:
        print("None")
