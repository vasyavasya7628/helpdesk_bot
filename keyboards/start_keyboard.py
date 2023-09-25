from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import res.resources as res


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=res.text_write_to_it())
    kb.button(text=res.text_admin_login())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
