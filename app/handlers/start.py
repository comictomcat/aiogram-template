from aiogram import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.markdown import hbold

from app.middlewares.throttling import rate_limit


@rate_limit(3, "start")
async def start(m: Message):
    """Responds to /start."""

    # Create an inline keyboard
    welcome_markup = InlineKeyboardMarkup()
    welcome_markup.insert(
        InlineKeyboardButton(
            "My Sources", url="https://github.com/comictomcat/aiogram-template"
        )
    )

    await m.answer(
        f"Hello there, {hbold(m.from_user.first_name)}!", reply_markup=welcome_markup
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(start, commands="start")
