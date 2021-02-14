default:help

help:
	@echo "USAGE"
	@echo "  make <commands>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  config	Generate a default config"
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

config:
	python -m poetry run python app/misc/confgen.py

install:
	python -m poetry install

run:
	python -m poetry run python -m app

update:
	python -m poetry update


black:
	python -m poetry run python -m black .

isort:
	python -m poetry run python -m isort .

flake:
	python -m poetry run python -m flake8 .

lint:
	$(MAKE) black
	$(MAKE) isort
	$(MAKE) flake