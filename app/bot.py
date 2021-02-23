import logging.config
from pathlib import Path

from rich.logging import RichHandler

from app.misc import parse_config

# Project directory
ROOT_DIRECTORY = Path(__file__).parent.parent

# Config
config = parse_config(ROOT_DIRECTORY / "config.yaml")

# Ignore certain loggers
for logger in config.get("log_ignore"):
    current_logger = logging.getLogger(logger)
    current_logger.disabled = True

# Configure logging
logging.basicConfig(
    level="NOTSET", format="%(message)s", datefmt="%X |", handlers=[RichHandler()]
)
