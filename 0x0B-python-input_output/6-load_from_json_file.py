#!/usr/bin/python3
"""
function loading json from a file
"""
import json


def load_from_json_file(filename):
    """function"""
    with open(filename, "r", encoding="UTF8") as fp:
        return json.load(fp)
