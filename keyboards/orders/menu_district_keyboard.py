import logging

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import Text


def list_to_buttons(kb, emoji):
    districts_copy = Text.GET_DISTRICTS.value
    for i in range(len(districts_copy) - 1):
        if i % 2 == 0:
            logging.info(f"{emoji}{districts_copy[i]}")
            kb.button(text=f"{emoji}" + districts_copy[i])


def kb_menu_districts() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=Text.MENU.value)
    list_to_buttons(kb, "💼")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
