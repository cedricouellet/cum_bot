"""
Functions which make API calls to obtain data.
"""


from typing import Tuple
import requests


def fetch_random_joke() -> Tuple[str, str]:
    """
    Get a random joke.

    Returns:
    - `(string, string)` - The setup and delivery of the joke

    Raises:
    - `requests.exceptions.HTTPError` - If the request fails
    """
    try:
        joke = requests.get('https://v2.jokeapi.dev/joke/Dark').json()

        setup = joke['setup']
        delivery = joke['delivery']

        return setup, delivery
    except requests.exceptions.HTTPError:
        # try again if the first request fails
        try:
            joke = requests.get('https://v2.jokeapi.dev/joke/Dark').json()

            setup = joke['setup']
            delivery = joke['delivery']

            return setup, delivery
        except requests.exceptions.HTTPError as e:
            # if the second request fails, raise the exception
            raise e