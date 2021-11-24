"""
Functions which make API calls to obtain data.
"""

from typing import Tuple
import requests


def __make_joke_request(category: str) -> Tuple[str, str, str]:
    joke = requests.get(f'https://v2.jokeapi.dev/joke/{category}').json()
    setup = joke['setup']
    delivery = joke['delivery']
    joke_type = joke['type']

    return setup, delivery, joke_type


def fetch_random_joke(category: str = "Any") -> Tuple[str, str, str]:
    """
    Get a random joke.

    Parameters:

    - `{str?} category` - The category of the joke (optional)


    Returns:

    - `{str, str, str}` - The setup, delivery and type of the joke

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
