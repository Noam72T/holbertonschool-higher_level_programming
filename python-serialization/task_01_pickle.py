#!/usr/bin/python3
'''Pickle Serialization'''
import pickle


class CustomObject:
    """Class Custom Object"""
    def __init__(self, name: str, age: int, is_student: bool):
        """Initialise the atribute of the object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serialize this object"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization Error: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize this object"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization Error: {e}")
            return None
