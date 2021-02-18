from aiogram import Dispatcher
from aiogram.types import BotCommand
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


async def set_commands(dp: Dispatcher, commands: dict):
    """
    Set command hints
    """

    await dp.bot.set_my_commands(
        [BotCommand(command, description) for command, description in commands.items()]
    )


async def mailing(dp, users: list, message: str):
    """
    Send message to every user in the passed list
    """

    for superuser in users:
        if not superuser:
            continue

        try:
            await dp.bot.send_message(superuser, message)
        except Exception:
            continue


def parse_config(path):
    """
    Parse a config.
    """

    with open(path) as file:
        return load(file, Loader=Loader)
