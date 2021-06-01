#!/usr/bin/python3
"""DEfines a function that loads an object from a json string"""
import json


def from_json_string(my_str):
    """Converst json string to an object"""
    return json.loads(my_str)
