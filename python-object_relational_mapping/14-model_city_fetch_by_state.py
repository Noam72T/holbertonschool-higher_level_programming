#!/usr/bin/python3
"""
Script that prints all City objects from the database.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
