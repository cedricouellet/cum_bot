#!/usr/bin/env python3

"""
CumBot v0.1.0

A not so family-friendly Discord bot

Made for fun on my personal Discord server
"""

import os
import asyncio
from dotenv import load_dotenv

import commands.commands as c
from discord_bot import DiscordBot

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
IS_PROD = ENVIRONMENT.lower().startswith('prod')


listeners = [
    # Tag commands
    c.on_command_jew,
    c.on_command_crackhead,
    c.on_command_loser,

    # Parameterized commands
    c.on_command_joke,
    c.on_command_gif,
    c.on_command_math,

    # Simple commands
    c.on_command_jizz,
    c.on_command_sale,
    c.on_command_oleg,
    c.on_command_fuckyou,
]
bot = DiscordBot(is_dev=not IS_PROD, command_listeners=listeners)


async def __up() -> None:
    await bot.run(discord_token=DISCORD_TOKEN)


async def __down() -> None:
    await bot.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(__up())
    except KeyboardInterrupt:
        print('Exiting...')
        loop.run_until_complete(__down())
        exit(0)
    except:  # noqa (we want to crash on any other exception)
        print('Crash...')
        loop.run_until_complete(__down())
        exit(1)
