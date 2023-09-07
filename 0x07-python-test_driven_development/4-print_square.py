#!/usr/bin/python3
'''
Print a square of hastags
the function receives a number
that indicate the size of the side
'''


def print_square(size):
    '''
    Function to print a square of hastags
    '''
    if not (isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for element in range(size):
        print('#' * size)
