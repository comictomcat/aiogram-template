from os.path import isfile
from pathlib import Path


def main():
    """
    Generate a config.
    """

    prefix = "\033[32m•\033[0m"
    project_path = Path(__file__).parent.parent.parent
    config_path = f"{project_path}/config.yml"

    print(f"{prefix} Creating default config file...")

    if isfile(config_path):

        answer = (
            input(
                f"{prefix} Config file is going to be " f"overwritten. Proceed? [Y/n] "
            )
            .strip()
            .lower()
        )

        if answer not in {"y", "yes", "yep", "sure", ""}:
            return False

    token = input(f"{prefix} Enter your token: ")
    user = input(f"{prefix} Enter your ID [None]: ")

    if not user.strip():
        user = "null"

    # Note: it's NOT a config, it's used for generating configs
    default_conf = f"""
app:
  bot:
    token: {token}
    parse_mode: html

  executor:
    skip_updates: true

  superusers:
    - {user}

  modules:
    - middlewares
    - handlers.start
    - handlers.errors

  log_ignore:
    - aiogram
    - asyncio
    - aiogram.Middleware
    - aiogram.dispatcher.dispatcher
"""

    with open(config_path, "w") as file:
        file.write(default_conf)

    print(f"{prefix} Config has successfully been created!")


if __name__ == "__main__":
    main()
