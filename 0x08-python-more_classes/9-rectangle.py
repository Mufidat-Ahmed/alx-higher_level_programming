#!/usr/bin/python3
"""class defination"""


class Rectangle:
    """rectangle representationn"""

    number_of_instances = 0
    print_symbol = '#'

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
            [cat.append(str(self.print_symbol)) for m in range(self.__width)]
            if i != self.__height - 1:
                cat.append("\n")
        return ("".join(cat))

    def __repr__(self):
        """returns string representation of rectangle"""
        cat = "Rectangle(" + str(self.__width)
        cat += ", " + str(self.__height) + ")"
        return (cat)

    def __del__(self):
        """Print Bye rectangle for every deletion done"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle
        Args:
        rect_1(Rectangle): rectangle one
        rect_2(Rectangle): rectangle two
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def square(cls, size=0):
        """returns a square
        Args:
        size(cls): height and width of the square
        """
        return (cls(size, size))
