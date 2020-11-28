from envparse import env

# Simply reads env file and assigns token variable
env.read_envfile()
BOT_TOKEN = env.str("BOT_TOKEN")

# Whether to skip updates or not
skip_updates = False

# List of commands
commands = (
    ("start", "See if the ship is sailing"),
    ("help", "Get the command list"),
)
