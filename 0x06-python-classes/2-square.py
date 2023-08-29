#!/usr/bin/python3
"""Defining  class Square."""


class Square:
    """Represents square."""

    def __init__(self, size=0):
        """Initializing new Square.

        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

