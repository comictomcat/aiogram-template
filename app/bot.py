import logging.config
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rich.logging import RichHandler

from app.misc import Config, ModuleManager

# Project directory
ROOT_DIRECTORY = Path(__file__).parent.parent

# Config
config = Config(ROOT_DIRECTORY / "config.yml")

# Bot, storage and dispatcher instances
bot = Bot(**config.bot)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Module instance for current dispatcher
modules = ModuleManager(dp, config.modules)

# Ignore certain loggers
for i in config.log_ignore:
    logger = logging.getLogger(i)
    logger.disabled = True

# Configure logging
logging.basicConfig(
    level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)
