import logging

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import res.resources as text


def adm_buttons_from_districts(kb):
    districts_copy = text.get_districts()
    for i in range(len(districts_copy) - 1):
        if i % 2 == 0:
            logging.info(f"➡{districts_copy[i]}")
            kb.button(text="➡" + districts_copy[i])


def adm_districts_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню")
    adm_buttons_from_districts(kb)
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
