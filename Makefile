default:help

help:
	@echo "USAGE"
	@echo "  make <commands>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  install	Install dependencies"
	@echo "  run		Start a bot"
	@echo "  update	Update dependencies"
	@echo "  flake		Run flake8"
	@echo "  black		Run black"
	@echo "  isort		Run isort"
	@echo "  lint		Reformat code"


# ========
# Commands
# ========

install:
	poetry install

run:
	poetry run python -m app

update:
	poetry update

black:
	poetry run python -m black .

isort:
	poetry run python -m isort .

flake:
	poetry run python -m flake8 .

lint: black isort flake