#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents BaseModel class all others inherit from"""

    def __init__(self, *args, **kwargs):
        """ Initializes a BaseModel
        Param Args: Args - list of arguments
        kwargs - dictionary of key:value arguments
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time)
                else:
                    self.__dict__[key] = value
    def __str__(self):
        """print/str representation of BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary key/value list of __dict__"""
        list_of_dict = self.__dict__.copy()
        list_of_dict["__class__"] = type(self).__name__
        list_of_dict["created_at"] = list_of_dict["created_at"].isoformat()
        list_of_dict["updated_at"] = list_of_dict["updated_at"].isoformat()
        return list_of_dict