def handle_add(bot):
    @bot.command(name="add")
    async def add(ctx, *numbers):
        _sum = 0
        for num in numbers:
            _sum += int(num)
        response = f'{_sum}'
        await ctx.send(response)
