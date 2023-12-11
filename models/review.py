#!/usr/bin/python3
"""
Review class, a subclass of BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel class
    Public cls attri:
        place_id:str will be Place.id
        user_id: will be User.id
        text:str
    """
    place_id = ""
    user_id = ""
    text = ""
