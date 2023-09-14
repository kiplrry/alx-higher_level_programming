#!/usr/bin/python3
"""
function reading a file
"""


def read_file(filename=""):
    """
    function
    """
    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
