"""
Contains the JokeCategory enum
"""

from enum import Enum


class JokeCategory(Enum):
    """
    The categories for a joke
    """
    ANY = "any"
    DARK = "dark"
    PROGRAMMING = "programming"
    MISC = "misc"
    PUN = "pun"
    SPOOKY = "spooky"
    CHRISTMAS = "christmas"
