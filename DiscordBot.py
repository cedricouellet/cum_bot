import discord
from discord.ext.commands import Bot
from commands import commands


GENERAL_CHANNEL = '912567550209056778'
CUMBOT_TAG = '<@912110450676727809>'
AUTHOR_TAG = '<@359068019286212618>'
USERS = {
    '359068019286212618': 'Cedric',
    '181490764734398464': 'Felix',
    '337754436304896000': 'Eli'
}


class DiscordBot(Bot):
    """
    CumBot 0.1.0
    """
    def __init__(self, is_dev: bool):
        """
        Constructor

        :param is_dev: Whether or not this is being called from a development environment.
                    If so, the bot will be quiet when logging in and out.
        """
        super().__init__(command_prefix='!')
        self.discord_token = None
        self.dev = is_dev

        listeners = []
        listeners += 'e'

        print(listeners)

        commands.on_command_jew(self)
        commands.on_command_jizz(self)
        commands.on_command_joke(self)
        commands.on_command_math(self)
        commands.on_command_loser(self)
        commands.on_command_fuckyou(self)
        commands.on_command_sale(self)
        commands.on_command_crackhead(self)
        commands.on_command_oleg(self)
        commands.on_command_gif(self)

    async def on_ready(self):
        """
        Once the bot is online.
        """
        channel = self.get_channel(int(GENERAL_CHANNEL))

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
