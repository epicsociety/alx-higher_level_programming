#!/usr/bin/python3
""" script prints the first state id's and name """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':

    user, password, db_name = sys.argv[1:]

    # dialect(flavor)+driver(dbAPI)://username:password@host:port/database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    city = City(name="San Francisco")
    state = State(name="California")
    state.cities.append(city)
    session.add(city)
    session.add(state)
    session.commit()
    session.close()
