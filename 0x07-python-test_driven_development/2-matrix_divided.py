#!/usr/bin/python3
'''
Function to divides all matrix's elements
by a just one number
can divide integers and floats with two decimals
'''


def matrix_divided(matrix, div):
    '''
    Function two divide each element by a number
    '''
    long_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    for lst in matrix:
        for number in lst:
            if not(isinstance(number, int) or isinstance(number, float)):
                raise TypeError(long_error)

    if not all(map(lambda lst: len(matrix[0]) == len(lst), matrix)):
        raise TypeError(
            'Each row of the matrix must have the same size')

    if not(type(div) is int or type(div) is float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')
    return ([list(map(lambda nm: round(nm / div, 2), lst)) for lst in matrix])
