#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class with size as private instance attribute"""
    def __init__(self, size=0):
        """Initializes the Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size