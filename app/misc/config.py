from pathlib import Path

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config:
    """
    YAML config parser
    """

    def __init__(self, path: str or Path):
        """
        A Config constructor
        :param path: path to config file
        :type path: Union[Path, str]
        """

        with open(path) as file:
            self.config = yaml.load(stream=file, Loader=Loader)

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
