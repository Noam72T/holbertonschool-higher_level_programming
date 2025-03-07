#!/usr/bin/python3
"""Module joining 2 tables"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

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

    # Requête pour joindre les tables City et State en utilisant l'attribut
    # de clé étrangère, triée par l'ID de la ville (City.id),
    # et affichage des résultats
    for city, state in session.query(
            City, State).join(State).order_by(City.id.asc()).all():
        # Affiche le nom de l'état et l'ID et le nom de la ville associée
        print(f'{state.name}: ({city.id}) {city.name}')

    # Fermeture de la session après la fin de l'exécution
    session.close()
