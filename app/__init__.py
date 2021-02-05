from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import BOT_TOKEN, PARSE_MODE

# Bot, storage and dispatcher instances
bot = Bot(token=BOT_TOKEN, parse_mode=PARSE_MODE)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Template version
__version__ = "0.0.1 (unstable)"
