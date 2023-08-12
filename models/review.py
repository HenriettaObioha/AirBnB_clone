#!/usr/bin/python3
"""This defines the review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review.
    Attributes:
    place_id (str): The place id.
    user_id (str): The user id.
    text (str): Thereview text.
    """

    place_id = ""
    user_id = ""
    text = ""
