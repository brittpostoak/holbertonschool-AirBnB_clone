#!/usr/bin/python3
"""Unittests for class: User"""


import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID


class TestsUser(unittest.TestCase):
    """Unittest for class: User"""

    obj = User()

    def setUp(self):
        """Sets up the Initial"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def test_normal_cases_user(self):
        """Tests for Normal Cases"""
        my_object = User()
        my_object.name = "AIRBnB"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "AIRBnB")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "User")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """Tests for Sub Class"""
        self.assertEqual(issubclass(User, BaseModel), True)

    def test_type(self):
        """Tests for type of Object"""
        self.assertEqual(type(self.obj.email), str)
        self.assertEqual(type(self.obj.password), str)
        self.assertEqual(type(self.obj.first_name), str)
        self.assertEqual(type(self.obj.last_name), str)

if __name__ == "__main__":
    unittest.main()
