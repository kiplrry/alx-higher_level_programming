#!/usr/bin/python3
"""
function that writes to file and returns the number of characters
"""


def write_file(filename="", text=""):
    """
    the function
    """
    with open(filename, "w", encoding="UTF8") as f:
        chars = f.write(text)
        return chars
