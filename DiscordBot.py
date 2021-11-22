import discord
import commands

from time import sleep

USERS = {
    '359068019286212618': 'Cedric',
    '181490764734398464': 'Felix',
    '337754436304896000': 'Eli'
}

GENERAL_CHANNEL = '911471269575290944'
CUMBOT_TAG = '<@912110450676727809>'
AUTHOR_TAG = '<@359068019286212618>'


class DiscordBot:
    """
    CumBot 0.1.0
    """
    def __init__(self, dev: bool):
        """
        Constructor
        
        Parameters:
        - `{bool} dev`: Whether or not this is being called from a development environment.
                        If so, the bot will be quiet when logging in and out.
        """

        self.client = discord.Client()
        self.token = None
        self.dev = dev

        @self.client.event
        async def on_ready():
            channel = self.client.get_channel(int(GENERAL_CHANNEL))
            
            if self.dev == False:
                await channel.send(f"*{CUMBOT_TAG} is here assholes!*")

            print(f'{self.client.user.name} has connected to Discord!')

        @self.client.event
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(f'{member.name}, you\'re my slave now.')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            command = message.content
            
            sender = ""
            try:
                sender = USERS[str(message.author.id)]
            except KeyError:
                sender = message.author.name        

            msg = commands.handle_command(command, sender)
            
            if msg != None:
                try:
                    await self.__send_message(message, msg)
                except BaseException as e:
                    print(e)
                    await self.stop(error=True)

    async def __send_message(self, in_message: discord.Message, out_message: str) -> None:
        """
        Send a message according to the message received

        Parameters:
        - `{discord.Message} in_message`: The message received
        - `{str} out_message`: The message to send
        """
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

    async def run(self, token: str) -> None:
        """
        Run the bot

        Parameters:
        - `{str} token`: The token to use to login to Discord
        """
        self.token = token

        await self.client.start(token)

    async def stop(self, error: bool = False) -> None:
        """
        Shutdown the bot

        Parameters:
        - `{bool} error`: Whether or not the bot is shutting down due to an error
        """
        channel = self.client.get_channel(int(GENERAL_CHANNEL))

        msg = ""
        if error:
            msg = f"*I crashed cause {AUTHOR_TAG} can't code for shit...*"
        else:
            msg = f"*Shutting down cause {AUTHOR_TAG} is gay...*" 

        if self.dev == False:
            await channel.send(msg)
        await self.client.close()