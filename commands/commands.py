"""
Command-related functions for the bot
"""

from discord.ext.commands import Context, Bot, CommandError
import discord.ext.commands.errors as command_errors
from strings import strings
from commands.handlers import handle_math_command, handle_joke_command, handle_code_command, handle_gif_command


def add_jew_command(bot):
    @bot.command(name="jew", brief=strings["briefs"]["jew"])
    async def jew(ctx: Context):
        await ctx.send(strings["tags"]["eli"])


def add_crackhead_command(bot: Bot):
    @bot.command(name="crackhead", brief=strings["briefs"]["crackhead"])
    async def crackhead(ctx: Context):
        await ctx.send(strings["tags"]["felix"])


def add_loser_command(bot: Bot):
    @bot.command(name="loser", brief=strings["briefs"]["loser"])
    async def loser(ctx: Context):
        await ctx.send(strings["tags"]["cedric"])


def add_oleg_command(bot: Bot):
    @bot.command(name="oleg", brief=strings["briefs"]["oleg"])
    async def oleg(ctx: Context):
        await ctx.send(strings["replies"]["oleg"])


def add_sale_command(bot: Bot):
    @bot.command(name="sale", brief=strings["briefs"]["sale"])
    async def sale(ctx: Context):
        await ctx.send(strings["replies"]["sale"])


def add_jizz_command(bot: Bot):
    @bot.command(name="jizz", brief=strings["briefs"]["jizz"])
    async def jizz(ctx: Context):
        await ctx.send(strings["replies"]["jizz"])


def add_fuckyou_command(bot: Bot):
    @bot.command(name="fuckyou", brief=strings["briefs"]["fuckyou"])
    async def jizz(ctx: Context):
        await ctx.send(strings["replies"]["fuckyou"])


def add_code_command(bot: Bot):
    @bot.command(name="code", brief=strings["briefs"]["code"])
    async def code(ctx: Context):
        await __send_long_message(ctx, handle_code_command())


def add_joke_command(bot: Bot):
    @bot.command(name="joke", brief=strings["briefs"]["joke"], description=strings["descriptions"]["joke"])
    async def joke(ctx: Context, category: str = None):
        await ctx.send(handle_joke_command(category))


def add_gif_command(bot: Bot, discord_api_token: str):
    @bot.command(name="gif", brief=strings["briefs"]["gif"])
    async def gif(ctx: Context, search: str = None):
        await ctx.send(handle_gif_command(search, discord_api_token))


def add_math_command(bot: Bot):
    @bot.command(name="math", brief=strings["briefs"]["math"])
    async def math(ctx: Context, expression: str):
        await ctx.send(handle_math_command(expression))

    @math.error
    async def math_error(ctx: Context, error: CommandError):
        message = "Something went wrong..."
        if isinstance(error, command_errors.MissingRequiredArgument):
            message = strings["errors_math"]["blank"]

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)


async def __send_long_message(ctx: Context, message: str):
    limit = 1994
    i = len(message)
    while i > 0:
        if i > limit:
            await ctx.send(f'```{message[:limit]}```')
            message = message[limit:]
            i -= limit
        else:
            await ctx.channel.send(f'```{message[:i]}```')
            i = 0
