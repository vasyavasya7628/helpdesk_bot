import logging

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import res.resources as res


def list_to_buttons(kb, emoji):
    districts_copy = res.get_districts()
    for i in range(len(districts_copy) - 1):
        if i % 2 == 0:
            logging.info(f"{emoji}{districts_copy[i]}")
            kb.button(text=f"{emoji}" + districts_copy[i])


def kb_user_districts() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню")
    list_to_buttons(kb, "✅")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
