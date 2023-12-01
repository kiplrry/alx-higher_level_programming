#!/usr/bin/python3
"""python script to get status from an url"""
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        ans = res.read()
        print("Body response:")
        print(f"\t- type: {type(ans)}")
        print(f"\t- content: {ans}")
        print(f"\t- utf8 content: {ans.decode('utf-8')}")
