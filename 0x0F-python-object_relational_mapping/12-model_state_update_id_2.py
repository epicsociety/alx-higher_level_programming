#!/usr/bin/python3
""" module searches for a state in the database and display
it's id
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    username, password, database = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        if state.id == 2:
            state.name = "New Mexico"
            break

    session.commit()
    session.close()
