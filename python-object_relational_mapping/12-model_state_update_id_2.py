#!/usr/bin/python3
"""
Script that changes the name of a State object from the database.
"""
import sys
from model_state import Base, State
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

    # Query state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update state name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
