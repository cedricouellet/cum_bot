"""
Contains the DiscordBot class
"""

import discord
from discord.ext.commands import Bot
from typing import List, Callable

GENERAL_CHANNEL = '912567550209056778'
CUMBOT_TAG = '<@912110450676727809>'
AUTHOR_TAG = '<@359068019286212618>'

class DiscordBot(Bot):
    """
    CumBot 0.1.0
    """
    def __init__(self, is_dev: bool, command_listeners: List[Callable[[Bot], None]]):
        """
        Constructor

        :param is_dev: Whether or not this is being called from a development environment.
                    If so, the bot will be quiet when logging in and out

        :param command_listeners: The list of command listeners
        """
        super().__init__(command_prefix='!')
        self.discord_token = None
        self.dev = is_dev

        for on_command in command_listeners:
            on_command(self)

    async def on_ready(self):
        """
        Once the bot is online.
        """
        channel = self.get_channel(int(GENERAL_CHANNEL))
        e = self.owner_id
        print(e)
        if self.dev is False:
            await channel.send(f"*{CUMBOT_TAG} is here assholes!*")

        print(f'{self.user.name} has connected to Discord!')

    async def run(self, discord_token: str) -> None:
        """
        Run the bot

        :param discord_token: The token to use to login to Discord
        """
        await self.start(discord_token)

    async def stop(self, is_error: bool = False) -> None:
        """
        Shutdown the bot

        :param is_error: Whether or not the bot is shutting down due to an error
        """
        channel = self.get_channel(int(GENERAL_CHANNEL))

        if is_error:
            msg = f"*I crashed cause {AUTHOR_TAG} can't code for shit...*"
        else:
            msg = f"*Shutting down cause {AUTHOR_TAG} is gay...*"

        if self.dev is False:
            await channel.send(msg)

        await self.close()

    @staticmethod
    async def on_member_join(member: discord.Member):
        """
        When a member joins

        :param member: The member that joined
        """
        await member.create_dm()
        await member.dm_channel.send(f'{member.name}, you\'re my slave now.')
