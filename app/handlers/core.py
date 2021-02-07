from aiogram.utils.markdown import hbold
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from app import dp, bot
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
        f" • /help: {commands['help']} \n"
        f" • /ping: {commands['ping']} \n\n"
        f"{hbold('Note:')} You may specify a certain module with "
        f"/help in order to get docs about the command."
    )

    await m.answer(answer, reply_markup=welcome_markup)


@rate_limit(3, "help")
@dp.message_handler(commands="help")
async def help_command(m: Message):
    """Respond to /help with a list of available commands."""

    answer = "Available commands: \n"
    for command, description in commands.items():
        answer += f" • /{command}: {description}\n"

    await m.answer(answer)


@rate_limit(3, "ping")
@dp.message_handler(commands="ping")
async def ping(m: Message):
    """Respond to /ping."""

    await m.answer("Pong!")

