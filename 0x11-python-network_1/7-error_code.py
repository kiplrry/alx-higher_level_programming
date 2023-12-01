#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    res = requests.get(url)

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
