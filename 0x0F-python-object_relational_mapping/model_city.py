#!/usr/bin/python3
'''
module contain the state class
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    '''state class that inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
