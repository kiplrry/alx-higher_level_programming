#!/usr/bin/python3
""""
function writing json data to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """the function"""
    with open(filename,  "w", encoding="UTF*") as fp:
        json.dump(my_obj, fp)
