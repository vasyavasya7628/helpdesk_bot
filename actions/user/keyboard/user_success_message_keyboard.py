from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import return_to_main_menu


def get_kb_return() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=return_to_main_menu())
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
