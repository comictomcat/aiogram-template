from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.bot import ROOT_DIRECTORY, config
from app.misc import ModuleManager, set_commands


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Load modules
    modules = ModuleManager(dispatcher, ROOT_DIRECTORY / "app")
    modules.load_all(config.get("modules"))

    # Set command hints
    await set_commands(dispatcher, config.get("commands"))


if __name__ == "__main__":
    # Bot, storage and dispatcher instances
    bot = Bot(**config.get("bot"))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup, **config.get("executor"))
