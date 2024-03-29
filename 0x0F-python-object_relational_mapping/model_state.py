#!/usr/bin/python3
"""file that contains the class definition of a state and an instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class def of a state"""

    __tablename__ = "states"
    id = Column(Integer, primary_key= True, autoincrement=True,nullable=False)
    name = Column(String(128), nullable=False)
