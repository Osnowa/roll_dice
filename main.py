import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import config

# Инициализация логгера в файле
logger = logging.getLogger(__name__)

async def main():
    '''Основная функция'''
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info("Старт Бота")

    bot = Bot(token=config.conf_bot.Bot_token)
    dp = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    '''Запуск бота'''
    asyncio.run(main())