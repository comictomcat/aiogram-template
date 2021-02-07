from loguru import logger

from app import dp
from .is_reply import IsReply


if __name__ == "app.filters":
    logger.info("Configuring filters...")
    dp.filters_factory.bind(IsReply)
