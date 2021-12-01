"""
Journaling functions
"""

import random
import os
import json
JOURNAL_FILE = "journal.json"


def __read_file() -> list:
    """
    Read the journal file.

    :return: The JSON parsed to a list
    """
    with open(JOURNAL_FILE, 'r') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = []

    return data


def __create_file_if_not_exists() -> None:
    """
    Create the journal file if it does not exists.

    Initializes an empty list.
    """
    if not os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, 'w') as f:
            json.dump([], f)


def read_random_entry() -> dict:
    """
    Read a random entry in the diary.

    e.g.
    `entry = {
    "entry": "HelloWorld",
    "author": "John Doe"
    }`

    :return: A random entry
    :raises IndexError: If no entries are found.
    """
    __create_file_if_not_exists()
    entries = __read_file()

    if len(entries) == 0:
        raise IndexError("No entries found.")
    
    return random.choice(entries)


def add_entry(entry: str, author: str) -> bool:
    """
    Add a unique entry to the diary.

    :param entry: The entry to add
    :param author: The author of the entry
    :return: True if the entry was added, or false
             if the entry already exists for that author.
    """
    __create_file_if_not_exists()
    entries = __read_file()

    new_entry = {"entry": entry, "author": author}

    if new_entry in entries:
        return False

    entries.append(new_entry)
    with open(JOURNAL_FILE, 'w') as f:
        json.dump(entries, f)
    return True
