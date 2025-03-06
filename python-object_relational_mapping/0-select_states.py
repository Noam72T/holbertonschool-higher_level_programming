#!/usr/bin/python3
"""
Module listing all states from the database `hbtn_0e_0_usa`.
This script takes 3 arguments: mysql username, mysql password, and database name.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by `states.id` and displayed as tuples.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to fetch all states sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
