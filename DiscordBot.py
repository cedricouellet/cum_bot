import discord
from discord.ext import commands
from discord.ext.commands import command
from commands.commands import handle_command
import commands.bot_commands as botcom

GENERAL_CHANNEL = '912567550209056778'
CUMBOT_TAG = '<@912110450676727809>'
AUTHOR_TAG = '<@359068019286212618>'
USERS = {
    '359068019286212618': 'Cedric',
    '181490764734398464': 'Felix',
    '337754436304896000': 'Eli'
}


class DiscordBot(commands.Bot):
    """
    CumBot 0.1.0
    """
    def __init__(self, dev: bool):
        """
        Constructor
        
        Parameters:

        - `{bool} dev` - Whether or not this is being called from a development environment.

        If so, the bot will be quiet when logging in and out.
        """
        super().__init__(command_prefix='!')
        self.token = None
        self.dev = dev

        botcom.handle_add(self)

    # discord method
    async def on_ready(self):
        """
        Once the bot is online.
        """
        channel = self.get_channel(int(GENERAL_CHANNEL))

        if self.dev is False:
            await channel.send(f"*{CUMBOT_TAG} is here assholes!*")

        print(f'{self.user.name} has connected to Discord!')

    # # discord method
    # async def on_message(self, message: discord.Message):
    #     """
    #     Once a message is received on the current guild/server.
    #
    #     Parameters:
    #
    #     - `{discord.Message} message` - The message that was received.
    #     """
    #     if message.author == self.user:
    #         return
    #
    #     command = message.content
    #
    #     try:
    #         sender = USERS[str(message.author.id)]
    #     except KeyError:
    #         sender = message.author.name
    #
    #     msg = handle_command(command, sender)
    #
    #     if msg is not None:
    #         try:
    #             await self.__send_message(message, msg)
    #         except BaseException as e:
    #             print(e)
    #             await self.stop(error=True)
    #
    async def run(self, token: str) -> None:
        """
        Run the bot

        Parameters:

        - `{str} token` - The token to use to login to Discord
        """
        self.token = token

        await self.start(token)

    async def stop(self, error: bool = False) -> None:
        """
        Shutdown the bot

        Parameters:

        - `{bool} error` - Whether or not the bot is shutting down due to an error
        """
        channel = self.get_channel(int(GENERAL_CHANNEL))

        if error:
            msg = f"*I crashed cause {AUTHOR_TAG} can't code for shit...*"
        else:
            msg = f"*Shutting down cause {AUTHOR_TAG} is gay...*"

        if self.dev is False:
            await channel.send(msg)

        await self.close()

    # discord method
    @staticmethod
    async def on_member_join(member: discord.Member):
        """
        When a member joins

        Parameters:
        
        - `{discord.Member} member` - The member that joined
        """
        await member.create_dm()
        await member.dm_channel.send(f'{member.name}, you\'re my slave now.')

    @staticmethod
    async def __send_message(in_message: discord.Message, out_message: str) -> None:
        if len(out_message) > 2000:
            i = len(out_message)
            while i > 0:
                if i > 2000:
                    await in_message.channel.send(out_message[:2000])
                    out_message = out_message[2000:]
                    i -= 2000
                else:
                    await in_message.channel.send(out_message[:i])
                    i = 0
        else:
            await in_message.channel.send(out_message)
