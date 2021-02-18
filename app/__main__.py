import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.bot import config, dp
from app.misc import ModuleManager, set_commands


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Load modules
    modules = ModuleManager(dispatcher)
    modules.load_all(config.get("modules"))

    await set_commands(dispatcher, config.get("commands"))


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup, **config.get("executor"))
