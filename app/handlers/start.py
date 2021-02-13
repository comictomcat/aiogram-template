from aiogram.utils.markdown import hbold
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from app import dp
from app.middlewares import rate_limit


@dp.message_handler(commands="start")
async def start(m: Message):
    """Responds to /start."""

    # Create an inline keyboard
    welcome_markup = InlineKeyboardMarkup()
    welcome_markup.insert(InlineKeyboardButton("My Sources", url="https://github.com/comictomcat/aiogram-template"))

    msg = await m.answer(f"Hello there, {hbold(m.from_user.first_name)}!", reply_markup=welcome_markup)
    await msg.edit_text(f"Hello there, {hbold(m.from_user.first_name)}!", reply_markup=welcome_markup)
