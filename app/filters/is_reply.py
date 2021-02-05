from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter


class IsReply(BoundFilter):
    """Check if message is reply to another message."""

    async def check(self, message: Message):
        return message.reply_to_message
