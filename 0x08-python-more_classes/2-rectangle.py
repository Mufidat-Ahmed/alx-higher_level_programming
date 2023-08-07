#!/usr/bin/python3
"""class defination"""


class Rectangle:
    """rectangle representation"""

    def __init__(self, width=0, height=0):
        """rectangle initialization

        Args:
        width(int) = width
        height(int) = height
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """get or set width"""
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
            """get or set height"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = height

        def area(self):
            """return the area of the rectangle"""
            return (self.__width * self.__height)

        def perimeter(self):
            """returns the perimeter of the rectangle"""
            if self.__width or self.__height != 0:
                return 2 * (self.__width * self.__height)
            else:
                return 0
