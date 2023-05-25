#!/usr/bin/python3
""" module has script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username, password, db_name = sys.argv[1:]

    # dialect(flavor)+driver(dbAPI)://username:password@host:port/database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if 'a' in state.name.lower():
            print("{}: {}".format(state.id, state.name))

    session.close()
