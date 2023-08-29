#!/usr/bin/python3
class Square:
    """
    Class to find an square area
    """
    def __init__(self, size=0):
        """
        This is the constructor
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        Function to find a square area
        """
        return(self.__size**2)
