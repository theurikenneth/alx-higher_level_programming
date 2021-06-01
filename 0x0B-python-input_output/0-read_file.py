#!/usr/bin/python3
"""Defines a function that prints a UTF-8 text file"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        read_result = f.read()
        print(read_result, end="")
