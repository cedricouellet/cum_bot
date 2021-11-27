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
    PROGRAMMER = "programmer"
    MISC = "misc"
    PUN = "pun"
    SPOOKY = "spooky"
    CHRISTMAS = "christmas"
