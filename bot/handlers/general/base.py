from aiogram import types
from aiogram.utils.markdown import hcode

from bot.misc import dp
import bot.data.config as config

from bot.middlewares import rate_limit
from bot.misc.keyboards import source_markup


@dp.message_handler(commands="start")
async def start(message: types.Message):
    """Responds to /start with greeting and inline keyboard,
    which's located in misc/keyboards/source_markup.py"""
    await message.answer(f"Hello there, {message.from_user.full_name}!",
                         reply_markup=source_markup)


@rate_limit(5, "help")
@dp.message_handler(commands="help")
async def commands(message: types.Message):
    """Responds to /help with list of available commands,
    which're located in data/config.py"""

    # Generates a list
    answer = ["Available commands: "]
    for command, description in config.commands:
        answer.append(hcode(f"/{command}") + f" — {description}")

    await message.answer("\n".join(answer))
