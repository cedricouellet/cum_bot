"""
Giphy API Requests
"""

import requests
import os

GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')
GIPHY_API_URL = 'https://api.giphy.com/v1/gifs'


def __make_giphy_request(search: str = None) -> str:
    """
    Makes an HTTP GET request to the giphy API.

    :param search: The search query
    :return: A gif according to the search, or a random gif
    """
    query_url = f'{GIPHY_API_URL}/search?q={search}&api_key={GIPHY_API_KEY}&limit=1'
    if search is None:
        query_url = f'{GIPHY_API_URL}/random?api_key={GIPHY_API_KEY}&limit=1'

    data = requests.get(query_url).json()["data"]
    if search is not None:
        data = data[0]

    return data["url"]


def fetch_gif(search: str = None) -> str:
    """
    Fetch a gif by a search.
    If no search is provided, it will default to a trending gif.

    :param search: The search query
    :return: The url to a gif
    :raise requests.exceptions.HTTPError: If the HTTP request fails
    :raise BaseException: If any other error occurs
    """
    try:
        return __make_giphy_request(search)
    except requests.exceptions.HTTPError as e:
        raise e
    except: # noqa (for all other errors)
        try:  # try one more time
            return __make_giphy_request(search)
        except BaseException as e:  # if it fails again, raise the error
            raise e
