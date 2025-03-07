#!/usr/bin/python3
"""
Module that safely lists states from the database that match the name argument
This version is protected against SQL injection
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    # Create cursor and execute query with parameterized input
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (argv[4],)
    )

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
