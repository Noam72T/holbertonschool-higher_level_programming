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

    # Création des tables dans la base de données si elles n'existent pas déjà
    Base.metadata.create_all(engine)

    # Ouverture d'une session avec la base de données
    session = Session(engine)

    # Récupère tous les états (State) dont le nom contient la lettre 'a'
    # et triés par leur id
    states = session.query(State).order_by(State.id).filter(
        State.name.like("%a%"))

    # Parcours de chaque état récupéré et affichage de son id et de son nom
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture de la session après la fin de l'exécution
    session.close()
