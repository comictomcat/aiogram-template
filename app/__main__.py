from loguru import logger
from aiogram import executor, Dispatcher

# noinspection PyUnresolvedReferences
from app import dp, middlewares, filters, handlers
from app.config import SKIP_UPDATES, commands


async def startup(dp: Dispatcher):
    """Triggers on startup."""
    await commands.set(dp)
    logger.info("Bot has started")


async def shutdown(dp: Dispatcher):
    """Triggers on shutdown."""
    logger.info("Bot has stopped")


if __name__ == "__main__":
    """Start long-polling mode"""
    executor.start_polling(
        dp, on_startup=startup, on_shutdown=shutdown, skip_updates=SKIP_UPDATES
    )
