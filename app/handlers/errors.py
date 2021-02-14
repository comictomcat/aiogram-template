import logging

from aiogram import Dispatcher

from app.bot import dp, config
from app.misc import mailing


async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all
    exceptions within task factory tasks.
    """

    await mailing(
        dp, config.superusers, f"Error: \n{exception} \n\n" f"Update: {update}"
    )

    logging.exception(exception)
    logging.debug(update)


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
