#!/usr/bin/python3
"""
This module defines the State class and links it to the MySQL table `states`.
It uses SQLAlchemy's declarative_base() for object-relational mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base to define the base class for the models
Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base and links to MySQL table `states`.
    
    Attributes:
        id (int): Primary key for the state, auto-generated.
        name (string): Name of the state, with a max length of 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
