#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
from pathlib import Path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


"""function"""
j_file = "add_item.json"
fp = Path(j_file)
if not Path.exists(fp):
    fp.write_text(str([]))
loaded_json = load_from_json_file(j_file)
new_json = loaded_json + sys.argv[1:]
save_to_json_file(new_json, j_file)
