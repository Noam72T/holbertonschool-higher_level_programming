#!/usr/bin/python3
'''Mode - 7-base_geometry'''


class BaseGeometry:
    '''Base Geometry class'''

    def area(self):
        """Not Implémented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''fnc fir int validator'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

