from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def keyboard_yes_no():
    """Создаем клавиатуру согласия на игру"""
    # создаём кнопки
    button_yes = InlineKeyboardButton(text="Больше", callback_data="yes")
    button_no = InlineKeyboardButton(text="Меньше", callback_data="no")

    # создаём клавиатуру с одним рядом
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[[button_yes, button_no]]
    )

    return inline_kb