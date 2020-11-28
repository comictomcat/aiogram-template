from loguru import logger

from bot.misc import dp
from .is_reply import IsReply


if __name__ == "bot.filters":
    logger.info("Configuring filters")
    dp.filters_factory.bind(IsReply)
