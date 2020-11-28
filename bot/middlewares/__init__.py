from loguru import logger

from bot.misc import dp
from .throttling import ThrottlingMiddleware, rate_limit


if __name__ == "bot.middlewares":
    logger.info("Configuring middlewares")
    dp.middleware.setup(ThrottlingMiddleware())
