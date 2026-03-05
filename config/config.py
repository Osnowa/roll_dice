from environs import Env
from dataclasses import dataclass

env = Env()
env.read_env()

@dataclass
class Config:
    '''Настройки конфигурация бота'''
    Bot_token: str

conf_bot = Config(env.str("BOT_TOKEN"))



