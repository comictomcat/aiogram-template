default:help
py := poetry run python

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
	$(py) -m app

update:
	poetry update

black:
	$(py) -m black .

isort:
	$(py) -m isort .

flake:
	$(py) -m flake8 .

lint: black isort flake