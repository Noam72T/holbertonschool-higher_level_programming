#!/usr/bin/python3
import MySQLdb
import sys

def list_states():
    # Get the arguments passed to the script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish the MySQL connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results from the query
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

# Ensure the script is not executed when imported
if __name__ == "__main__":
    list_states()
