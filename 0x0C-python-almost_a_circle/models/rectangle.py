#!/usr/bin/python3
"""defines rectangle class"""
from base import Base


class Rectangle:
    """Rectangle representation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
        width: width of the rectangle
        height: height of the rectangle
        x: rectangle coordinates
        y: rectangle coordinates
        id: rectangle identity
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__inti__(id)

    @property
    def width(self):
        """set/gets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/gets height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, int):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, int):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """update the rectangle to accept arguments
        Args:
        *args: new argument attribute
        kwargs:  assigns a key/value argument to attributes
        """
        if args and len(args) != 0:
            m = 0
            for index in args:
                if m == 0:
                    if index is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = index
                elif m == 1:
                    self.width = index
                elif m == 2:
                    self.height = index
                elif m == 3:
                    self.x = index
                elif m == 4:
                    self.y = index
                m += 1

        elif kwargs and len(kwargs) != 0:
            for i, a in kwargs.items():
                if i == "id":
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif i == "width":
                    self.width = a
                elif i == "height":
                    self.height = a
                elif i == "x":
                    self.x = a
                elif k == "y":
                    self.y = a

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        return {
           "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """str representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
