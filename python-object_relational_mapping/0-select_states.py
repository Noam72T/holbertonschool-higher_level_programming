#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa in ascending order by id.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def list_states():
    """Connect to MySQL database and list all states."""
    if len(sys.argv) != 4:
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to the MySQL database
        with MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database) as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
                for row in cursor.fetchall():
                    print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    list_states()
