#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):  # Check if idx is out of range
        return my_list  # Return the original list if invalid index

    del my_list[idx]  # Use the `del` statement to remove the element at idx
    return my_list  # Return the modified list
