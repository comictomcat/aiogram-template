### [![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)  [![Aiogram](https://img.shields.io/badge/aiogram-2.11.2-blue)](https://pypi.org/project/aiogram/) ![Docker](https://img.shields.io/badge/Docker-Yes-success) 

### About
Scalable and straightforward template for bots written on aiogram with built-in handlers, filters, utils, middlewares and keyboards. 

### Setting it up
#### Preparations 
- Clone this repo via `git clone https://gitlab.com/comictomcat/aiogram-template.git` OR just download the source code;
- Move to the `aiogram-template` directory;
- Rename `.env.dist` to `.env` and replace `BOT_TOKEN` to your own token.


#### Plain Deployment
- _Optionally:_ create the [virtual environment](https://docs.python.org/3/tutorial/venv.html);
- Install dependencies `pip install -r requirements.txt`;
- Start the bot `python3 -m bot`.

#### Docker Deployment
- _Required:_ **Docker** and **Docker-Compose**
- Start the bot `sudo docker-compose up -d`.

### Project Structure
 - Application package is in `bot`;
 - Config and .env file are located in `bot/data/config.py` and `bot/data/.env` respectively;
 - Entry-point is `bot/__main__.py` (can be executed as `python -m bot`).

```
├── bot 
│   ├── data
│   │   └── config.py
│   ├── filters
│   │   ├── __init__.py
│   │   └── is_reply.py
│   ├── handlers
│   │   ├── general
│   │   │   ├── base.py
│   │   │   └── errors.py
│   │   └── __init__.py
│   ├── __main__.py
│   ├── middlewares
│   │   └── throttling.py
│   └── misc
│       ├── bot_instance.py
│       ├── keyboards
│       │   └── source_markup.py
│       └── set_commands.py
│
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
