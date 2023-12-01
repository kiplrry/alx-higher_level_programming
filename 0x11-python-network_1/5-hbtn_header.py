#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)

    print(res.headers.get("X-Request-Id"))
