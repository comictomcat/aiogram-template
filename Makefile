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
	@echo "  reformat	Reformat code"

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

reformat:
	python -m poetry run python -m black .