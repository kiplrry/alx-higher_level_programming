#!/usr/bin/python3
"""
script that checks iheritance
"""


def inherits_from(obj, a_class):
    """
    function doing the check
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
