#!/usr/bin/python3
"""
module contains json
"""
import json


def to_json_string(my_obj):
    """
    returns a json representation of an object(string)
    """
    return json.dumps(my_obj)
