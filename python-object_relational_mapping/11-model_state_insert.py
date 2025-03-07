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

    # Création d'un nouvel objet "State" avec le nom 'Louisiana'
    new_state = State(name='Louisiana')

    # Ajout de l'objet "new_state" à la session
    session.add(new_state)

    # Engagement de la session pour enregistrer le nouvel état
    session.commit()

    # Affichage de l'id du nouvel état ajouté
    print(new_state.id)

    # Fermeture de la session après la fin de l'exécution
    session.close()
