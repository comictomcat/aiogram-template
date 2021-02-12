default:help

help:
	@echo "USAGE"
	@echo "   make <command>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  config	Generate a default config"
	@echo "  install	Install dependencies"
	@echo "  run		Start a bot"
	@echo "  update	Update dependencies"
	@echo "  version	View version of packages"

# ========
# Commands
# ========

config:
	poetry run python app/misc/confgen.py

install:
	poetry install

run:
	poetry run python -m app

update:
	poetry update