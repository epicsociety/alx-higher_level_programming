#!/usr/bin/python3
""" script prints the first state id's and name """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == '__main__':

    user, password, db_name = sys.argv[1:]

    # dialect(flavor)+driver(dbAPI)://username:password@host:port/database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name).join(
            State).filter(City.state_id == State.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.close()
