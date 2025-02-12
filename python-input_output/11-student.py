#!/usr/bin/python3
'''Class Student'''


class Student:
    def __init__(self, first_name, last_name, age):
        """
       Initializes a new instance of Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): List of strings representing the names of attributes to be retrieved.

        Returns:
            dict: A dictionary containing the attributes of the instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those provided in the json dictionary.

        Args dictionary:
            json (dict): A dictionary containing the instance's new attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
