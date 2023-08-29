#!/usr/bin/python3
class Square:
    """
    Class to find an square area
    """
    def __init__(self, size=0):
        """
        This is the constructor
        """
        self.__size = size

    @property
    def size(self):
        """
        Action to obtain the atribute value
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """
        Put the value and handle the errors
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Function to find a square area
        """
        return(self.__size**2)

    def my_print(self):
        """
        Function to print an square
        """
        if self.size == 0:
            print()
        for x in range(self.size):
            print('#'*self.size)
