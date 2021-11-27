"""
Command-related functions for the bot
"""

from discord.ext.commands import Context, Bot, CommandError
import discord.ext.commands.errors as command_errors
from strings import strings
from commands.functions import math, joke, gif


def on_command_jew(bot):
    @bot.command(name="jew", brief=strings["briefs"]["jew"])
    async def jew_command(ctx: Context):
        await ctx.send(strings["tags"]["eli"])


def on_command_crackhead(bot: Bot):
    @bot.command(name="crackhead", brief=strings["briefs"]["crackhead"])
    async def crackhead_command(ctx: Context):
        await ctx.send(strings["tags"]["felix"])


def on_command_loser(bot: Bot):
    @bot.command(name="loser", brief=strings["briefs"]["loser"])
    async def loser_command(ctx: Context):
        await ctx.send(strings["tags"]["cedric"])


def on_command_oleg(bot: Bot):
    @bot.command(name="oleg", brief=strings["briefs"]["oleg"])
    async def oleg_command(ctx: Context):
        await ctx.send(strings["replies"]["oleg"])


def on_command_sale(bot: Bot):
    @bot.command(name="sale", brief=strings["briefs"]["sale"])
    async def sale_command(ctx: Context):
        await ctx.send(strings["replies"]["sale"])


def on_command_jizz(bot: Bot):
    @bot.command(name="jizz", brief=strings["briefs"]["jizz"])
    async def jizz_command(ctx: Context):
        await ctx.send(strings["replies"]["jizz"])


def on_command_fuckyou(bot: Bot):
    @bot.command(name="fuckyou", brief=strings["briefs"]["fuckyou"])
    async def fuckyou_command(ctx: Context):
        await ctx.send(strings["replies"]["fuckyou"])


def on_command_joke(bot: Bot):
    @bot.command(name="joke", brief=strings["briefs"]["joke"], description=strings["descriptions"]["joke"])
    async def joke_command(ctx: Context, category: str = None):
        await ctx.send(joke(category))


def on_command_gif(bot: Bot):
    @bot.command(name="gif", brief=strings["briefs"]["gif"])
    async def gif_command(ctx: Context, search: str = None):
        await ctx.send(gif(search))


def on_command_math(bot: Bot):
    @bot.command(name="math", brief=strings["briefs"]["math"])
    async def math_command(ctx: Context, expression: str):
        await ctx.send(math(expression))

    @math_command.error
    async def math_error(ctx: Context, error: CommandError):
        message = "Something went wrong..."
        if isinstance(error, command_errors.MissingRequiredArgument):
            message = strings["errors_math"]["blank"]

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)


async def __send_long_message(ctx: Context, message: str, limit: int = 2000):
    """
    Sends a long message

    If the message is longer than a certain limit, it will be sent in chunks

    :param ctx: The context
    :param message: The message to send
    :param limit: The limit of each
    """
    i = len(message)
    while i > 0:
        if i > limit:
            await ctx.send(f'{message[:limit]}')
            message = message[limit:]
            i -= limit
        else:
            await ctx.channel.send(f'{message[:i]}')
            i = 0
