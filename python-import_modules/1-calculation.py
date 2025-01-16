#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# Assigning values to variables
a = 10
b = 5

# Performing calculations and printing results
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
