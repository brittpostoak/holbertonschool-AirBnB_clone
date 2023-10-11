#!/usr/bin/python3
"""Defines Review class"""
import models.base_model import BaseModel


class Review(BaseModel):
    """represents review inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
