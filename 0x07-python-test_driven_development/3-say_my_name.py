#!/usr/bin/python3
'''
Function that prints My name is...
 <name> <lastname>
'''


def say_my_name(first_name, last_name=""):
    '''
    Print the complete name
    '''
    if not(type(first_name) is str):
        raise TypeError('first_name must be a string')
    if not(type(last_name) is str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
