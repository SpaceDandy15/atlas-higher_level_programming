#!/usr/bin/python3
"""
This script updates the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine for connecting to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
    pool_pre_ping=True)

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object where id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the state's name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
