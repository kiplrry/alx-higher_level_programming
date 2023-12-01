#!/usr/bin/python3
from sys import argv
import urllib.request
import urllib.parse


if __name__ == '__main__':
    vals = {
        'email': argv[2],
    }
    data = urllib.parse.urlencode(vals)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
