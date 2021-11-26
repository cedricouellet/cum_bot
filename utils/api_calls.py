"""
Functions which make API calls to obtain data.
"""

from typing import Tuple
import requests
from enum import Enum


class JokeCategory(Enum):
    ANY = "any"
    DARK = "dark"
    PROGRAMMER = "programmer"
    MISC = "misc"
    PUN = "pun"
    SPOOKY = "spooky"
    CHRISTMAS = "christmas"


def __make_joke_request(category: JokeCategory) -> Tuple[str, str, str]:
    print(category, category.value)
    joke = requests.get(f'https://v2.jokeapi.dev/joke/{category.value}').json()
    setup = joke['setup']
    delivery = joke['delivery']

    return setup, delivery, category.value


def fetch_joke_by_category(category: JokeCategory = JokeCategory.ANY) -> Tuple[str, str, str]:
    """
    Get a random joke.

    Parameters:

    - `{JokeCategory} category` - The category of the joke (optional)


    Returns:

    - `{str, str, str}` - The setup, delivery and category of the joke

    Raises:

    - `{requests.exceptions.HTTPError}` - If the request fails

    - `{KeyError}` - If the category is invalid
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
