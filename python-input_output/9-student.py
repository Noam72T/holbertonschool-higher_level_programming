#!/usr/bin/python3
'''Class Student'''


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description"""
        return self.__dict__
