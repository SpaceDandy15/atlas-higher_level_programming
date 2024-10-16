#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine for connecting to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
    pool_pre_ping=True)

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the name passed as an argument
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
