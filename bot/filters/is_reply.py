from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsReply(BoundFilter):
    """Checks if message is reply to another message"""

    async def check(self, message: types.Message):
        return message.reply_to_message
