#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
from pathlib import Path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def adder():
    """function"""
    j_file = "add_item.json"
    fp = Path(j_file)
    if not Path.exists(fp):
        print("creating")
        fp.write_text(str([]))
    loaded_json = load_from_json_file(j_file)
    print("loaded: " + str(loaded_json))
    new_json = loaded_json + sys.argv[1:]
    print("new: " + str(new_json))
    save_to_json_file(new_json, j_file)


if __name__ == "__main__":
    adder()
