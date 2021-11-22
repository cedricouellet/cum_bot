import utils
from typing import Union
from self_display import get_bot_code
from requests.exceptions import HTTPError
from replies import reply_dict

PREFIX = '!'

COMMANDS = [
    f'{PREFIX}help : Show this message.',
    f'{PREFIX}code : Display this bot\'s code (first 2000 characters).',
    f'{PREFIX}joke : Tells a random joke.',
    f'{PREFIX}math <expression> : Calculated a mathematical expression',
    f'{PREFIX}sale : ||REDACTED||',
    f'{PREFIX}jizz : ||REDACTED||',
    f'{PREFIX}fuckyou : ||REDACTED||',
    f'{PREFIX}oleg : ||REDACTED||',
    f'{PREFIX}jew : Summon Eli',
    f'{PREFIX}crackhead : Summon Felix',
    f'{PREFIX}loser : Summon Cedric'
]


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

    if command.startswith('math'):
        return str(handle_math_command(command))

    elif command == 'joke':
        return handle_joke_command()

    elif command == 'help':
        return handle_help_command(sender)

    elif command == 'code':
        return f'```{get_bot_code()}```'

    elif command == 'sale':
        return reply_dict['funny'][command]
    
    elif command == 'jizz':
        return reply_dict['funny'][command]
    
    elif command == 'fuckyou':
        return reply_dict['insults'][command]
    
    elif command == 'oleg':
        return reply_dict['funny'][command]

    elif command == 'jew':
        return reply_dict['tags']['eli']

    elif command == 'crackhead':
        return reply_dict['tags']['felix']

    elif command == 'loser':
        return reply_dict['tags']['cedric']


def handle_math_command(command: str) -> str:
    """
    Handle the math command

    Parameters:
    - `{str} command` - The command

    Returns:
    - `{str}` - The result of the command or a comedic error message
    """
    try:
        return utils.calculate_expression(command[5:])
    except OverflowError:
        return reply_dict['math']['overflow']
    except KeyError:
        return reply_dict['math']['keyerror']
    except SyntaxError:
        return reply_dict['math']['blank']


def handle_joke_command() -> str:
    """
    Handle the joke command

    Returns:
    - `{str}` - The joke or a comedic error message
    """
    try:
        (setup, delivery) = utils.get_random_joke()
        return reply_dict['joke']['answer'] + f'**{setup}**\n*{delivery}*'
    except HTTPError:
        return reply_dict['joke']['httperror']


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
