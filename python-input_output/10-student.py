#!/usr/bin/python3
'''Class Student'''


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.
        
        Args:
            first_name (str): Name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a JSON representation of the instance.
        
        Args:
            attrs (list): List of attributes to	return.
        
        Returns:
            dict: Dictionnary .
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}