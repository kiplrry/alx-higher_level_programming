#!/usr/bin/python3
"""
Function that deserializes json to a python object
"""
import json


def from_json_string(my_str):
    """the function"""
    return json.loads(my_str)
