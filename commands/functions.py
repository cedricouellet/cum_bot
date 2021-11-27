"""
Command functions
"""

from typing import Union
from requests.exceptions import HTTPError

from strings import strings
from utils.JokeCategory import JokeCategory
from utils.math import calculate_expression
from utils.joke_requests import fetch_joke
from utils.giphy_requests import fetch_gif


def math(expression: str) -> Union[int, any]:
    """
    Math function

    :param expression: The mathematical expression to calculate
    :return: The result of the expression or an error message
    """
    try:
        return calculate_expression(expression)
    except OverflowError:
        return strings['errors_math']['overflow']
    except SyntaxError:
        return strings['errors_math']['blank']
    except: # noqa (all other errors should default to the same error message)
        return strings['errors_math']['invalid']


def joke(category: str) -> str:
    """
    Joke function

    :param category: The category of the joke
    :return: A joke or error message
    """
    try:
        enum_category = JokeCategory.ANY

        if category is not None:
            for cat in JokeCategory:
                if cat.value.lower() == category.lower():
                    enum_category = cat
                    break

        content = fetch_joke(enum_category)
        setup, delivery, category = content
        return strings['replies']['joke'] + f'Category: {category.upper()}\n\n**{setup}**\n*{delivery}*'
    except HTTPError:
        return strings['errors_joke']['http_error']
    except: # noqa (we want to handle all errors)
        return strings['errors_joke']['invalid']


def gif(search: str = None) -> str:
    """
    Gif function.

    :param search: The search query
    :return: The url to a gif
    """
    try:
        return fetch_gif(search)
    except HTTPError:
        return strings["errors_gif"]["http_error"]
    except IndexError:
        try:
            return fetch_gif()
        except BaseException: # noqa (if no default gif could be fetched, raise it)
            return strings["errors_gif"]["unexpected"]
    except BaseException: # noqa (we want to handle all other errors)
        return strings["errors_gif"]["unexpected"]
