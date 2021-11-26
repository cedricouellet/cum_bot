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
    joke = requests.get(f'https://v2.jokeapi.dev/joke/{category.value}').json()
    setup = joke['setup']
    delivery = joke['delivery']

    return setup, delivery, category.value


def __make_giphy_request(search: str, giphy_api_key: str) -> str:
    query_url = f'https://api.giphy.com/v1/gifs/'

    if search is None:
        query_url += f'trending?api_key={giphy_api_key}&limit=1'
    else:
        query_url += f'search?q={search}&api_key={giphy_api_key}&limit=1'

    gif = requests.get(query_url).json()
    url = gif["data"]["url"]

    return url


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


def fetch_gif_by_search(search: str, giphy_api_key: str) -> str:
    try:
        return __make_giphy_request(search, giphy_api_key)
    except requests.exceptions.HTTPError as e:
        raise e
    except: # noqa (for all other errors)
        try: # try one more time
            return __make_giphy_request(search, giphy_api_key)
        except BaseException as e: # if it fails again, raise the error
            raise e
