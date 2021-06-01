#!/usr/bin/python3
"""Defines a function that saves an object to a file as json string"""
import json


def save_to_json_file(my_obj, filename):
    if filename is None:
        return
    with open(filename, mode="w", encoding='UTF-8') as f:
        json_var = json.dump(my_obj, f)
