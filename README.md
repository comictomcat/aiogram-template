### [![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)  [![Aiogram](https://img.shields.io/badge/aiogram-2.11.2-blue)](https://pypi.org/project/aiogram/) 

### About
Scalable and straightforward template for bots written on [aiogram](https://github.com/aiogram/aiogram) with built-in handlers, utils, middleware, filter and a few extras. Inspired by a couple of other templates mentioned later.

### Setting it up
#### Preparations
- Clone this repo via `git clone https://gitlab.com/comictomcat/aiogram-template.git`;
- Move to the directory `cd aiogram-template`;
- Specify your token `echo "token <token>" > .secret`. (Replace <token> with your own one.)

#### Plain Deployment
- _Optionally:_ create the [virtual environment](https://docs.python.org/3/tutorial/venv.html);
- Install dependencies `pip install -r requirements.txt`;
- Start the bot `python3 -m app`. (or just `python`)

#### Project Structure
 - Application package is in `app`;
 - Config and .env file are located in `app/config.py` and `bot/data/.env` respectively;
 - Entry-point is `app/__main__.py` (can be executed as `python3 -m app`).

### Other templates
 - [aiogram-bot-template](https://github.com/Latand/aiogram-bot-template) by Latand
 - [aiogram-template](https://github.com/F0rzend/aiogram-template) by F0rzend
 - [tgbot_template](https://github.com/Tishka17/tgbot_template) by Tishka17
 - [aiogram-bot-template](https://github.com/Forden/aiogram-bot-template) by F0rden