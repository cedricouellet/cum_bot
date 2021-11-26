from enum import Enum


class CommandType(Enum):
    ADD = 1
    SUBTRACT = 2


def add_command(bot, command_type: CommandType):
    if command_type is CommandType.ADD:
        @bot.command(name="add")
        async def add(ctx, *numbers):
            _sum = 0
            for num in numbers:
                _sum += int(num)
            response = f'{_sum}'
            await ctx.send(response)

    if command_type is CommandType.SUBTRACT:
        @bot.command(name="subtract", )
        async def subtract(ctx, *numbers):
            _sum = 0
            for num in numbers:
                _sum -= int(num)
            response = f'{_sum}'
            await ctx.send(response)
