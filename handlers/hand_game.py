import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from database.db_conncet import connect_db
from service.user_service import register_user

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def cmd_start(message: Message):
    logger.info("Хендлер команды старт запущен")
    tg_id = message.from_user.id
    with connect_db() as conn:
        user = register_user(tg_id, conn)
        if user:
            await message.answer("Вижу, Вы у нас впервые, ловите начальные очки )")
        else:
            await message.answer("Рад снова Вас видеть )")
