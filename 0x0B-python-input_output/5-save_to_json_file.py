#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    write an object to text file using json representation
    """
    data = json.dumps(my_obj)
    with open("filename.txt", 'w', encoding='utf-8') as f:
        f.write(data)
