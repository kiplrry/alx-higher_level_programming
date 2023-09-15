#!/usr/bin/python3
"""
unction that returns the dictionary description with simple data structure\
(list, dictionary, string, integer and boolean) \
for JSON serialization of an objec
"""
import json


def class_to_json(obj):
    """ the function"""
    return obj.__dict__
