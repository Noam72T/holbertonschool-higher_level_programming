#!/usr/bin/python3
import sys
import argv
import MySQLdb
"""Function List all states"""

if __name__ == '__main__':
    """Connection to database"""
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchAll()

    for row in rows:
        print(row)
