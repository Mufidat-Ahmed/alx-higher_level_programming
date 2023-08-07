#!/usr/bin/python3
"""class defination"""


class Rectangle:
    """rectangle representationn"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """
        Args:
        width(int) = width
        height(int) = height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
