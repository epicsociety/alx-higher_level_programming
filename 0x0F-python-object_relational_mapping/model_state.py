#!/usr/bin/python3
'''
module contain the state class
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
'''Base class, default and imported'''


class State(Base):
    '''state class that inherits from Base'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
