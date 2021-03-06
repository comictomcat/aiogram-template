from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


async def start_command(m: Message):
    """
    Responds to /start.
    """

    # Create an inline keyboard
    welcome_markup = InlineKeyboardMarkup()

    # Insert a button with a url
    welcome_markup.insert(
        InlineKeyboardButton(
            "My Sources", url="https://github.com/comictomcat/aiogram-template"
        )
    )

    await m.answer(
        f"Hello there, <b>{m.from_user.first_name}</b>!", reply_markup=welcome_markup
    )
