from app.misc import read_secret

# Read .secret file
secret = read_secret()

# Telegram Bot API Token
BOT_TOKEN = secret.get("token")

# Whether to skip updates or not
SKIP_UPDATES = True

# The default parse mode
PARSE_MODE = "HTML"

# Commands
commands = {
    "start": "Start conversation with me",
    "help": "List of available commands",
    "ping": "See whether I'm alive or not"
}

