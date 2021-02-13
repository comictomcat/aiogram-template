from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.misc import Config, ModuleManager

# Project directory
ROOT_DIRECTORY = Path(__file__).parent.parent

# Config
config = Config(ROOT_DIRECTORY / "config.yml")

# Bot, storage and dispatcher instances
bot = Bot(**config.bot)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

modules = ModuleManager(dp, config.modules)
