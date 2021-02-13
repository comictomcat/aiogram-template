from importlib import import_module

from loguru import logger
from aiogram import Dispatcher


class ModuleManager:
    """
    Module Manager.
    """

    def __init__(self, dp: Dispatcher, modules):
        self.dp = dp
        self.modules = modules

    def load(self):
        loaded = list()
        for module in self.modules:
            imported = import_module("app." + module)

            if hasattr(imported, "setup"):
                if callable(imported.setup):
                    imported.setup(self.dp)
                    loaded.append(imported.__name__)
                else:
                    logger.error(f"Setup attribute is NOT callable in module <{imported.__name__}>")
            else:
                logger.error(f"Module <{imported.__name__}> was not loaded due to lack of "
                             f"setup attribute.")
        
        return loaded
