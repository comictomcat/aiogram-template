from loguru import logger

from app import dp
from .throttling import ThrottlingMiddleware, rate_limit


if __name__ == "app.middlewares":
    logger.info("Configuring middlewares")
    dp.middleware.setup(ThrottlingMiddleware())
