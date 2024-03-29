#!/usr/bin/python3
"""
class squre inheriting from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class square
    """
    def __init__(self, size):
        if self.integer_validator("size", size):
            self.__size = size
            super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
