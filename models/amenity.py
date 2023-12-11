#!/usr/bin/python3
"""
Amenity class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A subclass of BaseModel class
    Public cls attribute:
        name: (str)
    """
    name = ""
