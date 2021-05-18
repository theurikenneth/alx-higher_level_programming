#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class with private instance attribute:size"""
    def __init___(self, size):
        """Sets the initial size of the new square object

        Args:
            size (int): the size of the square once instance is created"""
        self.__size = size
