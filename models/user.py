#!/usr/bin/python3
"""This defines the user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """This represents a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
