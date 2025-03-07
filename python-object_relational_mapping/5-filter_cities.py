#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create cursor object
    cur = db.cursor()

    # Execute query to get cities of the specified state
    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (argv[4],))

    # Fetch all results
    rows = cur.fetchall()

    # Print results
    if rows:
        print(", ".join(row[0] for row in rows))
    else:
        print()

    # Close cursor and database connection
    cur.close()
    db.close()
