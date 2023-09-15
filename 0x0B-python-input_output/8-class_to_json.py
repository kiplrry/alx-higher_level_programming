#!/usr/bin/python3
"""
unction that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """ the function"""
    return obj.__dict__
