import logging

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def kb_waiting_reaction(admin_id, order_number) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Взять заявку", callback_data=f"get_order|{admin_id}|{order_number}")
    logging.info(f"ИД АДМИНА = {admin_id}")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
