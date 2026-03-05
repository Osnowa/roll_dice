from aiogram import Bot
from aiogram.types import BotCommand

async def set_main_menu(bot: Bot):
    '''Настройка основного меню'''
    main_menu_commands = [
        BotCommand(
            command='/start',
            description='Стар бота'
        ),
        BotCommand(
            command='/profile',
            description='Ваш профиль'
        ),
        BotCommand(
            command='/play',
            description='Запуск игры'
        ),
        BotCommand(
            command='/top',
            description='Топ игроков по очкам'
        ),
        BotCommand(
            command='/stats',
            description='Ваша статистика игр'
        ),
        BotCommand(
            command='/help',
            description='Помощь'
        )
    ]
    await bot.set_my_commands(main_menu_commands)

