#!/usr/bin/python3
"""This is the place class"""
import os
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
    """
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
            Getter for reviews.
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return(reviews_list)
            """

    """ Yash's Test Addition """
    @property
    def reviews(self):
        review_instances = []
        objects = storage.all()
        for k, v in objects.items():
            class_name = k.split(".")[0]
            if class_name == "Review":
                if v["place_id"] == self.id:
                    review_instances.append(v)
        return review_instances

    @property
    def amenities(self):
        amenity_instances = []
        objects = storage.all()
        for k, v in objects.items():
            class_name, instance_id = k.split(".")
            if class_name == "Amenity":
                if (v["place_id"] == self.id and
                        instance_id in self.amenity_ids):
                    amenity_instances.append(v)
        return amenity_instances

    @amenities.setter
    def amenities(self, obj):
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review',
                cascade='all, delete',
                backref='place'
            )
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False,
                backref='place'
            )
