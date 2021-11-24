"""
Command handlers
"""


from typing import Union
from requests.exceptions import HTTPError

from utils.math import calculate_expression
from utils.api_calls import fetch_joke_by_category

from replies import REPLIES
from .constants import COMMANDS


def handle_math_command(command: str) -> Union[int, any]:
    """
    Handle the math command

    Parameters:

    - `{str} command` - The command

    Returns:

    - `{str}` - The result of the command or a comedic error message
    """
    try:
        return calculate_expression(command[5:].strip())
    except OverflowError:
        return REPLIES['math']['overflow']
    except SyntaxError:
        return REPLIES['math']['blank']
    except: # noqa (all other errors should default to the same error message)
        return REPLIES['math']['invalid']


def handle_joke_command(command) -> str:
    """
    Handle the joke command

    Parameters:

    - `{str}` - The

    Returns:

    - `{str}` - The joke or a comedic error message
    """

    category = command[5:].strip()

    try:
        if category == "":
            content = fetch_joke_by_category()
        else:
            content = fetch_joke_by_category(category)

        setup, delivery, category = content
        return REPLIES['joke']['answer'] + f'Category: {category.upper()}\n\n**{setup}**\n*{delivery}*'
    except HTTPError:
        return REPLIES['joke']['httperror']
    except: # noqa (we want to handle all errors)
        return REPLIES['joke']['invalid']


def handle_help_command(sender: str) -> str:
    """
    Handle the help command

    Returns:

    - `{str}` - The help message
    """
    header = f'''
    **CumBot v0.1.0**

    Here {sender}, these are the available commands asshole:
    '''

    commands_str = '\n- ' + '\n- '.join(COMMANDS)
    return header + commands_str
