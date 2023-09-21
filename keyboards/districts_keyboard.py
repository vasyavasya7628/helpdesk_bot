from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import res.resources as text


def get_kb_districts() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню")
    add_buttons_from_districts(kb)
    kb.button(text="Здесь  список ведомств")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def add_buttons_from_districts(kb):
    districts_copy = text.get_districts()
    for i in range(len(districts_copy) - 1):
        if i % 2 == 0:
            kb.button(text=districts_copy[i])
            # save id to var to use it for sending message
            person_id = districts_copy[i + 1]
