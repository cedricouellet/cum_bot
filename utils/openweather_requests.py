"""
OpenWeather API Requests
"""

from typing import Tuple
from dotenv import load_dotenv
import os
import requests

load_dotenv()
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

OPENWEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/'


def __make_weather_request(city: str) -> Tuple[str, str, str, str, str]:
    """
    Makes an HTTP GET request to the OpenWeather API.

    :param city: The city for which to get the weather
    :return: The weather for a city
    """
    response = requests.get(f'{OPENWEATHER_API_URL}/weather?q={city}&appid={OPENWEATHER_API_KEY}').json()

    main = response["main"]
    weather = response["weather"]

    conditions = str(weather["description"])
    temp = str(main["temp"])
    temp_min = str(main["temp_min"])
    temp_max = str(main["temp_max"])

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
            print(e)
            raise e
