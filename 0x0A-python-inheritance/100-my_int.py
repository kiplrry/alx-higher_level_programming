#!/usr/bin/python3
"""
Class Myint inherits from int
"""


class MyInt(int):
    """
    class MyInt
    """
    def __eq__(self, value):
        return not super().__eq__(value)

    def __ne__(self, value):
        return not super().__ne__(value)
