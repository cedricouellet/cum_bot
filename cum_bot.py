"""
Contains the DiscordBot class
"""

import discord
from discord.ext.commands import Bot
from typing import List, Callable

AUTHOR_TAG = '<@359068019286212618>'


class CumBot(Bot):
    """
    CumBot 0.1.0
    """
    def __init__(self, is_dev: bool, command_listeners: List[Callable[[Bot], None]], bot_home_channel: str):
        """
        Initialize an instance of the CumBot

        :param is_dev: Whether or not this is being called from a development environment.
                    If so, the bot will be quiet when logging in and out
        :param command_listeners: The list of command listeners
        :param bot_home_channel: The home channel of the bot.
        """
        super().__init__(command_prefix='!')
        self.discord_token = None
        self.dev = is_dev
        self.bot_home_channel = bot_home_channel

        for on_command in command_listeners:
            on_command(self)

    async def on_ready(self):
        """
        Once the bot is online.
        """
        if self.dev is True:
            channel = self.get_home_channel()
            await channel.send(f"<@{self.user.id}> is here assholes!")

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
        channel = self.get_home_channel()

        guilds = await self.fetch_guilds(limit=100).flatten()
        for guild in guilds:
            print(guild.owner_id.__int__())

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

    def get_home_channel(self) -> any:
        """
        Get the bot's home channel

        :return: The bot's home channel
        """
        for channel in self.get_all_channels():
            if channel.name == self.bot_home_channel:
                return channel
        return None
