#!/usr/bin/python3
"""
function that inserts a line of text to a
 file, after each line containing a specific string
 """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+", encoding="UTF8") as fp:
        for line in fp:
            if line.find(search_string) != -1:
                fp.write(new_string)
