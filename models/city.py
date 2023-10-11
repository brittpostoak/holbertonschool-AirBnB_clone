#!/usr/bin/python3
"""
Class: City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ City class

    Attributes:
        name (str): City
        state_id (str): State where the city is located
    """
    name = ""
    state_id = ""
