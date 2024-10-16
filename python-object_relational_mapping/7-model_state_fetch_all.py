#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
It connects to the MySQL database using SQLAlchemy and retrieves data from the states table.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine for connecting to MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
    pool_pre_ping=True)

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, sorted by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results in the format "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
