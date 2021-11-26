"""
Command handlers
"""


from typing import Union
from requests.exceptions import HTTPError

from utils.math import calculate_expression
from utils.api_calls import fetch_joke_by_category
from utils.file_utils import scrape_all_files

from strings import strings
from utils.api_calls import JokeCategory


def handle_code_command() -> str:
    """
    Handle the code command

    Returns:

    - `{str}` - The result of the command or a comedic error message
    """
    try:
        return scrape_all_files()
    except OSError:
        return strings['errors_code']['os_error']


def handle_math_command(argument: str) -> Union[int, any]:
    """
    Handle the math command

    Parameters:

    - `{str} argument` - The argument

    Returns:

    - `{str}` - The result of the command or a comedic error message
    """
    try:
        return calculate_expression(argument)
    except OverflowError:
        return strings['errors_math']['overflow']
    except SyntaxError:
        return strings['errors_math']['blank']
    except: # noqa (all other errors should default to the same error message)
        return strings['errors_math']['invalid']


def handle_joke_command(argument: str) -> str:
    """
    Handle the joke command

    Parameters:

    - `{str}` - The argument

    Returns:

    - `{str}` - The joke or a comedic error message
    """

    try:
        enum_category = JokeCategory.ANY

        if argument is not None:
            for cat in JokeCategory:
                if cat.value.lower() == argument.lower():
                    enum_category = cat
                    break

        content = fetch_joke_by_category(enum_category)
        setup, delivery, category = content
        return strings['replies']['joke'] + f'Category: {category.upper()}\n\n**{setup}**\n*{delivery}*'
    except HTTPError:
        return strings['errors_joke']['http_error']
    except: # noqa (we want to handle all errors)
        return strings['errors_joke']['invalid']
