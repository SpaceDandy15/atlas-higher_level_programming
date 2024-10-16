#!/usr/bin/python3
"""
Start link class to table in database and create table using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server using SQLAlchemy's create_engine function
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
    pool_pre_ping=True)

    # Create the table in the database (if it doesn't exist)
    Base.metadata.create_all(engine)
