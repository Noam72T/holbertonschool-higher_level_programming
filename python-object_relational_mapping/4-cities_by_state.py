#!/usr/bin/python3
"""Module listing all cities from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    # Création d'un curseur
    cur = db.cursor()

    # Exécution de la requête SQL
    cur.execute(
        """SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    rows = cur.fetchall()

    # Récupération et affichage des résultats
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
