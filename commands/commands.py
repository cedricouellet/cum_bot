"""
Listeners for commands
"""
from discord.ext.commands import Context, Bot, CommandError, has_permissions
import discord.ext.commands.errors as command_errors

from utils.logging import write_log
from commands import \
    functions as fn, \
    briefs as briefs, \
    descriptions as desc, \
    error_messages as err


def on_command_diary(bot: Bot) -> None:
    """
    The command listener for the diary command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="diary", briefs=briefs.diary, description=desc.diary)
    async def diary_command(ctx: Context, *, entry: str = None) -> None:
        __log_command(ctx, 'diary', entry)

        author_name = ctx.message.author.name
        result, delete = fn.diary(entry, author_name)

        if delete:
            delete_after = 0
        else:
            delete_after = None

        await __send_message(ctx, result, delete_after=delete_after)

        if delete:
            await ctx.message.delete(delay=0)


def on_command_future(bot: Bot) -> None:
    """
    The command listener for the future command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="future", briefs=briefs.future, description=desc.future)
    async def future_command(ctx: Context) -> None:
        __log_command(ctx, 'future')
        await __send_message(ctx, fn.future())


def on_command_jew(bot: Bot) -> None:
    """
    The command listener for the jew command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="jew", brief=briefs.jew, description=desc.jew)
    async def jew_command(ctx: Context) -> None:
        __log_command(ctx, 'jew')
        await __send_message(ctx, fn.jew())


def on_command_crackhead(bot: Bot) -> None:
    """
    The command listener for the crackhead command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="crackhead", brief=briefs.crackhead, description=desc.crackhead)
    async def crackhead_command(ctx: Context) -> None:
        __log_command(ctx, 'crackhead')
        await __send_message(ctx, fn.crackhead())


def on_command_loser(bot: Bot) -> None:
    """
    The command listener for the loser command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="loser", brief=briefs.loser, description=desc.loser)
    async def loser_command(ctx: Context) -> None:
        __log_command(ctx, 'loser')
        await __send_message(ctx, fn.loser())


def on_command_oleg(bot: Bot) -> None:
    """
    The command listener for the oleg command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="oleg", brief=briefs.oleg, description=desc.oleg)
    async def oleg_command(ctx: Context) -> None:
        __log_command(ctx, 'oleg')
        await __send_message(ctx, fn.oleg())


def on_command_sale(bot: Bot) -> None:
    """
    The command listener for the sale command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="sale", brief=briefs.sale, description=desc.sale)
    async def sale_command(ctx: Context) -> None:
        __log_command(ctx, 'sale')
        await __send_message(ctx, fn.sale())


def on_command_jizz(bot: Bot) -> None:
    """
    The command listener for the jizz command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="jizz", brief=briefs.jizz, description=desc.jizz)
    async def jizz_command(ctx: Context) -> None:
        __log_command(ctx, 'jizz')
        await __send_message(ctx, fn.jizz())


def on_command_fuckyou(bot: Bot) -> None:
    """
    The command listener for the fuckyou command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="fuckyou", brief=briefs.fuckyou, description=desc.fuckyou)
    async def fuckyou_command(ctx: Context) -> None:
        __log_command(ctx, 'fuckyou')
        await __send_message(ctx, fn.fuckyou())


def on_command_joke(bot: Bot) -> None:
    """
    The command listener for the joke command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="joke", brief=briefs.joke, description=desc.joke)
    async def joke_command(ctx: Context, category: str = None) -> None:
        __log_command(ctx, 'joke', category)
        await __send_message(ctx, fn.joke(category))


def on_command_weather(bot: Bot) -> None:
    """
    The command listener for the weather command.

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="weather", brief=briefs.weather, description=desc.weather)
    async def weather_command(ctx: Context, *, city: str = None) -> None:
        __log_command(ctx, 'weather', city)
        await __send_message(ctx, fn.weather(city))

    @weather_command.error
    async def weather_error(ctx: Context, error: CommandError) -> None:
        message = err.unknown

        if isinstance(error, command_errors.MissingRequiredArgument):
            message = err.weather_blank
        await __on_error(ctx, message, 'weather')


def on_command_clear(bot: Bot) -> None:
    """
    The command listener for the clear command.

    :param bot: The bot on which to apply the listener.
    """

    @has_permissions(administrator=True)
    @bot.command(name="clear", brief=briefs.clear, description=desc.clear)
    async def clear_command(ctx: Context, pattern: str, limit: int = 100) -> None:
        messages = await ctx.channel.history(limit=limit).flatten()

        msg_starting = f"About to delete all messages that start with: {pattern} \nWithin {limit} messages."
        await __send_message(ctx, msg_starting)

        deleted = 0
        for message in messages:
            if message.content.startswith(pattern):
                await message.delete()
                deleted += 1

        __log_command(ctx, 'clear', pattern)
        msg_ending = f"{deleted} messages cleared!"
        await __send_message(ctx, msg_ending)

    @clear_command.error
    async def clear_error(ctx: Context, error: CommandError) -> None:
        message = err.unknown

        if isinstance(error, command_errors.MissingRequiredArgument):
            message = err.clear_blank

        if isinstance(error, command_errors.MissingPermissions):
            message = err.missing_permissions

        await __on_error(ctx, message, 'clear')


def on_command_gif(bot: Bot) -> None:
    """
    The command listener for the gif command.

    :param bot: The bot on which to apply the listener.
    """

    @bot.command(name="gif", brief=briefs.gif, description=desc.gif)
    async def gif_command(ctx: Context, *, search: str = None) -> None:
        __log_command(ctx, 'gif', search)
        await __send_message(ctx, fn.gif(search))


def on_command_math(bot: Bot) -> None:
    """
    The command listener for the gif command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="math", brief=briefs.math, description=desc.math)
    async def math_command(ctx: Context, *, expression: str) -> None:
        __log_command(ctx, 'math', expression)
        await __send_message(ctx, str(fn.math(expression)))

    @math_command.error
    async def math_error(ctx: Context, error: CommandError) -> None:
        message = err.unknown
        if isinstance(error, command_errors.MissingRequiredArgument):
            message = err.math_blank
        await __on_error(ctx, message, 'math')


def on_command_coinflip(bot: Bot) -> None:
    """
    The command listener for the coinflip command

    :param bot: The bot on which to apply the listener
    """

    @bot.command(name="coinflip", brief=briefs.coinflip, description=desc.coinflip)
    async def coinflip_command(ctx: Context) -> None:
        __log_command(ctx, 'coinflip')
        await __send_message(ctx, fn.coinflip())


def __log_command(ctx: Context, command_name: str, argument: str = None) -> None:
    """
    Logs a command.

    :param ctx: The context of the command
    :param command_name: The name of the command
    :param argument: The argument passed to the command
    """
    author = ctx.message.author
    write_log(f'(command) {command_name}: arg={argument}, name={author.name}, id={author.id}')


def __log_error(ctx: Context, command_name: str, error: str, argument: str = None):
    """
    Log a command error.

    :param ctx: The context of the command error
    :param command_name: The name of the command
    :param error: The error that was thrown
    :param argument: The argument passed to the command
    """
    author = ctx.message.author
    write_log(f'(error) {command_name}: error={error}, arg={argument}, name={author.name}, id={author.id}')


async def __send_message(ctx: Context, message: str, limit: int = 2000, delete_after: float = None) -> None:
    """
    Sends a long message

    If the message is longer than a certain limit, it will be sent in chunks

    :param ctx: The context
    :param message: The message to send
    :param limit: The limit of each
    :param delete_after: The time (in seconds) after which to delete the message
    """
    i = len(message)
    while i > 0:
        if i > limit:
            await ctx.send(f'{message[:limit]}', delete_after=delete_after)
            message = message[limit:]
            i -= limit
        else:
            await ctx.channel.send(f'{message[:i]}', delete_after=delete_after)
            i = 0


async def __on_error(ctx: Context, message: str, command_name: str) -> None:
    """
    When an error occurs.

    :param ctx: The context of the command error.
    :param message: The error message sent to the user
    :param command_name: The name of the command.
    """
    __log_error(ctx, command_name, message, None)
    await __send_message(ctx, message, delete_after=5)
    await ctx.message.delete(delay=5)
