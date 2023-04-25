#!/usr/bin/python3
""" script prints the first state id's and name """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

 """ db_flavor+db_connection://user:password@localhost/db_name """

user, password, db_name = sys.argv[1:]

engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(user, password, db_name),
                       pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

first_state = session.query(State).order_by(State.id).first()

if first_state:

    print("{} {}".format(first_state.id, first_state.name))
else:
    print("Nothing")

session.close()
