from aiogram.utils.markdown import hcode, hbold
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from app import dp, bot
from app.misc import get_args
from app.config import commands

from app.middlewares import rate_limit


@dp.message_handler(commands="start")
async def start(m: Message):
    """Responds to /start with greeting and inline keyboard"""

    # Create an inline keyboard
    welcome_markup = InlineKeyboardMarkup()

    # Get bot's instance
    me = await bot.get_me()

    # Insert the source code button with a specific url
    welcome_markup.insert(InlineKeyboardButton("My Sources", url="https://gitlab.com/comictomcat/aiogram-template"))
    welcome_markup.insert(InlineKeyboardButton("Add me to your group", url=f"http://t.me/{me.username}?startgroup=true"))

    answer = (
        f"Hello there, {hbold(m.from_user.first_name)}! "
        "I'm an open-source aiogram template bot with some extras. \n\n"
        f"{hbold('Main')} commands available here: \n"
    )

    # Get visible commands
    for command in commands.visible:
        answer += f" • /{command.name} {hcode(command.usage)}: {command.desc} \n"

    answer += (
        f"\n{hbold('Note:')} You may specify a certain module with "
        f"/help in order to get docs about the command. \n\n"
    )

    await m.answer(answer, reply_markup=welcome_markup)


@rate_limit(3, "help")
@dp.message_handler(commands="help")
async def help_command(m: Message):
    """Respond to /help with a list of available commands."""

    # Get arguments
    args = get_args(m.text, maximum=1)

    # If there're no arguments, respond with a list of available commands
    if not args:
        answer = "Available commands: \n"
        for cmd in commands.list.values():
            answer += f" • /{cmd.name} {hcode(cmd.usage)}: {cmd.desc} \n"

    # Otherwise, send a manual page for a certain command
    else:

        if command := commands.get(args):
            answer = (
                hcode(f"Manual page: {command.name}\n\n") +
                hbold(f" • Usage: ") + f"/{command.name} {hcode(command.usage)} \n" +
                hbold(f" • Description: \n") + command.desc
            )

        else:
            answer = "Module was not found."

    await m.answer(answer)


@dp.message_handler(commands="ping")
async def ping(m: Message):
    """Respond to /ping."""
    await m.answer("Pong!")

