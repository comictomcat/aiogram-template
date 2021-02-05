from pathlib import Path


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


def read_secret(path: str = ".secret"):
    """Read a secret file."""

    root = f"{Path(__file__).parent.parent.parent}/{path}"
    values = {}
    with open(root) as file:
        for line in file:

            # Ignore line, if it starts with hash symbol
            if line.startswith("#"):
                continue

            # Parse the line
            arguments = line.split()

            # Check if the line meets syntax (key value)
            if 2 < len(arguments) > 2:
                continue

            # Assign a value
            values[arguments[0]] = arguments[1]

    return values
