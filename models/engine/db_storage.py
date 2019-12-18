#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class queries a mySQL database with instance objects
    Attributes:
        __engine: engine linked to the MySQL database
        __session: the current database session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instance."""
        url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')
        )
        self.__engine = create_engine(url, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session for all objects of a class
        Return:
            returns a dictionary of queried objects
        """
        queried_objs = {}
        if cls is None:
            objs = []
            classes = [State, City, User, Place]
            for c in classes:
                results = self.__session.query(c).all()
                objs.extend(results)
        else:
            objs = self.__session.query(cls).all()
        for obj in objs:
            key = obj.__class__.__name__ + "." + obj.id
            queried_objs[key] = obj
        return queried_objs

    def new(self, obj):
        """Adds an object to the current database session
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()
