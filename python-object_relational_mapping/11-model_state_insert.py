#!/usr/bin/python3
"""
This script adds a new State object 'Louisiana' to the database hbtn_0e_6_usa
and prints the new state's id after creation.
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

    # Create a new State object for 'Louisiana'
    new_state = State(name='Louisiana')

    # Add the new state to the session and commit to the database
    session.add(new_state)
    session.commit()

    # Print the id of the newly added state
    print(new_state.id)

    # Close the session
    session.close()
