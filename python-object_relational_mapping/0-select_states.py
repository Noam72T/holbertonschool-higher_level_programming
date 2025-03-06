#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
This script connects to a MySQL database and retrieves all states,
displaying them in ascending order by their ID.
"""

import MySQLdb
import sys


def connect_to_db(username, password, database):
    """
    Establishes a connection to the MySQL database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        MySQLdb.connections.Connection: Database connection object
    """
    return MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )


def get_states(cursor):
    """
    Retrieves all states from the database ordered by ID.

    Args:
        cursor (MySQLdb.cursors.Cursor): Database cursor

    Returns:
        list: List of tuples containing state information
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    return cursor.fetchall()


def main():
    """
    Main function that orchestrates the database connection,
    state retrieval, and result display.
    """
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = connect_to_db(username, password, database)
        cur = db.cursor()

        states = get_states(cur)

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    main()
