#!/usr/bin/python3
'''Convert JSON To CSV'''
import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """Convert CSV to JSON"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
