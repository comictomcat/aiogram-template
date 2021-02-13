from loguru import logger
from aiogram import executor, Dispatcher

from app import dp, config, modules


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Load modules
    loaded = modules.load()

    logger.success(f"Started with {len(loaded)} module(s).")
    logger.info(f"Modules: \n{', '.join(loaded)}")


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(
        dp, on_startup=startup, **config.executor
    )
