from __future__ import annotations

from pathlib import Path
from typing import Union

import yaml


class Config:
    """
    YAML config parser
    """

    def __init__(self, path: Union[Path, str]):
        """
        A Config constructor
        :param path: path to config file
        :type path: Union[Path, str]
        """

        with open(path) as file:
            self.config = yaml.load(stream=file, Loader=yaml.CLoader)

        self._set_shortcuts()

    def _set_shortcuts(self):
        """
        A private method that sets shortcut for elements in `app`
        it's created to be able use config.bot instead of config.app.get('bot') and others
        """
        for key, value in self.app.items():
            setattr(self, key, value)

    def __getattr__(self, key, default=None):
        if default is None:
            default = dict()

        return self.config.get(key, default)

    def get(self, key, default=None) -> dict:
        return self.__getattr__(key, default)
