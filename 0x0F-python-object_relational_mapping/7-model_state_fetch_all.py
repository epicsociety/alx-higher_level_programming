#!/usr/bin/python3
'''
module prints state name and id 
'''

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    if len(sys.argv) == 4:

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database))

        '''creates the necessary database schema based on the model'''
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        query = session.query(State).order_by(State.id).all()
        for state in query:
            print('{}: {}'.format(state.id, state.name))

        session.close()
