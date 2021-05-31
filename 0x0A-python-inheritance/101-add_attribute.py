#!/usr/bin/python3
"""Defines a function that safely adds attributes to an object"""


def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
