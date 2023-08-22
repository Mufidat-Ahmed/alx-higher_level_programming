#!/usr/bin/python3
"""Defination of class square"""
from rectangle import Rectangle


class Square:
    """square representation"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
        size: size of the square
        x: coordinates of the square
        y: coordinates of the square
        id: identity of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Args:
        *args: arguments to the square
        **kwargs: dictionary for the square
        """
        if args:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attr_names):
                    setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary rep of a square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """str representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
