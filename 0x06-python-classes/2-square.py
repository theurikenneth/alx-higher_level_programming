#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Sqaure class with size as private instance attribute"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
