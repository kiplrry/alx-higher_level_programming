#!/usr/bin/python3
"""
function that appends to a file
"""


def append_write(filename="", text=""):
    """ function """
    with open(filename, "a", encoding="UTF*") as file:
        return file.write(text)
