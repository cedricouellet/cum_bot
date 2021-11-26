#!/usr/bin/env python3

"""
CumBot v0.1.0

A not so family-friendly Discord bot

Made for fun on my personal Discord server
"""

import os
import asyncio
from dotenv import load_dotenv
from DiscordBot import DiscordBot

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

IS_PROD = ENVIRONMENT.lower().startswith('prod')

bot = DiscordBot(dev=IS_PROD is False, giphy_api_key=GIPHY_API_KEY)


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
    except: # noqa (we want to crash on any other exception)
        print('Crash...')
        loop.run_until_complete(__down())
        exit(1)
