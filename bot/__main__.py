from loguru import logger
from aiogram import executor

from bot.misc import dp, set_commands
from bot import middlewares, filters, handlers

import bot.data.config as config


async def startup(dispatcher):
    """Triggers on startup, you may
    add filters and middlewares later."""
    await set_commands(dispatcher)
    logger.info("Bot has started")


async def shutdown(dispatcher):
    """Triggers on shutdown"""
    logger.info("Bot has stopped")


if __name__ == "__main__":
    # Starts long-polling mode
    executor.start_polling(
        dp, on_startup=startup, on_shutdown=shutdown, skip_updates=config.skip_updates
    )
