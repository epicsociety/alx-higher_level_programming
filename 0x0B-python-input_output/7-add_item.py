#!/usr/bin/python3
"""
module contains imported module and one internal method
"""

from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

for arg in argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
