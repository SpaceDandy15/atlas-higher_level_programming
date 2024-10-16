#!/usr/bin/python3
"""
This script fetches all City objects from the database hbtn_0e_14_usa
and prints them along with their corresponding State names.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query all cities and their associated states
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
