#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    creates an object from json file
    """
    with open("filename", 'r', encoding='utf-8') as f:
        my_obj = json.loads(f)
