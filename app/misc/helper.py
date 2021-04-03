from aiogram import Bot
from aiogram.types import BotCommand
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


async def set_commands(bot: Bot, commands: dict):
    """
    Set command hints
    """

    await bot.set_my_commands(
        [BotCommand(command, description) for command, description in commands.items()]
    )


def parse_config(path):
    """
    Parse a config.
    """

    with open(path) as file:
        return load(file, Loader=Loader)
