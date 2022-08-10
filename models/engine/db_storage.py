#!/usr/bin/python3
"""module for database storage engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class defines the DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine for the database"""

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session
        all objects depending of the class name"""
        newDict = {}
        classes = {City, State, User, Place, Review, Amenity}

        if cls is None:
            for classe in classes:
                for obj in self.__session.query(classe).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    newDict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                newDict[key] = obj
        return newDict

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))()

    def close(self):
        """close the session"""
        self.__session.close()
