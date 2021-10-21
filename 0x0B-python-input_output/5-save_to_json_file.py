#!/usr/bin/python3
"""Defines a function that saves an object to a file as json string"""
import json


def save_to_json_file(my_obj, filename):
    if filename is None:
        return
    with open(filename, "w") as f:
        f.write(my_obj, f)
