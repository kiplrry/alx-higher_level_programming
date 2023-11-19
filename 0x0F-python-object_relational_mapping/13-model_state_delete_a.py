#!/usr/bin/python3
"""Querying data from a database using query()"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
        )
    # engine = create_engine(
    # f'mysql+mysqldb://root:pass@localhost:3306/hbtn_0e_6_usa')

    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter(State.name.ilike('%a%'))\
        .delete(synchronize_session='fetch')
    session.commit()
