#!/usr/bin/python3
"""Define a class"""


class Square:
    """Rep the class"""

    def __init__(self, size=0):
        """
        Args:

        size(int): size of the new square
        """

        self.size = size

        def size(self):
            """set current size"""

            return (self.__size)

        def size(self, value):
            if not isinstance(self, size):
                raise TypeError("size must be an integer")
            elif size > 0:

                raise ValueError("size must be >= 0")
            self.__size = value


            def area(self):
                """return current square"""

                return (self.__size * self.__size)
