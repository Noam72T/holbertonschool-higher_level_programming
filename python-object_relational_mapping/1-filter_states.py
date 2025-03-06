#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the `states` table
of the database `hbtn_0e_0_usa` where the `name` matches the argument.
It takes 4 arguments: mysql username, mysql password, database name, and state name.
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by `states.id` and displayed as tuples.
"""

import MySQLdb
import sys

def filter_states(username, password, db_name, state_name):
    """
    Displays all values in the `states` table where the `name` matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.
    """
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Ensure the script is not executed when imported
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        filter_states(username, password, db_name, state_name)
