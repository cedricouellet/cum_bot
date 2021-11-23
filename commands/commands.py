"""
The main command module.
"""

from typing import Union

from utils.file_utils import scrape_all_files

from replies import REPLIES

from .handlers import handle_math_command, handle_joke_command, handle_help_command
from .constants import PREFIX


__reply_mapping = {
    'sale': REPLIES['funny']['sale'],
    'jizz': REPLIES['funny']['jizz'],
    'fuckyou': REPLIES['insults']['fuckyou'],
    'oleg': REPLIES['funny']['oleg'],
    'jew': REPLIES['tags']['eli'],
    'crackhead': REPLIES['tags']['felix'],
    'loser': REPLIES['tags']['cedric']
}


def __code() -> str:
    return scrape_all_files()


def __joke() -> str:
    return handle_joke_command()


def __math(command) -> str:
    return str(handle_math_command(command))


def __usage(sender) -> str:
    return handle_help_command(sender)


def handle_command(command: str, sender: str) -> Union[str, None]:
    """
    Handle a command being made by the user

    Parameters:

    - `{str} command` - The command to be handled

    - `{str} sender` - The user who sent the command

    Returns:

    - `{str|None}` - The response to the command
    """
    if not command.startswith(PREFIX):
        return None

    command = command[1:]

    if command in __reply_mapping:
        return __reply_mapping[command]

    if command.startswith('math'):
        return __math(command)

    if command == 'joke':
        return __joke()

    if command == 'help':
        return __usage(sender)

    if command == 'code':
        try:
            return __code()
        except OSError:
            return REPLIES['other']['unexpectederror']
