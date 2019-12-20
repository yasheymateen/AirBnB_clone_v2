#!/usr/bin/python3
"""This is the place class"""
import os
import models
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
from models.base_model import BaseModel, Base
from models.review import Review
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(
        String(60), ForeignKey("cities.id"), nullable=False
    )
    user_id = Column(
        String(60), ForeignKey("users.id"), nullable=False
    )
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(
        Integer, nullable=False, default=0
    )
    number_bathrooms = Column(
        Integer, nullable=False, default=0
    )
    max_guest = Column(
        Integer, nullable=False, default=0
    )
    price_by_night = Column(
        Integer, nullable=False, default=0
    )
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete, delete-orphan"
        )
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False
        )
    else:
        @property
        def reviews(self):
            """ Getter for reviews. """
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return(reviews_list)

        @property
        def amenities(self):
            """Getter for amenities."""
            amenities_list = []
            for k, v in models.storage.all(models.amenity.Amenity).items():
                if k.split('.')[1] in self.amenity_ids:
                    amenities_list.append(v)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Adds an Amenity.id to the attribute amenity_ids"""
            if type(obj) == models.amenity.Amenity:
                self.amenity_ids.append(obj.id)
