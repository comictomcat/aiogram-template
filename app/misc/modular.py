import logging
from importlib import import_module

from aiogram import Dispatcher


class ModuleManager:
    """
    Module Manager.
    """

    def __init__(self, dp: Dispatcher, modules):
        """
        A Config constructor
        :param dp: Dispatcher
        :type modules: Iterable
        """
        self.dp = dp
        self.modules = modules
        self.loaded = []

    def load(self):
        """
        This method goes through modules and imports them.
        If module has <setup> attribute and it's callable,
        it executes it.
        """

        for module in self.modules:
            imp_module = import_module("app." + module)
            module_name = imp_module.__name__

            if not hasattr(imp_module, "setup"):
                logging.error(f"Module <{module_name}> doesn't seem to have <setup>.")
                return

            if not callable(imp_module.setup):
                logging.error(f"<setup> is not callable in <{module_name}>")
                return

            imp_module.setup(self.dp)
            self.loaded.append(module_name)
