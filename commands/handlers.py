"""
Command handlers
"""


from typing import Union
from requests.exceptions import HTTPError

from utils.math import calculate_expression
from utils.api_calls import fetch_random_joke

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
        return calculate_expression(command[5:])
    except OverflowError:
        return REPLIES['math']['overflow']
    except SyntaxError:
        return REPLIES['math']['blank']
    except: # noqa (all other errors should default to the same error message)
        return REPLIES['math']['invalid']


def handle_joke_command() -> str:
    """
    Handle the joke command

    Returns:

    - `{str}` - The joke or a comedic error message
    """
    try:
        setup, delivery = fetch_random_joke()
        return REPLIES['joke']['answer'] + f'**{setup}**\n*{delivery}*'
    except HTTPError:
        return REPLIES['joke']['httperror']


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
