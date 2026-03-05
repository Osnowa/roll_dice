import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import config, logging_conf

from keyboard import set_menu
from database import create_table

# Инициализация логгера в файле
logger = logging.getLogger(__name__)


async def main():
    """Основная функция"""

    # настройки логирования
    logging_conf.conf_logging()

    logger.info("Старт Бота")

    bot = Bot(
        token=config.conf_bot.Bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    create_table.init_db()

    await set_menu.set_main_menu(bot)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    '''Запуск бота'''
    asyncio.run(main())
