#!/usr/bin/python3
"""defines a city model"""

from sqlalchemy import Column, ForeignKey, Interger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """reps a city for a My Sql database"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Interger, ForeignKey("states.id"), nullable=False)
