#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    roman_number = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    current_value = roman_number[roman_string[-1]]
    number = current_value
    for a in range(len(roman_string) - 1, 0, -1):
        current_value = roman_number[roman_string[a]]
        prev_value = roman_number[roman_string[a - 1]]
        if prev_value < current_value:
            number -= prev_value
        else:
            number += prev_value
    return number
