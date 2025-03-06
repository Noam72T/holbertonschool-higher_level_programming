#!/usr/bin/python3
"""Module listing all states matching a name from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    # Exécution de la requête avec un paramètre de manière sécurisée
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (argv[4],)
    )

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()

