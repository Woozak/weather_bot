from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    bot_token: str


@dataclass
class Config:
    tg_bot: TgBot
    openweathermap_key: str


def load_config(path=None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(bot_token=env('BOT_TOKEN')),
        openweathermap_key=env('OPENWEATHERMAP_KEY')
    )
