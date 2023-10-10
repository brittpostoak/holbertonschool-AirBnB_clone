#!/usr/bin/python3
"""Unittests for class: Base Model"""


import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage


class TestsBaseModel(unittest.TestCase):
    """
    Unittest for class: Base Model
    """

    obj = Place()

    def setUp(self):
        """Sets up the Intial"""
        city_id = ""
        user_id= ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def test_normal_cases_place(self):
        """Tests for Normal Cases"""
        my_object = Place()
        my_object.name = "AIRBnB"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "AIRBnB")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "Place")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """Tests for Sub Class"""
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_type(self):
        """Tests for type of Object"""
        self.assertEqual(type(self.obj.city_id), str)
        self.assertEqual(type(self.obj.user_id), str)
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(type(self.obj.description), str)
        self.assertEqual(type(self.obj.number_rooms), int)
        self.assertEqual(type(self.obj.number_bathrooms), int)
        self.assertEqual(type(self.obj.max_guest), int)
        self.assertEqual(type(self.obj.price_by_night), int)
        self.assertEqual(type(self.obj.latitude), float)
        self.assertEqual(type(self.obj.longitude), float)
        self.assertEqual(type(self.obj.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
