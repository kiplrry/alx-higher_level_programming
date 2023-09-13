#!/usr/bin/python3
"""
class that sorts list
"""


class MyList(list):
    """
    class that inherits from list
    """
    def print_sorted(self):
        self.sort()
        print(self)
