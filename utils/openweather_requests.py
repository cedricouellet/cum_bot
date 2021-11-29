"""
OpenWeather API Requests
"""

from typing import Tuple
import requests


OPENWEATHER_API_URL = 'https://api.openweather'


def __make_weather_request(city: str) -> Tuple[str, str, str, str, str]:
    """
    Makes an HTTP GET request to the OpenWeather API.

    :param city: The city for which to get the weather
    :return: The weather for a city
    """
    # TODO
    response = requests.get(f'{OPENWEATHER_API_URL}/{city}').json()
    conditions: str = ""
    temp: str = ""
    temp_min: str = ""
    temp_max: str = ""

    return city, conditions, temp, temp_min, temp_max


def fetch_weather(city: str) -> Tuple[str, str, str, str, str]:
    """
    Get weather for a city.

    :param city: The city for which to get the joke
    :return: The city, conditions, current temp, min temp and max temp
    :raise requests.exceptions.HTTPError: If the HTTP request fails
    :raise BaseException: If any other error occurs
    """
    try:
        return __make_weather_request(city)
    except requests.exceptions.HTTPError as e:
        raise e
    except:  # noqa (for all other errors)
        try:  # try one more time
            return __make_weather_request(city)
        except BaseException as e:  # if it fails again, raise the error
            raise e
