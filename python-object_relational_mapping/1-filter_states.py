#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    # Création d'un curseur pour exécuter des requêtes
    cur = db.cursor()

    # récupére les états dont le nom commence par 'N'
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )

    # Affichage des résultats obtenus
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
