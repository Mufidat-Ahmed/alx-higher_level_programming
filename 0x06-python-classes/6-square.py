#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        def size(self):
            return (self.__size)
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            else size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        def position(self):
            return (self.__position)
        def position(self, value):

