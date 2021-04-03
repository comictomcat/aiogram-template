default:help
py := poetry run python

help:
	@echo "USAGE"
	@echo "  make <commands>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  run		Start a bot"
	@echo "  flake		Run flake8"
	@echo "  black		Run black"
	@echo "  isort		Run isort"
	@echo "  lint		Reformat code"


# ========
# Commands
# ========

run:
	$(py) -m app

black:
	$(py) -m black .

isort:
	$(py) -m isort .

flake:
	$(py) -m flake8 .

lint: black isort flake