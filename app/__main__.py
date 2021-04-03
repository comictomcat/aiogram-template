from aiogram import Dispatcher, executor

from app import handlers
from app.bot import config, dp
from app.misc import set_commands


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    handlers.setup(dispatcher)

    # Set command hints
    await set_commands(dispatcher, config.get("commands"))


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup, **config.get("executor"))
