"""
Joke API Requests
"""

from typing import Tuple
import requests

from utils.JokeCategory import JokeCategory


JOKE_API_URL = 'https://v2.jokeapi.dev/joke'


def __make_joke_request(category: JokeCategory) -> Tuple[str, str, str]:
    joke = requests.get(f'{JOKE_API_URL}/{category.value}').json()
    return joke["setup"], joke["delivery"], joke["category"]


def fetch_joke(category: JokeCategory = JokeCategory.ANY) -> Tuple[str, str, str]:
    """
    Get a joke by its category.

    If no category is chosen, any joke will be returned.

    :param category: The category of the joke (optional)
    :return: The setup, delivery and category of the joke
    :raise requests.exceptions.HTTPError: If the HTTP request fails
    :raise BaseException: If any other error occurs
    """
    try:
        return __make_joke_request(category)
    except requests.exceptions.HTTPError as e:
        raise e
    except:  # noqa (for all other errors)
        try:  # try one more time
            return __make_joke_request(category)
        except BaseException as e:  # if it fails again, raise the error
            raise e
