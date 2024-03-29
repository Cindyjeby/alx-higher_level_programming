#!/usr/bin/python3
"""creates the state california with the city san francisco from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=true)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bing=engine)
    session = SEssion()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
