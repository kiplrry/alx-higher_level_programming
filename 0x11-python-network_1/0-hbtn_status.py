#!/usr/bin/python3
"""python script to get status from an url"""
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')


with urllib.request.urlopen(req) as res:
    ans = res.read()
    print(
        f"""Body response:
    - type: {type(ans)}
    - content: {ans}
    - utf8 content: {ans.decode('utf-8')}"""
    )
