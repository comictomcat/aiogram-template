from app.misc import read_secret
from app.misc import CommandsManager

# Read .secret file
secret = read_secret()

# Telegram Bot API Token
BOT_TOKEN = secret.get("token")

# Whether to skip updates or not
SKIP_UPDATES = True

# The default parse mode
PARSE_MODE = "HTML"

# Commands
commands = CommandsManager()
commands.add("start", "Start conversation with me")
commands.add("help", "List of available commands.", "[module]", visible=True)
commands.add("ping", "See whether I'm alive or not", visible=True)
