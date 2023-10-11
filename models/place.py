#!/usr/bin/python3
"""
Class: Place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class

    Attributes:
        city_id (str): ID of City
        user_id (str): ID of User
        name (str): Name of place
        description (str): Description
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price by night
        latitude (float): Latitude coordinates
        longitude (float): Longtiude coordinates
        amenity_ids (list of str): List of amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
