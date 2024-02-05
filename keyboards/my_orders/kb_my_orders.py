import logging

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def kb_my_orders(admin_id, order_number) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Закрыть++", callback_data=f"close|{admin_id}|{order_number}")
    logging.info(f"ИД АДМИНА = {admin_id}")
    kb.button(text="Отложить--", callback_data=f"delay|{admin_id}|{order_number}")
    logging.info(f"ИД ЗАЯВКИ = {order_number}")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
