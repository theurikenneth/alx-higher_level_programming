#!/usr/bin/python3
"""Checks if an object is a subclass of another class"""


def inherits_from(obj, a_class):
    if obj.__class__ is not a_class:
        return isinstance(obj, a_class)
