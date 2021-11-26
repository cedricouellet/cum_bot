"""
Command-related functions for the bot
"""

from discord.ext.commands import Context, Bot
from strings import strings
from commands.handlers import handle_math_command, handle_joke_command, handle_code_command


def init(bot: Bot):
    """
    Initialise the bot

    Parameters:

    - `{discord.commands.Bot} bot` - The bot for which to initialize commands

    """
    __add_joke_command(bot)
    __add_math_command(bot)
    __add_code_command(bot)
    __add_sale_command(bot)
    __add_jizz_command(bot)
    __add_fuckyou_command(bot)
    __add_oleg_command(bot)
    __add_jew_command(bot)
    __add_crackhead_command(bot)
    __add_loser_command(bot)


def __add_jew_command(bot):
    @bot.command(name="jew", brief=strings["briefs"]["jew"])
    async def jew(ctx: Context):
        await ctx.send(strings["tags"]["eli"])


def __add_crackhead_command(bot: Bot):
    @bot.command(name="crackhead", brief=strings["briefs"]["crackhead"])
    async def crackhead(ctx: Context):
        await ctx.send(strings["tags"]["felix"])


def __add_loser_command(bot: Bot):
    @bot.command(name="loser", brief=strings["briefs"]["loser"])
    async def loser(ctx: Context):
        await ctx.send(strings["tags"]["cedric"])


def __add_oleg_command(bot: Bot):
    @bot.command(name="oleg", brief=strings["briefs"]["oleg"])
    async def oleg(ctx: Context):
        await ctx.send(strings["replies"]["oleg"])


def __add_sale_command(bot: Bot):
    @bot.command(name="sale", brief=strings["briefs"]["sale"])
    async def sale(ctx: Context):
        await ctx.send(strings["replies"]["sale"])


def __add_jizz_command(bot: Bot):
    @bot.command(name="jizz", brief=strings["briefs"]["jizz"])
    async def jizz(ctx: Context):
        await ctx.send(strings["replies"]["jizz"])


def __add_fuckyou_command(bot: Bot):
    @bot.command(name="fuckyou", brief=strings["briefs"]["fuckyou"])
    async def jizz(ctx: Context):
        await ctx.send(strings["replies"]["fuckyou"])


def __add_code_command(bot: Bot):
    @bot.command(name="code", brief=strings["briefs"]["code"])
    async def code(ctx: Context):
        await __send_long_message(ctx, handle_code_command())


def __add_joke_command(bot: Bot):
    @bot.command(name="joke", brief=strings["briefs"]["joke"], description=strings["descriptions"]["joke"])
    async def joke(ctx: Context, category: str = None):
        await ctx.send(handle_joke_command(category))


def __add_math_command(bot: Bot):
    @bot.command(name="math", brief=strings["briefs"]["math"])
    async def math(ctx: Context, expression: str):
        await ctx.send(handle_math_command(expression))


async def __send_long_message(ctx: Context, message: str):
    limit = 4000
    i = len(message)
    while i > 0:
        if i > limit:
            await ctx.send(message[:limit])
            message = message[limit:]
            i -= limit
        else:
            await ctx.channel.send(message[:i])
            i = 0
