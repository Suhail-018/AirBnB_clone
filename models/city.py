#!/usr/bin/python3
"""
City class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A subclass of BaseModel class
    Public cls attr:
        state_id:(str) will be State.id
        name:(str)
    """
    state_id = ""
    name = ""
