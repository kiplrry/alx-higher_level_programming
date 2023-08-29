#!/usr/bin/python3
class Square:
    """
    Class to find an square area
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is the constructor
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        for x in position:
            if not isinstance(x, int) or x < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            self.__position = position

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

    @property
    def position(self):
        """
        Obtain the atribute position value
        """
        return(self.__position)

    @position.setter
    def position(self, value):
        """
        Put the value and handle the errors
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        for x in value:
            if not isinstance(x, int) or x < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            self.__position = value

    def area(self):
        """
        Function to find a square area
        """
        return self.__size**2

    def my_print(self):
        """
        Function to print an square
        """
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for y in range(self.__size):
                print(' ' * self.position[0], end='')
                print('#' * self.__size, end='')
                print("")
