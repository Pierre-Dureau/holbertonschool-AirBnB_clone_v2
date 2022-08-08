#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
    else:
        @property
        def reviews(self):
            """returns the list of Review instances with place_id
            equals to the current Place.id => It will be the FileStorage
            relationship between Place and Review"""
            reviews = []

            for value in models.storage.all(Review).values():
                if value.place_id == self.id:
                    reviews.append(value)
            return reviews
