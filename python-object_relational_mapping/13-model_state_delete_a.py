#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Création d'une instance de moteur SQLAlchemy
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )

    # Création des tables dans la base de données
    Base.metadata.create_all(engine)

    # Ouverture d'une session avec la base de données
    session = Session(engine)

    # Parcours des états dont le nom contient la lettre 'a'
    for state in session.query(State).filter(State.name.contains('a')):
        # Suppression de chaque état trouvé
        session.delete(state)

    # Engagement de la session pour enregistrer les suppressions
    session.commit()

    # Fermeture de la session après la fin de l'exécution
    session.close()
