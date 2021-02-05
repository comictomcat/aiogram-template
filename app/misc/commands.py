from aiogram.types import BotCommand


class Command:
    def __init__(self, name, desc, usage, visible):
        self.name = name
        self.desc = desc
        self.usage = usage
        self.visible = visible


class CommandsManager:
    def __init__(self):
        self.list = {}

    def add(self, name: str, desc: str, usage: str = "", visible: bool = False):
        self.list[name] = Command(name, desc, usage, visible)

    def get(self, name: str) -> Command or bool:
        return self.list.get(name)

    @property
    def visible(self) -> set:
        return {value for value in self.list.values() if value.visible}

    async def set(self, dispatcher):
        await dispatcher.bot.set_my_commands(
            [BotCommand(command.name, f"{command.usage} {command.desc}")
             for command in self.visible])


