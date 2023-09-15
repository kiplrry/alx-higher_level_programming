#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {x: self.__dict__[x] for
                    x in list(attrs) if x in self.__dict__}

    def reload_from_json(self, json):
        for key, value in json.items():
            self[key] = value
