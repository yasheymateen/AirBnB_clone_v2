#!/usr/bin/python3
"""This is the state class"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: The table name
        name: input name
    """
    __tablename__ = "states"
    name = Column(
        String(128), nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan"
        )
    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """Getter for cities."""
            cities_list = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
