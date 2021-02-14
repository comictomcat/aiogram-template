from aiogram import filters
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

from app.middlewares import rate_limit


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


def setup(dispatcher):
    dispatcher.register_message_handler(start, filters.Command(commands="start"))
