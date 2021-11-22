BOT_FILENAME = "bot.py"
UTILS_FILENAME = "utils.py"
COMMANDS_FILENAME = "commands.py"
REPLIES_FILENAME = "replies.py"
DISCORD_BOT_FILENAME = "DiscordBot.py"

def get_file_content(filename) -> str:
    """
    Get the file contents of a file

    Parameters:
    - `{str} filename`: The name of the file to get the contents of

    Returns:
    - `{str}`: The contents of the file
    """
    with open(filename, "r") as f:
        return f.read()


def get_bot_code() -> str:
    """
    Gets all the code that powers the bot

    Returns:
    - `{str}`: The code that powers the bot
    """
    return get_file_content(BOT_FILENAME) + \
        get_file_content(DISCORD_BOT_FILENAME) + \
        get_file_content(COMMANDS_FILENAME) + \
        get_file_content(REPLIES_FILENAME) + \
        get_file_content(UTILS_FILENAME) 