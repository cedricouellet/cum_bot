from typing import Tuple
import numexpr
import requests


def get_random_joke() -> Tuple[str, str]:
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
        
        return (setup, delivery)
    except:
        # try again if the first request fails
        try:
            joke = requests.get('https://v2.jokeapi.dev/joke/Dark').json()
        
            setup = joke['setup']
            delivery = joke['delivery']
            
            return (setup, delivery)
        except BaseException as e:
            # if the second request fails, raise the exception
            raise e


def calculate_expression(expression: str) -> int:
    """
    Calculate a mathematical expression.

    Parameters:
    - `{str} expression` - The expression to calculate

    Returns:
    - `{str}` - The result of the calculated expression

    Raises:
    - `BaseException` - If there was a problem calculating the expression
    """
    try:
        return numexpr.evaluate(expression)
    except BaseException as e:
        raise e