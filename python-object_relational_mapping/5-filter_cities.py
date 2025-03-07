#!/usr/bin/python3
"""Module listing all cities from the state passed in argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    # Création d'un curseur
    cur = db.cursor()

    # Exécution de la requête SQL
    cur.execute(
        """SELECT name
                FROM cities
                 WHERE cities.state_id = (SELECT id
                    FROM states
                    WHERE name = %(state)s)
                ORDER BY cities.id ASC""",
        {"state": argv[4]})
    rows = list(cur.fetchall())

    # Récupération et affichage des résultats
    for i in range(len(rows)):
        rows[i] = str(rows[i][0])
    print(', '.join(rows))

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
