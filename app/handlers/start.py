from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from app.middlewares.throttling import rate_limit


@rate_limit(3, "start")
async def start_command(m: Message):
    """Responds to /start."""

    # Create an inline keyboard
    welcome_markup = InlineKeyboardMarkup()
    welcome_markup.insert(
        InlineKeyboardButton(
            "My Sources", url="https://github.com/comictomcat/aiogram-template"
        )
    )

    await m.answer(
        f"Hello there, <b>{m.from_user.first_name}</b>!", reply_markup=welcome_markup
    )
