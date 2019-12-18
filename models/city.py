#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        __tablename__: The table name
        name: input name
        state_id: The state id
    """
    __tablename__ = "cities"
    name = Column(
        String(128), nullable=False
    )
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False,
    )
