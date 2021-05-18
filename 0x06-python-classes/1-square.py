#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class with size as private instance attribute"""
    def __init___(self, size):
        """Sets the initial size of the new square object

        Args:
            size (int): the size of the square once instance is created"""
        self.__size = size
