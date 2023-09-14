#!/usr/bin/python3
"""
function reading a file
"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")

