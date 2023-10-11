#!/usr/bin/python3
"""
Class: User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Creates object: User

    Attributes:
        email (str): User's email
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    # create public class attributes
    # update FileStorage to manage serialization/deserialization of User
    # update console to allow show, create, destroy, update, and all with User
