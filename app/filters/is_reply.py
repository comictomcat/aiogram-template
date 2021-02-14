from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class IsReply(BoundFilter):
    """
    Check if message is reply to another message.
    """

    async def check(self, message: Message):
        return message.reply_to_message


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsReply)
