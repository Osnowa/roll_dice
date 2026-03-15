import asyncio
import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram.types import CallbackQuery

from database.db_conncet import connect_db
from database.users_add_get import get_user
from database.score_db import score_minus, user_is_game
from service.user_service import register_user

from keyboard.keyboard_play import keyboard_yes_no
from game_logic.move_opponent import move_opponent, move_me

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


@router.message(Command("play"))
async def cmd_play(message: Message):
    tg_id = message.from_user.id
    with connect_db() as conn:
        user = get_user(conn, tg_id)
        #### поставить что режим в игре активен
        user_is_game(conn, tg_id, activ=1)  # режим игры активен
        await message.answer(
            f"Ваши очки {user["score"]} \n"
            "Пожалуйста введите вашу ставку"
        )


@router.message(lambda x: x.text and x.text.isdigit() and int(x.text) > 0)
async def cmd_tav(message: Message):
    tg_id = message.from_user.id
    with connect_db() as conn:
        user = get_user(conn, tg_id)
        if user["is_game"]:
            if user["score"] >= int(message.text):
                score_minus(conn, tg_id, int(message.text))  # списание очков
                await message.answer(
                    f"Ваша ставка принята \n"
                    "Как вы думаете, Вы выбросите больше оппонента ?",
                    reply_markup=keyboard_yes_no()
                )
            else:
                await message.answer(
                    f"Извини, у тебя недостаточно очков для такой ставки\n"
                    f"Попробуй ввести другую ставку"
                )
        else:
            await message.answer(
                f"Дружище, ты еще не в игре, что бы я принимал твою ставку"
            )


@router.callback_query(lambda x: x.data == "yes")
async def callback_yes(cb: CallbackQuery):
    tg_id = cb.message.from_user.id
    m_o1, m_o2 = move_opponent()
    m_o_itog = sum((m_o1, m_o2))
    await cb.message.edit_text(
        f"Противник выбрасывает {m_o1} на первой кости \n"
        f"Противник выбрасывает {m_o2} на второй кости \n"
        f"Итого {m_o_itog} \n"
    )
    await asyncio.sleep(2)

    m1, m2 = move_me()
    m_itog = sum((m1, m2))

    if m_itog > m_o_itog:
        await cb.message.edit_text(
            f"Вы выбросили {m1} на первой кости \n"
            f"Вы выбросили {m2} на второй кости \n"
            f"Поздравляю, Вы Победили !"
        )


@router.callback_query(lambda x: x.data == "yes")
async def callback_yes(cb: CallbackQuery):
    tg_id = cb.message.from_user.id
    m_o1, m_o2 = move_opponent()
    m_o_itog = sum((m_o1, m_o2))
    await cb.message.edit_text(
        f"Противник выбрасывает {m_o1} на первой кости \n"
        f"Противник выбрасывает {m_o2} на второй кости \n"
        f"Итого {m_o_itog} \n"
    )
    await asyncio.sleep(2)

    m1, m2 = move_me()
    m_itog = sum((m1, m2))

    if m_itog > m_o_itog:
        await cb.message.edit_text(
            f"Вы выбросили {m1} на первой кости \n"
            f"Вы выбросили {m2} на второй кости \n"
            f"Поздравляю, Вы Победили !"
        )
