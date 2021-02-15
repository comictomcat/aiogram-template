import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.bot import config, dp
from app.misc import ModuleManager


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Load modules
    modules = ModuleManager(dispatcher, config.modules)
    modules.load()

    logging.info("Start polling.")


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup, **config.executor)
