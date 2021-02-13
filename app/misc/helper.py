from aiogram.types import BotCommand


def get_args(text: str, maximum: int = 2):
    """Get command arguments."""

    if maximum <= 0:
        maximum = -1
    elif maximum == 1:
        args = text.split(maxsplit=maximum)[1:]
        if args:
            return args[0]
        else:
            return args

    return text.split(maxsplit=maximum)[1:]


async def set_commands(dp, commands: dict):
    await dp.bot.set_my_commands(
        [BotCommand(command, description)
         for command, description in commands.items()])


async def mailing(dp, users: list, message: str):
    
    # Iterate through superusers and try to send an error message
    for superuser in users:
        if not superuser:
            continue

        try:
            await dp.bot.send_message(superuser, message)
        except:
            continue
