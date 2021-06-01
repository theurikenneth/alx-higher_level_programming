#!/usr/bin/python3
"""Defines a function that prints a UTF-8 text file"""


def read_file(filename=""):
    with open(filename, "r", encoding='UTF-8') as f:
        print(f.read(), end="")
