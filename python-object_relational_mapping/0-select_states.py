#!/usr/bin/python3
import sys
import MySQLdb

def list_states():
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish the MySQL connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to get all states in ascending order by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all rows from the executed query
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states()
