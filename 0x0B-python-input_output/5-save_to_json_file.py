#!/usr/bin/python3
"""
module contains one object that write an object to text file
using json
"""

import json


def save_to_json_file(my_obj, filename):
    """
    write an object to text file using json representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
