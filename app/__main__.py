import logging

from aiogram import Dispatcher, executor

from app.bot import config, dp, modules


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Load modules
    modules.load()
    logging.debug("Modules: " + ", ".join(modules.loaded))
    logging.info("Start polling.")


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup, **config.executor)
