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

    # Recherche du premier état dont le nom correspond exactement
    # à l'argument passé en ligne de commande
    state = session.query(State).filter(State.name.like(argv[4])).first()

    # Vérifie si aucun état n'a été trouvé et affiche un message approprié
    if state is None:
        # Affiche "Not found" si aucun état n'est trouvé
        print('Not found')
    else:
        # Affiche l'id de l'état trouvé
        print("{}".format(state.id))

    # Fermeture de la session après la fin de l'exécution
    session.close()
