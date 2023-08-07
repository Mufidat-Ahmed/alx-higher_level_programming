#!/usr/bin/python3
"""class defination"""


class Rectangle:
    """class representation"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle
        Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """set rectangle width"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if vaule < 0:
                raise TypeError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """set or get height of rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance("value, int"):
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")
            self.__height = value
