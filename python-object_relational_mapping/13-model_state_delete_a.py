#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing the letter 'a' and delete them
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
