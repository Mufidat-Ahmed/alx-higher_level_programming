#!/usr/bin/python3
"""defines a function of type JSON-object"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure"""
    return json.loads(my_str)
