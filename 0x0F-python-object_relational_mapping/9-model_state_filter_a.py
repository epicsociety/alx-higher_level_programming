#!/usr/bin/python3
""" module has script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa"""

import sys
import sqlalchemy import create_engine()
from model_state import Base, State

if __name__ == "if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # db_flavor+db_connector://user:password@localhost/database_nameengine
    engine  = create_engine("mysql+mysqldb)://{}:{}@localhost:3306/{}"\
            .format(mysql_username, mysql_password, datbase_name))

            Session = sessionmaker(bind=engine)
            session = Session()

            display = session.query("states").order_by(state.id).first()


            for i in display:

                print("{}:{}":display[0], display[1])

                session.close()
