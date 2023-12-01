#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
sthe value of the variable X-Request-Id in the response header"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)

    print(res.headers.get("X-Request-Id"))
