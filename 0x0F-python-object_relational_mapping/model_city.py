#!/usr/bin/python3
'''Creating a class City'''


from sqlalchemy import Integer, String, Column, ForeignKeyConstraint
from model_state import Base


class City(Base):
    '''Class City inheriting from Base'''
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['state_id'], ['states.id']),
    )
