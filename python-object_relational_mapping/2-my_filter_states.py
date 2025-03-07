#!/usr/bin/python3
"""Lists all states where 'name' matches the user input from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    # Exécution de la requête
    cur.execute(
        """SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"""
        .format(argv[4]))

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
