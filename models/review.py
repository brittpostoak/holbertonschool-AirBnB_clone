#!/usr/bin/python3
"""
Class: Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class

    Attributes:
        place_id (str): Place ID review
        user_id (str): User ID review
        text (str): Text of review
    """
    place_id = ""
    user_id = ""
    text = ""
