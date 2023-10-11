#!/usr/bin/python3
"""Unittests for class: Base Model"""


import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID


class TestsBaseModel(unittest.TestCase):
    """Unittest for class: Base Model"""
    
    obj = Review()

    def seUp(self):
        """Sets up the Initial"""
        place_id = ""
        user_id = ""
        text = ""

    def test_normal_cases_review(self):
        """Tests for Normal Cases"""
        my_object = Review()
        my_object.name = "AIRBnB"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "AIRBnB")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "Review")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """Tests for Sub Class"""
        self.assertEqual(issubclass(Review, BaseModel), True)
	
    def test_type(self):
        """Tests for type of Object"""
        self.assertEqual(type(self.obj.place_id), str)
        self.assertEqual(type(self.obj.user_id), str)
        self.assertEqual(type(self.obj.text), str)

if __name__ == "__main__":
    unittest.main()
