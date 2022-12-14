#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
    Args:
        filename: name of the file
    """
    with open(filename, "r") as myFile:
        return json.load(myFile)
