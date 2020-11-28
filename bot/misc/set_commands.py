from aiogram import types
from bot.data.config import commands


async def set_commands(dp):
    await dp.bot.set_my_commands(
        [types.BotCommand(name, description) for name, description in commands]
    )
