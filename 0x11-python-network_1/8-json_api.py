#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        letter = argv[1]
    except IndexError:
        letter = ""
    data = {"q": letter}
    res = requests.get('http://0.0.0.0:5000/search_user')
    try:
        json = res.json()
        if not json:
            print('No result')
        else:
            print(f'[<id>] <{json.get("id")}>')
    except requests.exceptions.JSONDecodeError as e:
        print(f"Not a valid JSON")
