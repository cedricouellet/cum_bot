"""
Functions which make API calls to obtain data.
"""


from typing import Tuple
import requests


def fetch_random_joke(category: str = "Any") -> Tuple[str, str]:
    """
    Get a random joke.

    Parameters:

    - `{str?} category` - The category of the joke (optional)


    Returns:

    - `{str, str}` - The setup and delivery of the joke

    Raises:

    - `{requests.exceptions.HTTPError}` - If the request fails

    - `{KeyError}` - If the category is invalid
    """
    try:
        joke = requests.get(f'https://v2.jokeapi.dev/joke/{category}').json()

        setup = joke['setup']
        delivery = joke['delivery']

        return setup, delivery
    except TypeError:
        raise KeyError()
    except requests.exceptions.HTTPError as e:
        raise e
