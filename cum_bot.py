"""
Contains the DiscordBot class
"""

import discord
from discord.ext.commands import Bot
from typing import List, Callable
from logs.loggers import write_log


class CumBot(Bot):
    """
    CumBot 0.4.1
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
        self.discord_token: str
        self.dev = is_dev
        self.bot_home_channel = bot_home_channel

        for on_command in command_listeners:
            on_command(self)

    async def on_ready(self):
        """
        Once the bot is online.
        """
        write_log('status: ready')

        message = f"<@{self.user.id}> Status: **booting**"
        print(message)

        if self.dev is False:
            channel = self.get_home_channel()
            await channel.send(message)

    async def run(self, discord_token: str) -> None:
        """
        Run the bot

        :param discord_token: The token to use to login to Discord
        """
        write_log('status: booting')
        await self.start(discord_token)

    async def stop(self, is_error: bool = False) -> None:
        """
        Shutdown the bot

        :param is_error: Whether or not the bot is shutting down due to an error
        """
        channel = self.get_home_channel()

        msg = f"<@{self.user.id}> Status: "
        if is_error:
            msg += "**crashing**"
            write_log('status: crashing')
        else:
            msg += "**shutting down**"
            write_log('status: shutting down')

        print(msg)

        if self.dev is False:
            await channel.send(msg)

        await self.close()

    @staticmethod
    async def on_member_join(member: discord.Member):
        """
        When a member joins

        :param member: The member that joined
        """
        write_log(f'member join: {member}')

        await member.create_dm()
        await member.dm_channel.send(f'{member}, kindly proceed to erase yourself from this world.')

    def get_home_channel(self) -> any:
        """
        Get the bot's home channel

        :return: The bot's home channel
        """
        for channel in self.get_all_channels():
            if channel.name == self.bot_home_channel:
                write_log(f'home channel set: {channel}')
                return channel
        return None
