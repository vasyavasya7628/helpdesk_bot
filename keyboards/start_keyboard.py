from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import text_write_to_it, text_admin_login, text_order_list


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=text_write_to_it())
    kb.button(text=text_admin_login())
    kb.button(text=text_order_list())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
