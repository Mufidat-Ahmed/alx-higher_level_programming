#!/usr/bin/python3
"""Define a class"""


class Square:
    """Rep athe class"""

    def __init__(self, size=0):
        """
        Args:
        size(int): size of the int
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
