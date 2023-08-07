#!/usr/bin/python3
"""class defination"""


class Rectangle:
    """rectangle representation"""

    def __init__(self, width=0, height=0):
        """initialization of rectangle
        Args:
        width(int) = width
        height(int) = height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """set or get width of rectangle"""
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
        """setor get height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """represents the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        cat = []
        for i in range(self.__height):
            [cat.append('#') for m in range(self.__width)]
            if i != self.__height - 1:
                cat.append("\n")
        return ("".join(cat))
