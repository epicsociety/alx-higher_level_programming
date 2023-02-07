#!/usr/bin/python3
"""
module contains json
"""
import json


def from_json_string(my_str):
    """
    returns an object (python data structure) represented
    by a json string
    """
    return json.loads(my_str)
