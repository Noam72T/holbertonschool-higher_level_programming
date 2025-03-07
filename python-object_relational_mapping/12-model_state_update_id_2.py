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

    # Recherche du premier état dont l'id est 2
    state = session.query(State).filter(State.id.like(2)).first()

    # Modification du nom de l'état trouvé en 'New Mexico'
    state.name = 'New Mexico'

    # Engagement de la session pour enregistrer le nouvel état
    session.commit()

    # Fermeture de la session après la fin de l'exécution
    session.close()
