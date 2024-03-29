#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
