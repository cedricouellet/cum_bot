import os
import discord
import asyncio
from dotenv import load_dotenv
from DiscordBot import DiscordBot

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
TOKEN = os.getenv('DISCORD_TOKEN')

IS_PROD = ENVIRONMENT.lower().startswith('prod')

bot = DiscordBot(dev=IS_PROD == False)

async def up() -> None:
    await bot.run(token=TOKEN)


async def down() -> None:
    await bot.stop()

    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(up())
    except KeyboardInterrupt:
        print('Exiting...')
        loop.run_until_complete(down())
        exit(0)
    except:
        print('Crash...')
        loop.run_until_complete(down())
        exit(1)

    
