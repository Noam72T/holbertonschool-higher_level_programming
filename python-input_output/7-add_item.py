#!/usr/bin/python3
'''Import Libraries'''
import os 
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
loaload_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
	items = loaload_from_json_file(filename)
else:
    items = []
    
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
