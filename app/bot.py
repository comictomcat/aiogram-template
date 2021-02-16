import logging.config
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rich.logging import RichHandler

from app.misc import ModuleManager, parse_config

# Project directory
ROOT_DIRECTORY = Path(__file__).parent.parent

# Config
config = parse_config(ROOT_DIRECTORY / "config.yaml")

# Bot, storage and dispatcher instances
bot = Bot(**config.get("bot"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Ignore certain loggers
for i in config.get("log_ignore"):
    logger = logging.getLogger(i)
    logger.disabled = True

# Configure logging
logging.basicConfig(
    level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)
