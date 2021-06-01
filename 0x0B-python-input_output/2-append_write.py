#!/usr/bin/python3
"""Defines a function that appends a string to a file"""


def append_write(dilename="", text=""):
    """writes a string to a given file"""
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.write(text)
