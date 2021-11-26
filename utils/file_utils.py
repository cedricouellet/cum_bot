"""
File-related utilities
"""

import os

__DIRS = [
    'commands',
    'utils',
]

__ROOT_FILES = [
    '__main__.py',
    'DiscordBot.py',
    'strings.py'
]


def __get_file_separator() -> str:
    if os.name == 'nt':
        return '\\'
    else:
        return '/'


def __scrape_file(path: str) -> str:
    data = ""
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data += f'{line.strip().replace("@", "")}'

    return data


def scrape_all_files(root_files: [str] = None, dirs: [str] = None) -> str:
    """
    Scrapes all selected files and directories in the bot's code
    (starting from root folder)

    Includes:
        Files:
            - ./main.py
            - ./DiscordBot.py
            - ./strings.py
        Directories:
            - /commands/
            - /utils/

    Returns:

    - `{str}` - The contents of all selected files
    """
    file_separator = __get_file_separator()

    if root_files is None:
        root_files = __ROOT_FILES

    if dirs is None:
        dirs = __DIRS

    data = ""

    # Root files first
    for file in root_files:
        data += __scrape_file(file)

    # Directories second
    # non-recursive
    for folder in dirs:
        files = os.listdir(folder)
        for file in files:
            if not file.startswith('__'):
                cwd = os.getcwd() + file_separator + folder + file_separator
                data += __scrape_file(cwd + file)
    return data
