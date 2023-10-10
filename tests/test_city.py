#!/usr/bin/python3
"""
Unittests for class: Base Model
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage


class TestsCity(unittest.TestCase):
    
    obj = City()

    def setUp(self):
        """Sets up the Initial"""
        name = ""
        state_id = ""

    def test_normal(self):
        """Tests for Normal Case"""
        my_object = City()
        my_object.name = "AIRBnB"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "AIRBnB")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "City")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """Tests for Sub Class"""
        self.assertEqual(issubclass(City, BaseModel), True)
    
    def test_type(self):
        """Tests for type of Object"""
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(type(self.obj.state_id), str)
	

if __name__ == "__main__":
    unittest.main()
