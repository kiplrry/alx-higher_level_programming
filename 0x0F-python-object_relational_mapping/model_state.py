#!/usr/bin/python3
'''Creating a class State'''
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, CheckConstraint, \
    UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''Class State inheriting from Base'''
    
