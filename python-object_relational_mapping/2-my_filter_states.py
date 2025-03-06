#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor
    cur = db.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.aragv[4],)
    )
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
